Summary:	Advanced Power Management (APM) utilities for notebooks
Summary(pl):	Obs³uga zarz±dzania enerig± (APM) dla notebooków
Name:		apmd
Version:	3.0
Release:	5
License:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	http://www.worldvisions.ca/~apenwarr/apmd/%{name}-%{version}.tar.gz
Source1:	apmd.init
URL:		http://www.worldvisions.ca/~apenwarr/apmd/
Requires:	procps
Prereq:		chkconfig
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}

%description
Advanced Power Management daemon and utilities allows you to watch
your notebook's power state and warn all users when the battery is
low. It can also handle some power state events automatically.

%description -l pl
Demon zadz±dzania energi± APM (Advanced Power Management) wraz z
programami pomocniczymi. Dziêki nim mo¿liwe jest monitorowanie stanu
zasilania Twojego notebooka i ostrzeganie wszystkich u¿ytkowników o
koñcz±cej siê baterii, jak równie¿ automatyczne reagowanie na zmiany.

%package devel
Summary:	Header files for developing APM applications
Summary(pl):	Pliki nag³ówkowe do tworzenia aplikacji korzystaj±cych z APM
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Group(fr):	Development/Librairies
Requires:	%{name} = %{version}

%description devel
Header files necessary for developing APM applications

%description devel -l pl
Pliki nag³ówkowe niezbêdne do tworzenia aplikacji korzystaj±cych z APM

%package -n xapm
Summary:	XFree86 APM monitoring and management tool
Summary(pl):	Narzêdzie do monitorowania i zarz±dzania APMem pod XFree86
Group:		X11/Utilities/System
Group(pl):	X11/Narzêdzia/System
Requires:	XFree86

%description -n xapm
xapm is an XFree86 version of console APM client - "apm".

%description -n xapm -l pl
xapm jest wersj± konsolowego klienta APM - "apm", przenaczon± dla
XFree86

%prep
%setup -q -n apmd

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s APMD_PROXY_DIR=%{_sbindir}
%{__make} -C xbattery clean
%{__make} CCOPTIONS="$RPM_OPT_FLAGS" LOCAL_LDFLAGS="-s" -C xbattery

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir},%{_sbindir}} \
	$RPM_BUILD_ROOT%{_prefix}/X11R6/{bin,man/man1} \
	$RPM_BUILD_ROOT{%{_mandir}/man{1,8},/etc/{rc.d/init.d,sysconfig}}

install apm apmsleep tailf on_ac_power $RPM_BUILD_ROOT%{_bindir}
install apmd apmd_proxy $RPM_BUILD_ROOT%{_sbindir}

install xapm $RPM_BUILD_ROOT%{_prefix}/X11R6/bin

install apm.1 apmsleep.1 tailf.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install apmd.8 $RPM_BUILD_ROOT%{_mandir}/man8/
install xapm.1 $RPM_BUILD_ROOT%{_prefix}/X11R6/man/man1/xapm.1x
install xbattery/xbattery.man $RPM_BUILD_ROOT%{_prefix}/X11R6/man/man1/xbattery.1x

install libapm.a $RPM_BUILD_ROOT%{_libdir}
install apm.h $RPM_BUILD_ROOT%{_includedir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/apmd
install xbattery/xbattery $RPM_BUILD_ROOT%{_prefix}/X11R6/bin

cat << EOF > $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/apmd
APMD_OPTIONS="-p 10 -w 5 -W -P %{_sbindir}/apmd_proxy"
EOF

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	$RPM_BUILD_ROOT%{_prefix}/X11R6/man/man*/* \
	README README.transfer ChangeLog ANNOUNCE
 
%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig apmd reset
if [ -f /var/lock/subsys/apmd ]; then
	/etc/rc.d/init.d/apmd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/apmd start\" to start apmd daemon."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/apmd ]; then
		/etc/rc.d/init.d/apmd stop 1>&2
	fi
	/sbin/chkconfig --del apmd
fi

%files
%defattr(644,root,root,755)
%doc ANNOUNCE.gz ChangeLog.gz README.gz README.transfer.gz
%{_mandir}/man*/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(754,root,root) /etc/rc.d/init.d/apmd
%config(noreplace) /etc/sysconfig/apmd

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.a

%files -n xapm
%defattr(644,root,root,755)
%{_prefix}/X11R6/man/man*/*
%attr(755,root,root) %{_prefix}/X11R6/bin/*
