Summary: Advanced Power Management (APM) BIOS utilities for laptops.
Name: apmd
Version: 3.0beta5
Release: 7
Source: ftp://ftp.debian.org/debian/dists/frozen/main/source/admin/%{name}_%{version}-1.tar.gz
Source1: apmd.init
Patch1: apmd-buildroot.patch
Copyright: GPL
Group: System Environment/Daemons
Requires: chkconfig >= 0.9
Prereq: chkconfig
BuildRoot: /var/tmp/apmd-root
ExclusiveArch: i386

%description
This is a Advanced Power Management daemon and utilities.
It can watch your notebook's battery and warn all users when the battery
is low.

Patches to Rik Faith's original version have been added for shutting down
the PCMCIA sockets before a suspend.

%prep
%setup -q -n apmd
%patch1 -p1 -b .buildroot

%build
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,include,lib,sbin,man/man1,man/man8,X11R6/bin,X11R6/man/man1}
make RPM_BUILD_ROOT=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
install -m 755 $RPM_SOURCE_DIR/apmd.init $RPM_BUILD_ROOT/etc/rc.d/init.d/apmd

cat <<'EOF' >$RPM_BUILD_ROOT/etc/sysconfig/apmd
APMD_OPTIONS="-p 10 -w 5 -W"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add apmd

%preun
if [ $1 = 0 ]; then
	/sbin/chkconfig --del apmd
fi

%files
%doc ANNOUNCE ChangeLog README README.transfer LSM
/usr/man/man1/*
/usr/man/man8/*
#/usr/X11R6/bin/*
#/usr/X11R6/man/man1/*
/usr/bin/*
/usr/sbin/*
/usr/include/*
/usr/lib/*
%config /etc/rc.d/init.d/apmd
%config /etc/sysconfig/apmd
