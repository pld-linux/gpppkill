Summary:	Finishes idle ppp connection. X11/gtk+ program
Summary(pl.UTF-8):	Program X11/GTK+ kończący nieaktywne połączenie ppp
Name:		gpppkill
Version:	1.0.3
Release:	0.1
Epoch:		1
License:	GPL
Vendor:		The gpppkill Team
Group:		X11/Applications/Networking
# Native URL is http: only, but we prefer ftp:
# Source0:	http://www.pla.net.py/home/oliver/gpppkill/archive/%{name}-%{version}.tar.gz
Source0:	ftp://metalab.unc.edu/pub/Linux/system/network/serial/ppp/%{name}-%{version}.tar.gz
# Source0-md5:	222279e531a57ff21b918d04561146ba
Patch0:		%{name}-warning.patch
URL:		http://www.pla.net.py/home/oliver/gpppkill/
BuildRequires:	gtk+-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gpppkill is a X11 program for Linux that finishes the ppp connection
if it not receive a minimal amount of bytes during certain time. It
also show the ppp traffic in a graph. Al configuration is done via the
GUI. Detects all pppds and let you choose which to use.

%description -l pl.UTF-8
gpppkill to program dla X, który kończy połączenie ppp jeśli w danym
okresie czasu nie otrzyma minimalnej ilości bajtów. Ukazuje on również
ruch ppp w formie wykresu. Konfiguruje się go za pomocą GUI. Wykrywa
wszystkie pppd i pyta, którego użyć.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cxx}" \
	CFLAGS="%{rpmcxxflags} -Wall -Wno-unused -Wno-deprecated -fpermissive -DGTK_DISABLE_COMPAT_H"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install gpppkill $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG CONTRIBUTORS README
%attr(755,root,root) %{_bindir}/*
