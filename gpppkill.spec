Summary:	Finishes idle ppp connection. X11/gtk+ program
Summary(pl):	Program X11/GTK+ koñcz±cy nieaktywne po³±czenie ppp
Name:		gpppkill
Version:	1.0.2
Release:	1
Epoch:		1
License:	GPL
Vendor:		The gpppkill Team
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
# Native URL is http: only, but we prefer ftp:
# Source0:	http://www.pla.net.py/home/oliver/gpppkill/archive/%{name}-%{version}.tar.gz
Source0:	ftp://metalab.unc.edu/pub/Linux/system/network/serial/ppp/%{name}-%{version}.tar.gz
URL:		http://www.pla.net.py/home/oliver/gpppkill/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	gpppkill

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
gpppkill is a X11 program for Linux that finishes the ppp connection
if it not receive a minimal amount of bytes during certain time. It
also show the ppp traffic in a graph. Al configuration is done via the
GUI. Detects all pppds and let you choose which to use.

%description -l pl
gpppkill to program dla X, który koñczy po³±czenie ppp je¶li w danym
okresie czasu nie otrzyma minimalnej ilo¶ci bajtów. Ukazuje on równie¿
ruch ppp w formie grafu. Konfiguruje sie go za pomoc± GUI. Wykrywa
wszystkie pppd i pyta, którego u¿yæ.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d ${RPM_BUILD_ROOT}%{_prefix}/X11R6/bin
%{__make} install DESTDIR=${RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG
%attr(755,root,root) %{_bindir}/*
