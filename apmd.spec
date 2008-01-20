Summary:	Advanced Power Management (APM) utilities for notebooks
Summary(cs.UTF-8):	Nástroje pro APM (Advanced Power Management) BIOS na laptopech
Summary(da.UTF-8):	Avanceret strømstyring (APM) bios værktøjer for bærbare
Summary(de.UTF-8):	Advanced Power Management (APM) BIOS-Dienstprogramme für Laptops
Summary(es.UTF-8):	Utilitarios para APM (Gestión Avanzado de Energía) BIOS para portátiles
Summary(fr.UTF-8):	Utilitaires BIOS de gestion avancée de l'énergie (APM) pour les ordinateurs portables
Summary(id.UTF-8):	Advanced Power Management (APM) BIOS utilities untuk laptop
Summary(is.UTF-8):	Tól sem stjórnar orkunotkun fartölvu (Advanced Power Management)
Summary(it.UTF-8):	Utility APM (Advanced Power Management) BIOS per laptop
Summary(ja.UTF-8):	ラップトップ用の APM (Advanced Power Management) ユーティリティ
Summary(nb.UTF-8):	Advanced Power Management (APM) BIOS verktøy for bærbare
Summary(pl.UTF-8):	Obsługa zarządzania enerigą (APM) dla notebooków
Summary(pt.UTF-8):	Utilitários Advanced Power Management (APM) para portáteis
Summary(pt_BR.UTF-8):	Utilitários para APM (Gerenciamento Avancado de Energia)
Summary(ru.UTF-8):	Утилиты для Advanced Power Management (APM) BIOS в лаптопах
Summary(sk.UTF-8):	Pomôcky pre Advanced Power Management (APM) BIOS laptopov
Summary(sl.UTF-8):	Pripomočki za prenosnike z Advanced Power Management (APM)
Summary(sv.UTF-8):	Verktyg för styrning av spänningshantering (APM) i bärbara datorer
Summary(uk.UTF-8):	Утиліти для Advanced Power Management (APM) BIOS в лаптопах
Summary(zh_CN.UTF-8):	用于膝上型计算机的高级电源管理 (APM) BIOS 实用程序。
Name:		apmd
Version:	3.2.2
Release:	5
Epoch:		1
License:	GPL v2+
Group:		Applications/System
Source0:	ftp://ftp.debian.org/debian/pool/main/a/apmd/%{name}_%{version}.orig.tar.gz
# Source0-md5:	b1e6309e8331e0f4e6efd311c2d97fa8
Source1:	%{name}.init
Patch0:		%{name}-libtool.patch
URL:		http://www.worldvisions.ca/~apenwarr/apmd/
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXaw-devel
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	procps
Requires:	rc-scripts
Conflicts:	acpid
Obsoletes:	poweracpid
# APM is specific to 32-bit x86, but Linux provides emulation for some archs:
# arm, mips (AU1xx0-based), ppc (PMAC, 32-bit only), sh (HP6XX only)
ExclusiveArch:	%{ix86} arm mips ppc sh
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Advanced Power Management daemon and utilities allows you to watch
your notebook's power state and warn all users when the battery is
low. It can also handle some power state events automatically.

%description -l cs.UTF-8
APMD je sada programů pro ovládání démona pro pokročilou správu
energie (Advanced Power Management - APM) včetně pomocných programů,
které jsou k dispozici na většině moderních přenosných počítačů. APMD
umí sledovat stav baterie notebooku a varovat uživatele při poklesu
jejího napětí. APMD je také schopné vypnout PCMCIA sokety před uspáním
počítače.

%description -l da.UTF-8
APMD er et sæt programmer for kontrol af Advanced Power Management
(APM) dæmonen og værktøjer som findes i de fleste moderne bærbare
datamaskiner. APMD kan overvåge batteriet på din bærbare og advare dig
når batteriniveauet er lavt og/eller lukke ned for PCMCIA kortene før
maskinen går i dvale.

%description -l de.UTF-8
APMD enthält Programme zur Steuerung des Advanced Power Management
(APM)-Daemons und der Dienstprogramme, die in den meisten modernen
Laptops verwendet werden. APMD kann den Akku von Notebooks überwachen
und Benutzer über eine zu geringe Ladung informieren. APMD kann
außerdem die PCMCIA-Schnittstellen herunterfahren, bevor der Computer
in den Suspend-Modus schaltet.

%description -l es.UTF-8
Utilitarios y servidor para gestión avanzada de energía (APM).
Verifica la batería de tu notebook y avisa a los usuarios cuando la
carga es poca.

