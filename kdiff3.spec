
Summary:	kdiff3 - Graphical tool for merging two or three files or directories
Summary(pl):	kdiff3 - Graficzne narzêdzie do ³±czenie zawarto¶ci wielu plików lub katalogów
Name:		kdiff3
Version:	0.9.80
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	335d4c86d0483b8b10071b769bb18a05
URL:		http://kdiff3.sourceforge.net/
BuildRequires:	autoconf >= 2.54
BuildRequires:	kdelibs-devel >= 3.1.1a
Requires:  	diffutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
KDiff3 is program able to compares two or three text input files,
shows the differences line by line and character by character (!),
provides an automatic merge-facility and an integrated editor for
comfortable solving of merge-conflicts and has an intuitive graphical
user interface,and it can also compare and merge directories!

%description -l pl
KDiff3 jest programem zdolnym do porównywania zawarto¶ci dwóch lub
trzech plików, wskazywania ró¿nic linia po linii i znak po znaku, daje
automatyczne mo¿liwo¶ci ³±czenia zawarto¶ci plików oraz zintegrowany
edytor do wygodnego rozwi±zywanie konfliktów powsta³ych podczas
³±czenia zawarto¶ci. Posiada intuicyjny graficzny interfejs
u¿ytkownika i mo¿e porównywaæ i ³±czyæ zawarto¶æ katalogów.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
kde_appsdir="%{_applnkdir}"; export kde_appsdir

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/apps/%{name}
%{_datadir}/apps/*/*.rc
%{_datadir}/services/kdiff3part.desktop
%{_applnkdir}/Development/%{name}.desktop
%{_pixmapsdir}/*/*/apps/%{name}.png
%{_libdir}/kde3/*
#/usr/lib/kde3/libkdiff3part.la # Do we need .la ?
#/usr/lib/kde3/libkdiff3part.so
