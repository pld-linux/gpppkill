Summary:   Finishes idle ppp connection. X11/gtk+ program.
Summary(pl):   Program X11/GTK+ ko�cz�cy nieaktywne po��czenie ppp.
Name:      gpppkill
Version:   1.0.2
Release:   1
Serial:    1
Copyright: GPL
Group:     Applications/Internet
Group(pl):     Aplikacje/Internet

Source:    gpppkill-1.0.2.tar.gz

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:  gpppkill

Vendor:    The gpppkill Team
Url:       http://www.pla.net.py/home/oliver/gpppkill/

Packager:  Oliver Schulze L. <oliver@pla.net.py>
Distribution: gpppkill custom RPM (RH6.1)

%description
gpppkill is a X11 program for Linux that finishes the ppp connection if it 
not receive a minimal amount of bytes during certain time.
It also show the ppp traffic in a graph. Al configuration is done via the GUI.
Detects all pppds and let you choose which to use.

%description -l pl
gpppkill to program dla X, kt�ry ko�czy po��czenie ppp je�li w danym okresie 
czasu nie otrzyma minimalnej ilo�ci bajt�w. Ukazuje on r�wnie� ruch ppp
w formie grafu. Konfiguruje sie go za pomoc� GUI. Wykrywa wszystkie pppd
i pyta, kt�rego u�y�.

%changelog
* Tue Aug 17 1999 Oliver Schulze L. <oliver@pla.net.py>
- can change the size of the dialog windows any more.
- bugfix: if gpppkill detect a pppd after one has ended, the bars start at the
  right of the grah the first time the scale is changed.
- resolved dinamic graph size. Now you can use any size of fonts, gpppkill will
  make the graph size dinamicaly
- typo in Help->About 
- cutting edge build: RPM 3.0.2, gtk+ 1.2.3
- changed the RPM group from 'X11/Applications/Networking' to
  'Applications/Internet'
- well, back in bussiness again. :-)

* Mon Aug 16 1999 Jean-Louis Leroy <jll@skynet.be>
- thanks to that, gpppkill can now run from /etc/ppp/ip-* scripts!
- in pppkill::es_mi_proceso() now using geteuid(2) and getegid(2) insteed of
  getuid(2) and getgid(2).

* Mon May 31 1999 Alfred Weyers <alfred@otto.gia.RWTH-Aachen.DE>
- in rcgpppkill::check_version() the rc template was writen twice

* Tue May 28 1999 Oliver Schulze <oliver@pla.net.py>
- all goals completed. Expect new features from now.
- stable release
- "refresh list" button in Interfaces tab.
- new popup menu
- code clean up for 1.0.0.
- more intiutive preferences window

* Tue May 18 1999 Oliver Schulze <oliver@pla.net.py>
- stable release
- bug fixed, code clean up and new classes.
- new preferences window
- got statusbar

%prep
%setup

%build
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi

mkdir -p ${RPM_BUILD_ROOT}/usr/X11R6/bin
make install DESTDIR=${RPM_BUILD_ROOT}

%clean
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi

%files
%doc README INSTALL GPL-LICENSE CHANGELOG
/usr/X11R6/bin/*