%description -l fr.UTF-8
APMD est un ensemble de programmes permettant de contrôler le démon
APM (Advanced Power Management) et les utilitaires installés sur la
plupart des ordinateurs portables récents. APMD peut surveiller la
batterie de votre portable, vous avertir lorsqu'elle est faible ou
arrêter les supports PCMCIA avant l'arrêt de votre ordinateur.

%description -l id.UTF-8
APMD adalah sekumpulan program yang melakukan kontrol terhadap
Advanced Power Management, deamon dan utility yang dapat ditemukan
hampir di semua laptop moderen. APMD dapat mengawasi penggunaan
baterai pada notebook, dan memberikan peringatan kepada pengguna bila
tenaga bateri rendah. APMD juga mampu melakukan shut down socket
PCMCIA sebelum suspend.

%description -l is.UTF-8
APMD er safn forrita til að stjórna APM ( Advanced Power Management -
stýring rafnotkunar ) stýringum sem er að finna í flestum fartölvum.
APMD getur fylgst með ástandi rafhlöðunnar og látið notendur vita
þegar rafmagn fer að þrjóta. APMD getur einnig slökkt á PCMCIA
þjónustum áður en slökkt er á vélinni.

%description -l it.UTF-8
APDM è un set di programmi per il controllo del demone e delle utility
di Advanced Power Management (APM) presenti nella maggior parte dei
laptop moderni. APDM consente di controllare la batteria del portatile
e di avvisare gli utenti quando è quasi scarica e/o di chiudere gli
attacchi del PCMCIA prima di un'interruzione.

%description -l ja.UTF-8
APMD は最近のラップトップコンピュータで用いられる Advanced Power
Management (APM) デーモンとユーティリティを制御するためのプログラム
セットです。 APMD はノートブックのバッテリを監視し、容量が少なく
なると警告したり、サスペンドモードに切り替わる前に PCMCIA を
シャットダウンしたりします。

%description -l nb.UTF-8
APMD er et sett programmer for kontroll av Advanced Power Management
(APM) daemonen og verktøy som finnes i de fleste moderne bærbare
datamaskiner. APMD kan overvåke batteriet på din bærbare og advare deg
brukere når batterinivået er lavt og/eller stenge ned PCMCIA
kontaktene før maskinen går i dvale.

%description -l pl.UTF-8
Demon zarządzania energią APM (Advanced Power Management) wraz z
programami pomocniczymi. Dzięki nim możliwe jest monitorowanie stanu
zasilania Twojego notebooka i ostrzeganie wszystkich użytkowników o
kończącej się baterii, jak również automatyczne reagowanie na zmiany.

%description -l pt.UTF-8
O APMD é um conjunto de programas e utilitários para controlar o APM
(Advanced Power Management ou Gestão de Energia Avançada) existente na
maioria dos computadores portáteis modernos. O APMD pode vigiar a
bateria do seu portátil e avisá-lo quando a bateria está em baixo e/ou
desligar os 'sockets' PCMCIA antes de suspender.

%description -l pt_BR.UTF-8
Utilitários e servidor para gerenciamento avançado de energia (APM).
Ele verifica a bateria de seu notebook e avisa aos usuários que ele
está com pouca carga. Foi adicionado um patch nao oficial para parar
os soquetes PCMCIA antes de uma suspensao de energia.

%description -l ru.UTF-8
APMD - это набор программ для управления демоном APM (Advanced Power
Management) и утилитами, находящимися на большинстве современных
портативных компьютеров. APMD может следить за состоянием батарей
портативного компьютера и предупреждать пользователя об их разрядке.
Кроме того, APMD может отключить разьемы PCMCIA перед переходом в
режим пониженного энергопотребления.

%description -l sk.UTF-8
APMD je sada programov pre riadenie systému APM (Advanced Power
Management), nachádzajúceho sa vo väčšine moderných prenosných
počítačov. APMD je schopný kontrolovať batériu vášho notebooku a
varovať používateľov, pokiaľ je skoro vybitá. Môže tiež odpájať PCMCIA
sokety pred \"uspaním\"

%description -l sv.UTF-8
APMD är program för att styra demon och verktyg för strömhantering
(Advanced Power Management, APM) som finns i de flesta moderna bärbara
datorer. APMD kan bevaka din bärbaras batteri och varna dig när
batteriet sinar och/eller stänga av PCMCIA-uttag före suspendering.

%description -l uk.UTF-8
APMD - це набір програм для керування демоном Advanced Power
Management. APMD може слідкувати за батареями Вашого лаптопа та
попереджувати користувачів при розряді батарей.

%description -l zh_CN.UTF-8
APMD
是一组程序，用于控制最新膝上型计算机上的高级电源管理后台程序和实用程序。
APMD
可以监控笔记本计算机的电池状态，并且在电池电量不足时向用户发出警告。
APMD 还可以在暂挂前关闭 PCMCIA 插槽。

