Summary:	More ps type tools for /proc filesystem
Summary(de):	Mehr ps-artige Tools für das /proc-Dateisystem 
Summary(fr):	Autres outils du type ps pour le système de fichiers /proc
Summary(pl):	Narzêdzia do kontroli procesów korzystaj±ce z systemu /proc
Summary(tr):	/proc dosya sistemi için ps tipi araçlar
Name:		psmisc
Version:	18
Release:	2
Copyright:	distributable
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source:		ftp://lrcftp.epfl.ch/pub/linux/local/%{name}-%{version}.tar.gz
Patch0:		%{name}.patch
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
%setup -q -n %{name}
%patch -p1 

%build
make 'LDFLAGS=-s' OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{bin,usr/{sbin,bin,man/man1}}

install -s fuser $RPM_BUILD_ROOT/usr/sbin
install -s {killall,pstree} $RPM_BUILD_ROOT/usr/bin

install {fuser,killall,pstree}.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%attr(755,root,root) /usr/sbin/fuser
%attr(755,root,root) /usr/bin/*

%{_mandir}/man1/*

%changelog
* Sat Mar 13 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [18-2]
- fixed Group(pl),
- commpressed man pages,
- cosmetic changes.

* Tue Sep 29 1998 Marcin Korzonek <mkorz@shadow.eu.org>
  [17-4d]
- translations modified for pl
- defined files permission
- allow building from non-root account

* Thu Jul 23 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [17-4]
- build against glibc-2.1,
- start at invalid RH spec file.
