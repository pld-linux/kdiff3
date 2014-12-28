
%define		qtver	4.4.3

Summary:	kdiff3 - Graphical tool for merging two or three files or directories
Summary(pl.UTF-8):	kdiff3 - Graficzne narzędzie do łączenia zawartości wielu plików lub katalogów
Name:		kdiff3
Version:	0.9.98
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/kdiff3/%{name}-%{version}.tar.gz
# Source0-md5:	b52f99f2cf2ea75ed5719315cbf77446
URL:		http://kdiff3.sourceforge.net/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	gettext-tools
BuildRequires:	kde4-kdebase-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	diffutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDiff3 is program able to compares two or three text input files,
shows the differences line by line and character by character (!),
provides an automatic merge-facility and an integrated editor for
comfortable solving of merge-conflicts and has an intuitive graphical
user interface,and it can also compare and merge directories!

%description -l pl.UTF-8
KDiff3 jest programem zdolnym do porównywania zawartości dwóch lub
trzech plików, wskazywania różnic linia po linii i znak po znaku; daje
możliwość automatycznego łączenia zawartości plików oraz zintegrowany
edytor do wygodnego rozwiązywania konfliktów powstałych podczas
łączenia zawartości. Posiada intuicyjny graficzny interfejs
użytkownika i może porównywać i łączyć zawartość katalogów.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

# remove locolor icons
%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{name} --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/kde4/*.so
%{_datadir}/apps/kdiff3
%{_datadir}/apps/kdiff3part
%{_datadir}/kde4/services/%{name}*.desktop
%{_desktopdir}/kde4/*.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
