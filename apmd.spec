Summary:	Advanced Power Management (APM) utilities for notebooks
Summary(cs):	Nástroje pro APM (Advanced Power Management) BIOS na laptopech
Summary(da):	Avanceret strømstyring (APM) bios værktøjer for bærbare
Summary(de):	Advanced Power Management (APM) BIOS-Dienstprogramme für Laptops
Summary(es):	Utilitarios para APM (Gestión Avanzado de Energía) BIOS para portátiles
Summary(fr):	Utilitaires BIOS de gestion avancée de l'énergie (APM) pour les ordinateurs portables
Summary(id):	Advanced Power Management (APM) BIOS utilities untuk laptop
Summary(is):	Tól sem stjórnar orkunotkun fartölvu (Advanced Power Management)
Summary(it):	Utility APM (Advanced Power Management) BIOS per laptop
Summary(ja):	¥é¥Ã¥×¥È¥Ã¥×ÍÑ¤Î APM (Advanced Power Management) ¥æ¡¼¥Æ¥£¥ê¥Æ¥£
Summary(no):	Advanced Power Management (APM) BIOS verktøy for bærbare
Summary(pl):	Obs³uga zarz±dzania enerig± (APM) dla notebooków
Summary(pt):	Utilitários Advanced Power Management (APM) para portáteis
Summary(pt_BR):	Utilitários para APM (Gerenciamento Avancado de Energia)
Summary(ru):	õÔÉÌÉÔÙ ÄÌÑ Advanced Power Management (APM) BIOS × ÌÁĞÔÏĞÁÈ
Summary(sk):	Pomôcky pre Advanced Power Management (APM) BIOS laptopov
Summary(sl):	Pripomoèki za prenosnike z Advanced Power Management (APM)
Summary(sv):	Verktyg för styrning av spänningshantering (APM) i bärbara datorer
Summary(uk):	õÔÉÌ¦ÔÉ ÄÌÑ Advanced Power Management (APM) BIOS × ÌÁĞÔÏĞÁÈ
Summary(zh_CN):	ÓÃÓÚÏ¥ÉÏĞÍ¼ÆËã»úµÄ¸ß¼¶µçÔ´¹ÜÀí (APM) BIOS ÊµÓÃ³ÌĞò¡£
Name:		apmd
Version:	3.0.2
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://www.worldvisions.ca/~apenwarr/apmd/%{name}-%{version}.tar.gz
Source1:	%{name}.init
Patch0:		%{name}-security.patch
Patch1:		%{name}-spinlock.patch
URL:		http://www.worldvisions.ca/~apenwarr/apmd/
BuildRequires:	XFree86-devel
Prereq:		/sbin/chkconfig
Obsoletes:	acpid
Requires:	procps
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86} ppc

%description
Advanced Power Management daemon and utilities allows you to watch
your notebook's power state and warn all users when the battery is
low. It can also handle some power state events automatically.

%description -l cs
APMD je sada programù pro ovládání démona pro pokroèilou správu
energie (Advanced Power Management - APM) vèetnì pomocnıch programù,
které jsou k dispozici na vìt¹inì moderních pøenosnıch poèítaèù. APMD
umí sledovat stav baterie notebooku a varovat u¾ivatele pøi poklesu
jejího napìtí. APMD je také schopné vypnout PCMCIA sokety pøed uspáním
poèítaèe.

%description -l da
APMD er et sæt programmer for kontrol af Advanced Power Management
(APM) dæmonen og værktøjer som findes i de fleste moderne bærbare
datamaskiner. APMD kan overvåge batteriet på din bærbare og advare dig
når batteriniveauet er lavt og/eller lukke ned for PCMCIA kortene før
maskinen går i dvale.

%description -l de
APMD enthält Programme zur Steuerung des Advanced Power Management
(APM)-Daemons und der Dienstprogramme, die in den meisten modernen
Laptops verwendet werden. APMD kann den Akku von Notebooks überwachen
und Benutzer über eine zu geringe Ladung informieren. APMD kann
außerdem die PCMCIA-Schnittstellen herunterfahren, bevor der Computer
in den Suspend-Modus schaltet.

%description -l es
Utilitarios y servidor para gestión avanzada de energía (APM).
Verifica la batería de tu notebook y avisa a los usuarios cuando la
carga es poca. Fue adicionado un patch no oficial para parar los
enchufes PCMCIA antes de una suspensión de energía.

%description -l fr
APMD est un ensemble de programmes permettant de contrôler le démon
APM (Advanced Power Management) et les utilitaires installés sur la
plupart des ordinateurs portables récents. APMD peut surveiller la
batterie de votre portable, vous avertir lorsqu'elle est faible ou
arrêter les supports PCMCIA avant l'arrêt de votre ordinateur.

