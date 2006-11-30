Summary:	kdiff3 - Graphical tool for merging two or three files or directories
Summary(pl):	kdiff3 - Graficzne narzêdzie do ³±czenia zawarto¶ci wielu plików lub katalogów
Name:		kdiff3
Version:	0.9.91
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kdiff3/%{name}-%{version}.tar.gz
# Source0-md5:	e56613506475f23b8ab713f325dea6e3
Patch0:		%{name}-desktop.patch
Patch1:		kde-ac260.patch
Patch2:		kde-am.patch
Patch3:		kde-ac260-lt.patch
URL:		http://kdiff3.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
Requires:	diffutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautoreq      libtool(.*)

%description
KDiff3 is program able to compares two or three text input files,
shows the differences line by line and character by character (!),
provides an automatic merge-facility and an integrated editor for
comfortable solving of merge-conflicts and has an intuitive graphical
user interface,and it can also compare and merge directories!

%description -l pl
KDiff3 jest programem zdolnym do porównywania zawarto¶ci dwóch lub
trzech plików, wskazywania ró¿nic linia po linii i znak po znaku; daje
mo¿liwo¶æ automatycznego ³±czenia zawarto¶ci plików oraz zintegrowany
edytor do wygodnego rozwi±zywania konfliktów powsta³ych podczas
³±czenia zawarto¶ci. Posiada intuicyjny graficzny interfejs
u¿ytkownika i mo¿e porównywaæ i ³±czyæ zawarto¶æ katalogów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%{__sed} -i -e 's,\$(TOPSUBDIRS),doc po src,' Makefile.am

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f Makefile.cvs

%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	shelldesktopdir=%{_desktopdir}/kde

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_datadir}/apps/kdiff3
%{_datadir}/apps/kdiff3part
%{_datadir}/services/kdiff3part.desktop
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}*
