Summary:	Utilities for managing processes on your system
Summary(de):	Utilities zum Verwalten der Prozesse auf Ihrem System
Summary(es):	Más herramientas de tipo ps para el sistema de archivos /proc
Summary(fr):	Autres outils du type ps pour le système de fichiers /proc
Summary(pl):	Narzêdzia do kontroli procesów
Summary(pt_BR):	Mais ferramentas do tipo ps para o sistema de arquivos /proc
Summary(tr):	/proc dosya sistemi için ps tipi araçlar
Name:		psmisc
Version:	20.2
Release:	3
License:	Distributable
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-make.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel >= 5.0
URL:		http://psmisc.sourceforge.net/
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
Ten pakiet zawiera programy umo¿liwiaj±ce wy¶wietlienie drzewa
procesów, znalezienie u¿ytkownika, który otworzy³ dany plik i wys³anie
sygna³u do procesu o zadanej nazwie.

%description -l pt_BR
Este pacote contém programas para mostrar uma árvore de processos,
saber quais usuários têm arquivo aberto e mandar sinais aos processos
por nome.

%description -l tr
Bu paket, süreçlerin aðaç yapýsýný göstermek, hangi kullanýcýlarýn
açýk dosyasý olduðunu bulmak ve süreçlere isimleri ile sinyal
göndermek için gerekli programlarý içerir.

%prep
%setup  -q
%patch0 -p1 

%build
rm -f missing
gettextize --copy --force
aclocal
automake -a -c
autoheader
autoconf
CFLAGS="%{rpmcflags} -D_GNU_SOURCE -I/usr/include/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS Chang* NEWS README

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
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