%package libs
Summary:	libapm library
Summary(pl.UTF-8):	Biblioteka libapm
License:	LGPL v2+
Group:		Libraries

%description libs
libapm library.

%description libs -l pl.UTF-8
Biblioteka libapm.

%package devel
Summary:	Header files and static library for developing APM applications
Summary(es.UTF-8):	Archivos de inclusión y bibliotecas para apmd en versión estática
Summary(pl.UTF-8):	Pliki nagłówkowe i biblioteka statyczna do tworzenia aplikacji korzystających z APM
Summary(pt_BR.UTF-8):	Arquivos de inclusão e bibliotecas para o apmd em versão estática
License:	LGPL v2+
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
Header files necessary for developing APM applications.

%description devel -l es.UTF-8
Archivos de inclusión y bibliotecas para apmd en versión estática

%description devel -l pl.UTF-8
Pliki nagłówkowe niezbędne do tworzenia aplikacji korzystających z
APM.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão e bibliotecas para o apmd em versão estática

%package static
Summary:	Static libapm library
Summary(pl.UTF-8):	Statyczna biblioteka libapm
License:	LGPL v2+
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libapm library.

%description static -l pl.UTF-8
Statyczna biblioteka libapm.

%package -n xapm
Summary:	XFree86 APM monitoring and management tool
Summary(pl.UTF-8):	Narzędzie do monitorowania i zarządzania APMem pod XFree86
Group:		X11/Applications
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description -n xapm
xapm is an XFree86 version of console APM client - "apm".

%description -n xapm -l pl.UTF-8
xapm jest wersją konsolowego klienta APM - "apm", przenaczoną dla
XFree86.

%prep
%setup -q -n %{name}-%{version}.orig
%patch0 -p1

sed -i -e 's#-I/usr/src/linux.*/include##g' Makefile
sed -i -e 's#\.\./libapm\.a#-L../.libs -lapm#' xbattery/Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	APMD_PROXY_DIR=%{_sbindir}

%{__make} -C xbattery clean

%{__make} -C xbattery \
	CC="%{__cc}" \
	CCOPTIONS="%{rpmcflags}" \
	LOCAL_LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir},%{_sbindir}} \
	$RPM_BUILD_ROOT{%{_mandir}/{man{1,8},fr/man1},/etc/{rc.d/init.d,sysconfig}} \
	$RPM_BUILD_ROOT%{_sysconfdir}/apm

cd .libs
install apm xapm apmsleep ../on_ac_power ../xbattery/xbattery $RPM_BUILD_ROOT%{_bindir}
install apmd $RPM_BUILD_ROOT%{_sbindir}
cd ..

install apmd_proxy $RPM_BUILD_ROOT%{_sysconfdir}/apm
install apm.1 apmsleep.1 on_ac_power.1 xapm.1 $RPM_BUILD_ROOT%{_mandir}/man1
install apmsleep.fr.1 $RPM_BUILD_ROOT%{_mandir}/fr/man1/apmsleep.1
install *.8 $RPM_BUILD_ROOT%{_mandir}/man8
install xbattery/xbattery.man $RPM_BUILD_ROOT%{_mandir}/man1/xbattery.1

libtool --mode=install install libapm.la $RPM_BUILD_ROOT%{_libdir}/libapm.la

install apm.h $RPM_BUILD_ROOT%{_includedir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/apmd

cat << EOF > $RPM_BUILD_ROOT/etc/sysconfig/apmd
APMD_OPTIONS="-p 10 -w 5 -W -P %{_sysconfdir}/apm/apmd_proxy"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add apmd
%service apmd restart "apmd daemon"

%preun
if [ "$1" = "0" ]; then
	%service apmd stop
	/sbin/chkconfig --del apmd
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LSM README
%attr(755,root,root) %{_bindir}/apm
%attr(755,root,root) %{_bindir}/apmsleep
%attr(755,root,root) %{_bindir}/on_ac_power
%attr(755,root,root) %{_sbindir}/apmd
%attr(754,root,root) /etc/rc.d/init.d/apmd
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/apmd
%dir %{_sysconfdir}/apm
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apm/apmd_proxy
%{_mandir}/man1/apm.1*
%{_mandir}/man1/apmsleep.1*
%{_mandir}/man1/on_ac_power.1*
%{_mandir}/man8/apmd.8*
%lang(fr) %{_mandir}/fr/man1/apmsleep.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libapm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libapm.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libapm.so
%{_libdir}/libapm.la
%{_includedir}/apm.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libapm.a

%files -n xapm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xapm
%attr(755,root,root) %{_bindir}/xbattery
%{_mandir}/man1/xapm.1*
%{_mandir}/man1/xbattery.1*
