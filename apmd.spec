Summary:	Advanced Power Management (APM) utilities for notebooks.
Summary(pl):	Obs³uga zarz±dzania enerig± (APM) dla notebooków.
Name:		apmd
Version:	3.0
Release:	2
Epoch:		1
License:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source:		http://www.worldvisions.ca/~apenwarr/apmd/%{name}-%{version}.tar.gz
Source1:	apmd.init
URL:		http://www.worldvisions.ca/~apenwarr/apmd/
Requires:	procps
Prereq:		chkconfig
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}

%description
Advanced Power Management daemon and utilities allows you to watch your
notebook's power state and warn all users when the battery is low. It can
also handle some power state events automatically.

%description -l pl
Demon zadz±dzania energi± APM (Advanced Power Management) wraz z programami
pomocniczymi. Dziêki nim mo¿liwe jest monitorowanie stanu zasilania Twojego
notebooka i ostrzeganie wszystkich u¿ytkowników o koñcz±cej siê baterii,
jak równie¿ automatyczne reagowanie na zmiany.

%prep
%setup -q -n apmd

%build
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s APMD_PROXY_DIR=%{_sbindir}
make -C xbattery clean
make CCOPTIONS="$RPM_OPT_FLAGS" -C xbattery

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{bin,include,lib,sbin}
install -d $RPM_BUILD_ROOT%{_prefix}/X11R6/{bin,man/man1}
install -d $RPM_BUILD_ROOT%{_datadir}/man/{man1,man8}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d
install -d $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install apm 	$RPM_BUILD_ROOT%{_bindir}
install apmd 	$RPM_BUILD_ROOT%{_sbindir}
install apmsleep $RPM_BUILD_ROOT%{_bindir}
install tailf 	$RPM_BUILD_ROOT%{_bindir}
install on_ac_power $RPM_BUILD_ROOT%{_bindir}
install xapm 	$RPM_BUILD_ROOT%{_prefix}/X11R6/bin
install apmd_proxy $RPM_BUILD_ROOT%{_sbindir}
install apm.1 	$RPM_BUILD_ROOT%{_datadir}/man/man1/
install apmd.8 	$RPM_BUILD_ROOT%{_datadir}/man/man8/
install xapm.1 	$RPM_BUILD_ROOT%{_prefix}/X11R6/man/man1/xapm.1x
install tailf.1  $RPM_BUILD_ROOT%{_datadir}/man/man1/
install apmsleep.1 $RPM_BUILD_ROOT%{_datadir}/man/man1
install libapm.a $RPM_BUILD_ROOT%{_libdir}
install apm.h $RPM_BUILD_ROOT%{_includedir}
install $RPM_SOURCE_DIR/apmd.init $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/apmd
install -s xbattery/xbattery $RPM_BUILD_ROOT%{_prefix}/X11R6/bin
install xbattery/xbattery.man $RPM_BUILD_ROOT%{_prefix}/X11R6/man/man1/xbattery.1x

cat <<'EOF' >$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/apmd
APMD_OPTIONS="-p 10 -w 5 -W -P %{_sbindir}/apmd_proxy"
EOF

gzip -9nf $RPM_BUILD_ROOT%{_datadir}/man/man*/* \
	$RPM_BUILD_ROOT%{_prefix}/X11R6/man/man*/* \
	README README.transfer ChangeLog ANNOUNCE
 
%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add apmd
if [ -f /var/lock/subsys/apmd ]; then
	%{_sysconfdir}/rc.d/init.d/apmd restart 1>&2
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
%{_datadir}/man/man*/*
%{_prefix}/X11R6/man/man*/*
%attr(755,root,root) %{_prefix}/X11R6/bin/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_includedir}/*
%{_libdir}/*
%attr(754,root,root) %{_sysconfdir}/rc.d/init.d/apmd
%config %{_sysconfdir}/sysconfig/apmd
