Summary:	Utilities for managing processes on your system
Summary(de):	Utilities zum Verwalten der Prozesse auf Ihrem System
Summary(fr):	Autres outils du type ps pour le système de fichiers /proc
Summary(pl):	Narzêdzia do kontroli procesów
Summary(tr):	/proc dosya sistemi için ps tipi araçlar
Name:		psmisc
Version:	20.1
Release:	1
License:	distributable
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	autoconf
BuildRequires:	automake
URL:		http://psmisc.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir	/bin

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

%description -l fr
Ce paquetage contient les programmes pour afficher une arborescence de
processus, trouver quel utilisateur a un fichier ouvert et envoyer des
signaux aux processes par leurs noms.

%description -l pl
Ten pakiet zawiera programy umo¿liwiaj±ce wy¶wietlienie drzewa
procesów, znalezienie u¿ytkownika, który otworzy³ dany plik i wys³anie
sygna³u do procesu o zadanej nazwie.

%description -l tr
Bu paket, süreçlerin aðaç yapýsýný göstermek, hangi kullanýcýlarýn
açýk dosyasý olduðunu bulmak ve süreçlere isimleri ile sinyal
göndermek için gerekli programlarý içerir.

%prep
%setup  -q
%patch0 -p1 

%build
rm missing
automake -a -c
aclocal
autoheader
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS Chang* NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
