#
# Conditional build:
%bcond_without	selinux		# build without SELinux support
#
Summary:	Utilities for managing processes on your system
Summary(de.UTF-8):	Utilities zum Verwalten der Prozesse auf Ihrem System
Summary(es.UTF-8):	Más herramientas de tipo ps para el sistema de archivos /proc
Summary(fr.UTF-8):	Autres outils du type ps pour le système de fichiers /proc
Summary(ko.UTF-8):	시스템에서 프로세서를 관리하는 도구
Summary(pl.UTF-8):	Narzędzia do kontroli procesów
Summary(pt_BR.UTF-8):	Mais ferramentas do tipo ps para o sistema de arquivos /proc
Summary(ru.UTF-8):	Утилиты работы с процессами
Summary(tr.UTF-8):	/proc dosya sistemi için ps tipi araçlar
Summary(uk.UTF-8):	Утиліти роботи з процесами
Name:		psmisc
Version:	22.7
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/psmisc/%{name}-%{version}.tar.gz
# Source0-md5:	ee9ec3b60fe45057ec4cec19c94a2d15
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	9add7665e440bbd6b0b4f9293ba8b86d
Patch0:		%{name}-pl.po-update.patch
URL:		http://psmisc.sourceforge.net/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-devel >= 0.14.1
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	ncurses-devel >= 5.0
Conflicts:	heartbeat < 2.0.8-0.2
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

%description -l de.UTF-8
Das psmisc-Paket enthält Utilities zum Verwalten vom Prozessen auf
Ihrem System: pstree, killall und fuser. Der pstree-Befehl zeigt eine
Baumstruktur von allen laufenden Prozessen an. killall schickt
angegebenen Programmen ein Signal (SIGTERM, falls nichts anderes
angegeben wird). fuser identifiziert die PIDs (Prozess-IDs) von
Prozessen, die bestimmte Dateien oder Dateisysteme benutzen.

%description -l es.UTF-8
Este paquete contiene programas para enseñar un árbol de procesos,
saber que usuarios tienen archivo abierto y mandar señales a los
procesos por nombre.

%description -l fr.UTF-8
Ce paquetage contient les programmes pour afficher une arborescence de
processus, trouver quel utilisateur a un fichier ouvert et envoyer des
signaux aux processes par leurs noms.

%description -l pl.UTF-8
Ten pakiet zawiera programy umożliwiające wyświetlenie drzewa
procesów, znalezienie użytkownika, który otworzył dany plik i wysłanie
sygnału do procesu o zadanej nazwie.

%description -l pt_BR.UTF-8
Este pacote contém programas para mostrar uma árvore de processos,
saber quais usuários têm arquivo aberto e mandar sinais aos processos
por nome.

%description -l ru.UTF-8
В этот пакет включены программы для отображения дерева процессов,
получения информации о том, кем открыт файл и для посылки сигналов
процессам по имени процесса.

%description -l tr.UTF-8
Bu paket, süreçlerin ağaç yapısını göstermek, hangi kullanıcıların
açık dosyası olduğunu bulmak ve süreçlere isimleri ile sinyal
göndermek için gerekli programları içerir.

%description -l uk.UTF-8
Цей пакет містить програми для відображення дерева процесів, посилки
сигналів процесам по імені процеса та отримання інформації про те, хто
відкрив файл.

%prep
%setup -q
%patch0 -p1

rm -f po/stamp-po

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
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
