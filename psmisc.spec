Summary:	More ps type tools for /proc filesystem
Summary(de):	Mehr ps-artige Tools für das /proc-Dateisystem 
Summary(fr):	Autres outils du type ps pour le système de fichiers /proc
Summary(pl):	Narzêdzia do kontroli procesów korzystaj±ce z systemu /proc
Summary(tr):	/proc dosya sistemi için ps tipi araçlar
Name:		psmisc
Version:	18
Release:	3
Copyright:	distributable
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source:		ftp://lrcftp.epfl.ch/pub/linux/local/psmisc/%{name}-%{version}.tar.gz
Patch0:		psmisc-opt.patch
Patch1:		psmisc-ncurses.patch
BuildPrereq:	ncurses-devel
Buildroot:	/tmp/%{name}-%{version}-root

%description
This package contains programs to display a tree of processes, find
out what users have a file open, and send signals to processes by name.

%description -l de
Dieses Paket enthält Programme, die eine Baumstruktur der Prozesse 
aufzeigen, herausfinden, welche Benutzer eine Datei geöffnet halten und 
Signale (anhand von Namen) an Prozesse ausgeben. 

%description -l fr
Ce paquetage contient les programmes pour afficher une arborescence de
processus, trouver quel utilisateur a un fichier ouvert et envoyer des
signaux aux processes par leurs noms.

%description -l pl
Ten pakiet zawiera programy umo¿liwiaj±ce wy¶wietlienie drzewa procesów, 
znalezienie u¿ytkownika, który otworzy³ dany plik i wys³anie sygna³u do
procesu o zadanej nazwie.

%description -l tr
Bu paket, süreçlerin aðaç yapýsýný göstermek, hangi kullanýcýlarýn açýk
dosyasý olduðunu bulmak ve süreçlere isimleri ile sinyal göndermek için
gerekli programlarý içerir.

%prep
%setup  -q -n %{name}
%patch0 -p1 
%patch1 -p1

%build
make LDFLAGS="-s" OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{bin,%{_sbindir},%{_bindir},%{_mandir}/man1}

install -s fuser $RPM_BUILD_ROOT%{_sbindir}
install -s {killall,pstree} $RPM_BUILD_ROOT%{_bindir}

install {fuser,killall,pstree}.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%attr(755,root,root) %{_sbindir}/fuser
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
