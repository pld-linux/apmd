Summary:	Advanced Power Management (APM) utilities for notebooks.
Summary(pl):	Obs³uga zarz±dzania enerig± (APM) dla notebooków.
Name: 		apmd
Version: 	3.0beta9
Release: 	1
Copyright:	GPL
Group: 		Utilities/System
Group(pl):	Narzêdzia/system
URL:		http://www.worldvisions.ca/~apenwarr/apmd
Source:		http://worldvisions.ca/~apenwarr/apmd/%{name}-%{version}.tar.gz
Source1: 	apmd.init
Requires:	procps
Prereq:		chkconfig
BuildRequires:	XFree86-devel
BuildRoot: 	/tmp/%{name}-%{version}
ExclusiveArch:  %{ix86}

%description
Advanced Power Management daemon and utilities allows you to watch your 
notebook's power state and warn all users when the battery is low. It can
also handle some power state events automatically.

%description -l pl
Demon zadz±dzania energi± APM (Advanced Power Management) wraz z programami
pomocniczymi. Dziêki nim mo¿liwe jest monitorowanie stanu zasilania Twojego
notebooka i ostrzeganie wszystkich u¿ytkowników o koñcz±cej siê baterii, jak
równie¿ automatyczne reagowanie na zmiany.

%prep
%setup -q -n apmd

%build
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s APMD_PROXY_DIR=/usr/sbin
make -C xbattery clean
make CCOPTIONS="$RPM_OPT_FLAGS" -C xbattery

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,include,lib,sbin}
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1}
mkdir -p $RPM_BUILD_ROOT/usr/share/man/{man1,man8}
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
install apm 	$RPM_BUILD_ROOT/usr/bin
install apmd 	$RPM_BUILD_ROOT/usr/sbin
install apmsleep $RPM_BUILD_ROOT/usr/bin
install tailf 	$RPM_BUILD_ROOT/usr/bin
install on_ac_power $RPM_BUILD_ROOT/usr/bin
install xapm 	$RPM_BUILD_ROOT/usr/X11R6/bin
install apmd_proxy $RPM_BUILD_ROOT/usr/sbin
install apm.1 	$RPM_BUILD_ROOT/usr/share/man/man1/
install apmd.8 	$RPM_BUILD_ROOT/usr/share/man/man8/
install xapm.1 	$RPM_BUILD_ROOT/usr/X11R6/man/man1/xapm.1x
install tailf.1  $RPM_BUILD_ROOT/usr/share/man/man1/
install apmsleep.1 $RPM_BUILD_ROOT/usr/share/man/man1
install libapm.a $RPM_BUILD_ROOT/usr/lib
install apm.h $RPM_BUILD_ROOT/usr/include
install $RPM_SOURCE_DIR/apmd.init $RPM_BUILD_ROOT/etc/rc.d/init.d/apmd
install -s xbattery/xbattery $RPM_BUILD_ROOT/usr/X11R6/bin
install xbattery/xbattery.man $RPM_BUILD_ROOT/usr/X11R6/man/man1/xbattery.1x

cat <<'EOF' >$RPM_BUILD_ROOT/etc/sysconfig/apmd
APMD_OPTIONS="-p 10 -w 5 -W -P /usr/sbin/apmd_proxy"
EOF

gzip -9nf $RPM_BUILD_ROOT/usr/share/man/man*/* \
	$RPM_BUILD_ROOT/usr/X11R6/man/man*/* \
	README README.transfer ChangeLog ANNOUNCE
 
%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add apmd

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del apmd
fi

%files
%defattr(644,root,root,755)
%doc ANNOUNCE.gz ChangeLog.gz README.gz README.transfer.gz
/usr/share/man/man*/*
/usr/X11R6/man/man*/*
%attr(755,root,root) /usr/X11R6/bin/*
%attr(755,root,root) /usr/bin/*
%attr(755,root,root) /usr/sbin/*
/usr/include/*
/usr/lib/*
%attr(754,root,root) /etc/rc.d/init.d/apmd
%config /etc/sysconfig/apmd
