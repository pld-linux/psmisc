Summary:	Utilities for managing processes on your system
Summary(de):	Utilities zum Verwalten der Prozesse auf Ihrem System
Summary(es):	MАs herramientas de tipo ps para el sistema de archivos /proc
Summary(fr):	Autres outils du type ps pour le systХme de fichiers /proc
Summary(ko):	╫ц╫╨еш©║╪╜ га╥н╪╪╪╜╦╕ ╟Э╦╝го╢б ╣╣╠╦
Summary(pl):	NarzЙdzia do kontroli procesСw
Summary(pt_BR):	Mais ferramentas do tipo ps para o sistema de arquivos /proc
Summary(ru):	Утилиты работы с процессами
Summary(tr):	/proc dosya sistemi iГin ps tipi araГlar
Summary(uk):	Утил╕ти роботи з процесами
Name:		psmisc
Version:	21.4
Release:	1
License:	distributable
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	8449269fdc8ae5d7d494df745e1180d3
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	9add7665e440bbd6b0b4f9293ba8b86d
Patch0:		%{name}-missing-nls.patch
Patch1:		%{name}-pl.po.patch
Patch2:		%{name}-tinfo.patch
Patch3:		%{name}-selinux.patch
URL:		http://psmisc.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libselinux-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin
%define		_sbindir	/sbin

%description
The psmisc package contains utilities for managing processes on your
system: pstree, killall and fuser. The pstree command displays a tree
structure of all of the running processes on your system. The killall
command sends a specified signal (SIGTERM if nothing is specified) to
processes identified by name. The fuser command identifies the PIDs of
processes that are using specified files or filesystems.

%description -l de
Das psmisc-Paket enthДlt Utilities zum Verwalten vom Prozessen auf
Ihrem System: pstree, killall und fuser. Der pstree-Befehl zeigt eine
Baumstruktur von allen laufenden Prozessen an. killall schickt
angegebenen Programmen ein Signal (SIGTERM, falls nichts anderes
angegeben wird). fuser identifiziert die PIDs (Prozess-IDs) von
Prozessen, die bestimmte Dateien oder Dateisysteme benutzen.

%description -l es
Este paquete contiene programas para enseЯar un Аrbol de procesos,
saber que usuarios tienen archivo abierto y mandar seЯales a los
procesos por nombre.

%description -l fr
Ce paquetage contient les programmes pour afficher une arborescence de
processus, trouver quel utilisateur a un fichier ouvert et envoyer des
signaux aux processes par leurs noms.

%description -l pl
Ten pakiet zawiera programy umo©liwiaj╠ce wy╤wietlienie drzewa
procesСw, znalezienie u©ytkownika, ktСry otworzyЁ dany plik i wysЁanie
sygnaЁu do procesu o zadanej nazwie.

%description -l pt_BR
Este pacote contИm programas para mostrar uma Аrvore de processos,
saber quais usuАrios tЙm arquivo aberto e mandar sinais aos processos
por nome.

%description -l ru
В этот пакет включены программы для отображения дерева процессов,
получения информации о том, кем открыт файл и для посылки сигналов
процессам по имени процесса.

%description -l tr
Bu paket, sЭreГlerin aПaГ yapЩsЩnЩ gЖstermek, hangi kullanЩcЩlarЩn
aГЩk dosyasЩ olduПunu bulmak ve sЭreГlere isimleri ile sinyal
gЖndermek iГin gerekli programlarЩ iГerir.

%description -l uk
Цей пакет м╕стить програми для в╕дображення дерева процес╕в, посилки
сигнал╕в процесам по ╕мен╕ процеса та отримання ╕нформац╕╖ про те, хто
в╕дкрив файл.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# allow *.gmo rebuilding
rm -f po/stamp-po

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
CFLAGS="%{rpmcflags} -D_GNU_SOURCE -I/usr/include/ncurses"
%configure \
	--enable-selinux
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mkdir $RPM_BUILD_ROOT/sbin
mv $RPM_BUILD_ROOT/bin/fuser $RPM_BUILD_ROOT/sbin

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS Chang* NEWS README
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(ko) %{_mandir}/ko/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pl) %{_mandir}/pl/man1/*
