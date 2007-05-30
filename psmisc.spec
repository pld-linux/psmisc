#
# Conditional build:
%bcond_without	selinux		# build without SELinux support
#
Summary:	Utilities for managing processes on your system
Summary(de):	Utilities zum Verwalten der Prozesse auf Ihrem System
Summary(es):	Más herramientas de tipo ps para el sistema de archivos /proc
Summary(fr):	Autres outils du type ps pour le système de fichiers /proc
Summary(ko):	½Ã½ºÅÛ¿¡¼­ ÇÁ·Î¼¼¼­¸¦ °ü¸®ÇÏ´Â µµ±¸
Summary(pl):	Narzêdzia do kontroli procesów
Summary(pt_BR):	Mais ferramentas do tipo ps para o sistema de arquivos /proc
Summary(ru):	õÔÉÌÉÔÙ ÒÁÂÏÔÙ Ó ÐÒÏÃÅÓÓÁÍÉ
Summary(tr):	/proc dosya sistemi için ps tipi araçlar
Summary(uk):	õÔÉÌ¦ÔÉ ÒÏÂÏÔÉ Ú ÐÒÏÃÅÓÁÍÉ
Name:		psmisc
Version:	22.3
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/psmisc/%{name}-%{version}.tar.gz
# Source0-md5:	0c44b995d068a221daf35d23e13db419
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	9add7665e440bbd6b0b4f9293ba8b86d
Patch0:		%{name}-AM_INTL.patch
URL:		http://psmisc.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-devel >= 0.14.1
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	ncurses-devel >= 5.0
Conflicts:	rc-scripts < 0.4.1.6-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin

%description
The psmisc package contains utilities for managing processes on your
system: pstree, killall and fuser. The pstree command displays a tree
structure of all of the running processes on your system. The killall
command sends a specified signal (SIGTERM if nothing is specified) to
processes identified by name. The fuser command identifies the PIDs of
processes that are using specified files or filesystems.

%description -l de
Das psmisc-Paket enthält Utilities zum Verwalten vom Prozessen auf
Ihrem System: pstree, killall und fuser. Der pstree-Befehl zeigt eine
Baumstruktur von allen laufenden Prozessen an. killall schickt
angegebenen Programmen ein Signal (SIGTERM, falls nichts anderes
angegeben wird). fuser identifiziert die PIDs (Prozess-IDs) von
Prozessen, die bestimmte Dateien oder Dateisysteme benutzen.

%description -l es
Este paquete contiene programas para enseñar un árbol de procesos,
saber que usuarios tienen archivo abierto y mandar señales a los
procesos por nombre.

%description -l fr
Ce paquetage contient les programmes pour afficher une arborescence de
processus, trouver quel utilisateur a un fichier ouvert et envoyer des
signaux aux processes par leurs noms.

%description -l pl
Ten pakiet zawiera programy umo¿liwiaj±ce wy¶wietlenie drzewa
procesów, znalezienie u¿ytkownika, który otworzy³ dany plik i wys³anie
sygna³u do procesu o zadanej nazwie.

%description -l pt_BR
Este pacote contém programas para mostrar uma árvore de processos,
saber quais usuários têm arquivo aberto e mandar sinais aos processos
por nome.

%description -l ru
÷ ÜÔÏÔ ÐÁËÅÔ ×ËÌÀÞÅÎÙ ÐÒÏÇÒÁÍÍÙ ÄÌÑ ÏÔÏÂÒÁÖÅÎÉÑ ÄÅÒÅ×Á ÐÒÏÃÅÓÓÏ×,
ÐÏÌÕÞÅÎÉÑ ÉÎÆÏÒÍÁÃÉÉ Ï ÔÏÍ, ËÅÍ ÏÔËÒÙÔ ÆÁÊÌ É ÄÌÑ ÐÏÓÙÌËÉ ÓÉÇÎÁÌÏ×
ÐÒÏÃÅÓÓÁÍ ÐÏ ÉÍÅÎÉ ÐÒÏÃÅÓÓÁ.

%description -l tr
Bu paket, süreçlerin aðaç yapýsýný göstermek, hangi kullanýcýlarýn
açýk dosyasý olduðunu bulmak ve süreçlere isimleri ile sinyal
göndermek için gerekli programlarý içerir.

%description -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÐÒÏÇÒÁÍÉ ÄÌÑ ×¦ÄÏÂÒÁÖÅÎÎÑ ÄÅÒÅ×Á ÐÒÏÃÅÓ¦×, ÐÏÓÉÌËÉ
ÓÉÇÎÁÌ¦× ÐÒÏÃÅÓÁÍ ÐÏ ¦ÍÅÎ¦ ÐÒÏÃÅÓÁ ÔÁ ÏÔÒÉÍÁÎÎÑ ¦ÎÆÏÒÍÁÃ¦§ ÐÒÏ ÔÅ, ÈÔÏ
×¦ÄËÒÉ× ÆÁÊÌ.

%prep
%setup -q
%patch0 -p0

%build
%{__gettextize}
%{__aclocal}
%{__autoconf} -I m4
%{__autoheader}
%{__automake}
CFLAGS="%{rpmcflags} -D_GNU_SOURCE -I/usr/include/ncurses"
%configure \
	%{?with_selinux:--enable-selinux}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
rm -f $RPM_BUILD_ROOT%{_mandir}/README.psmisc-non-english-man-pages

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS Chang* NEWS README
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
