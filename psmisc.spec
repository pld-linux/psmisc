Summary:     More ps type tools for /proc filesystem
Summary(de): Mehr ps-artige Tools für das /proc-Dateisystem 
Summary(fr): Autres outils du type ps pour le système de fichiers /proc
Summary(pl): Narzêdzia do kontroli procesów korzystaj±ce z systemu /proc.
Summary(tr): /proc dosya sistemi için ps tipi araçlar
Name:        psmisc
Version:     17
Release:     5
Copyright:   distributable
Group:       Utilities/System
Source:      ftp://sunsite.unc.edu/pub/Linux/system/status/ps/%{name}-%{version}.tar.gz
Patch0:      psmisc-buildroot.patch
Patch1:      psmisc-optflags.patch
Buildroot:   /tmp/%{name}-%{version}-root

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
%setup -q -n psmisc
%patch0 -p1 -b .br
%patch1 -p1 -b .optflags

%build
make LDFLAGS="-s" OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{bin,usr/{sbin,bin,man/man1}}

install -s fuser $RPM_BUILD_ROOT/usr/sbin
install -s killall pstree $RPM_BUILD_ROOT/usr/bin
install {fuser,killall,pstree}.1 $RPM_BUILD_ROOT/usr/man/man1

gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755, root, root)
/usr/sbin/*
/usr/bin/*
%attr(644, root, man) /usr/man/man1/*

%changelog
* Tue Dec  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [17-5]
- added gziping man pages,
- build agains libncurses instead libtermcap.

* Tue Sep 29 1998 Marcin Korzonek <mkorz@shadow.eu.org>
- added pl translation,
- allow building from non-root account.

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- renamed the patch file .patch instead of .spec

* Thu Apr 09 1998 Erik Troan <ewt@redhat.com>
- updated to psmisc version 17
- buildrooted

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from version 11 to version 16
- spec file cleanups

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