%description -l id
APMD adalah sekumpulan program yang melakukan kontrol terhadap
Advanced Power Management, deamon dan utility yang dapat ditemukan
hampir di semua laptop moderen. APMD dapat mengawasi penggunaan
baterai pada notebook, dan memberikan peringatan kepada pengguna bila
tenaga bateri rendah. APMD juga mampu melakukan shut down socket
PCMCIA sebelum suspend.

%description -l is
APMD er safn forrita til ağ stjórna APM ( Advanced Power Management -
stıring rafnotkunar ) stıringum sem er ağ finna í flestum fartölvum.
APMD getur fylgst meğ ástandi rafhlöğunnar og látiğ notendur vita
şegar rafmagn fer ağ şrjóta. APMD getur einnig slökkt á PCMCIA
şjónustum áğur en slökkt er á vélinni.

%description -l it
APDM è un set di programmi per il controllo del demone e delle utility
di Advanced Power Management (APM) presenti nella maggior parte dei
laptop moderni. APDM consente di controllare la batteria del portatile
e di avvisare gli utenti quando è quasi scarica e/o di chiudere gli
attacchi del PCMCIA prima di un'interruzione.

%description -l ja
APMD ¤ÏºÇ¶á¤Î¥é¥Ã¥×¥È¥Ã¥×¥³¥ó¥Ô¥å¡¼¥¿¤ÇÍÑ¤¤¤é¤ì¤ë Advanced Power
Management (APM) ¥Ç¡¼¥â¥ó¤È¥æ¡¼¥Æ¥£¥ê¥Æ¥£¤òÀ©¸æ¤¹¤ë¤¿¤á¤Î¥×¥í¥°¥é¥à
¥»¥Ã¥È¤Ç¤¹¡£ APMD ¤Ï¥Î¡¼¥È¥Ö¥Ã¥¯¤Î¥Ğ¥Ã¥Æ¥ê¤ò´Æ»ë¤·¡¢ÍÆÎÌ¤¬¾¯¤Ê¤¯
¤Ê¤ë¤È·Ù¹ğ¤·¤¿¤ê¡¢¥µ¥¹¥Ú¥ó¥É¥â¡¼¥É¤ËÀÚ¤êÂØ¤ï¤ëÁ°¤Ë PCMCIA ¤ò
¥·¥ã¥Ã¥È¥À¥¦¥ó¤·¤¿¤ê¤·¤Ş¤¹¡£

%description -l no
APMD er et sett programmer for kontroll av Advanced Power Management
(APM) daemonen og verktøy som finnes i de fleste moderne bærbare
datamaskiner. APMD kan overvåke batteriet på din bærbare og advare deg
brukere når batterinivået er lavt og/eller stenge ned PCMCIA
kontaktene før maskinen går i dvale.

%description -l pl
Demon zadz±dzania energi± APM (Advanced Power Management) wraz z
programami pomocniczymi. Dziêki nim mo¿liwe jest monitorowanie stanu
zasilania Twojego notebooka i ostrzeganie wszystkich u¿ytkowników o
koñcz±cej siê baterii, jak równie¿ automatyczne reagowanie na zmiany.

%description -l pt
O APMD é um conjunto de programas e utilitários para controlar o APM
(Advanced Power Management ou Gestão de Energia Avançada) existente na
maioria dos computadores portáteis modernos. O APMD pode vigiar a
bateria do seu portátil e avisá-lo quando a bateria está em baixo e/ou
desligar os 'sockets' PCMCIA antes de suspender.

%description -l pt_BR
Utilitários e servidor para gerenciamento avançado de energia (APM).
Ele verifica a bateria de seu notebook e avisa aos usuários que ele
está com pouca carga. Foi adicionado um patch nao oficial para parar
os soquetes PCMCIA antes de uma suspensao de energia.

%description -l ru
APMD - ÜÔÏ ÎÁÂÏÒ ĞÒÏÇÒÁÍÍ ÄÌÑ ÕĞÒÁ×ÌÅÎÉÑ ÄÅÍÏÎÏÍ APM (Advanced Power
Management) É ÕÔÉÌÉÔÁÍÉ, ÎÁÈÏÄÑİÉÍÉÓÑ ÎÁ ÂÏÌØÛÉÎÓÔ×Å ÓÏ×ÒÅÍÅÎÎÙÈ
ĞÏÒÔÁÔÉ×ÎÙÈ ËÏÍĞØÀÔÅÒÏ×. APMD ÍÏÖÅÔ ÓÌÅÄÉÔØ ÚÁ ÓÏÓÔÏÑÎÉÅÍ ÂÁÔÁÒÅÊ
ĞÏÒÔÁÔÉ×ÎÏÇÏ ËÏÍĞØÀÔÅÒÁ É ĞÒÅÄÕĞÒÅÖÄÁÔØ ĞÏÌØÚÏ×ÁÔÅÌÑ ÏÂ ÉÈ ÒÁÚÒÑÄËÅ.
ëÒÏÍÅ ÔÏÇÏ, APMD ÍÏÖÅÔ ÏÔËÌÀŞÉÔØ ÒÁÚØÅÍÙ PCMCIA ĞÅÒÅÄ ĞÅÒÅÈÏÄÏÍ ×
ÒÅÖÉÍ ĞÏÎÉÖÅÎÎÏÇÏ ÜÎÅÒÇÏĞÏÔÒÅÂÌÅÎÉÑ.

%description -l sk
APMD je sada programov pre riadenie systému APM (Advanced Power
Management), nachádzajúceho sa vo väè¹ine modernıch prenosnıch
poèítaèov. APMD je schopnı kontrolova» batériu vá¹ho notebooku a
varova» pou¾ívateµov, pokiaµ je skoro vybitá. Mô¾e tie¾ odpája» PCMCIA
sokety pred \"uspaním\"

%description -l sv
APMD är program för att styra demon och verktyg för strömhantering
(Advanced Power Management, APM) som finns i de flesta moderna bärbara
datorer. APMD kan bevaka din bärbaras batteri och varna dig när
batteriet sinar och/eller stänga av PCMCIA-uttag före suspendering.

%description -l uk
APMD - ÃÅ ÎÁÂ¦Ò ĞÒÏÇÒÁÍ ÄÌÑ ËÅÒÕ×ÁÎÎÑ ÄÅÍÏÎÏÍ Advanced Power
Management. APMD ÍÏÖÅ ÓÌ¦ÄËÕ×ÁÔÉ ÚÁ ÂÁÔÁÒÅÑÍÉ ÷ÁÛÏÇÏ ÌÁĞÔÏĞÁ ÔÁ
ĞÏĞÅÒÅÄÖÕ×ÁÔÉ ËÏÒÉÓÔÕ×ÁŞ¦× ĞÒÉ ÒÏÚÒÑÄ¦ ÂÁÔÁÒÅÊ.

%description -l zh_CN
APMD
ÊÇÒ»×é³ÌĞò£¬ÓÃÓÚ¿ØÖÆ×îĞÂÏ¥ÉÏĞÍ¼ÆËã»úÉÏµÄ¸ß¼¶µçÔ´¹ÜÀíºóÌ¨³ÌĞòºÍÊµÓÃ³ÌĞò¡£
APMD
¿ÉÒÔ¼à¿Ø±Ê¼Ç±¾¼ÆËã»úµÄµç³Ø×´Ì¬£¬²¢ÇÒÔÚµç³ØµçÁ¿²»×ãÊ±ÏòÓÃ»§·¢³ö¾¯¸æ¡£
APMD »¹¿ÉÒÔÔÚÔİ¹ÒÇ°¹Ø±Õ PCMCIA ²å²Û¡£

%package devel
Summary:	Header files and static library for developing APM applications
Summary(es):	Archivos de inclusión y bibliotecas para apmd en versión estática
Summary(pl):	Pliki nag³ówkowe i biblioteka statyczna do tworzenia aplikacji korzystaj±cych z APM
Summary(pt_BR):	Arquivos de inclusão e bibliotecas para o apmd em versão estática
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files necessary for developing APM applications.

%description devel -l es
Archivos de inclusión y bibliotecas para apmd en versión estática

%description devel -l pl
Pliki nag³ówkowe niezbêdne do tworzenia aplikacji korzystaj±cych z
APM.

%description devel -l pt_BR
Arquivos de inclusão e bibliotecas para o apmd em versão estática

%package -n xapm
Summary:	XFree86 APM monitoring and management tool
Summary(pl):	Narzêdzie do monitorowania i zarz±dzania APMem pod XFree86
Group:		X11/Applications
Requires:	XFree86

%description -n xapm
xapm is an XFree86 version of console APM client - "apm".

%description -n xapm -l pl
xapm jest wersj± konsolowego klienta APM - "apm", przenaczon± dla
XFree86.

%prep
%setup -q -n apmd
%patch0 -p1

%ifarch ppc
%patch1 -p1 
%endif 

%build
%{__make} CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" APMD_PROXY_DIR=%{_sbindir}
%{__make} -C xbattery clean
%{__make} CCOPTIONS="%{rpmcflags}" LOCAL_LDFLAGS="%{rpmldflags}" -C xbattery

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir},%{_sbindir}} \
	$RPM_BUILD_ROOT%{_prefix}/X11R6/{bin,man/man1} \
	$RPM_BUILD_ROOT{%{_mandir}/man{1,8},%{_sysconfdir}/{rc.d/init.d,sysconfig}}

install apm apmsleep on_ac_power $RPM_BUILD_ROOT%{_bindir}
install apmd apmd_proxy $RPM_BUILD_ROOT%{_sbindir}

install xapm $RPM_BUILD_ROOT%{_prefix}/X11R6/bin

install apm.1 apmsleep.1 $RPM_BUILD_ROOT%{_mandir}/man1/
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

gzip -9nf README README.transfer ChangeLog ANNOUNCE

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add apmd
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
%doc *.gz
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
