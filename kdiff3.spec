Summary:	kdiff3 - Graphical tool for merging two or three files or directories
Summary(pl):	kdiff3 - Graficzne narz�dzie do ��czenia zawarto�ci wielu plik�w lub katalog�w
Name:		kdiff3
Version:	0.9.80
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	335d4c86d0483b8b10071b769bb18a05
Patch0:		%{name}-types.patch
URL:		http://kdiff3.sourceforge.net/
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
KDiff3 jest programem zdolnym do por�wnywania zawarto�ci dw�ch lub
trzech plik�w, wskazywania r�nic linia po linii i znak po znaku, daje
automatyczne mo�liwo�ci ��czenia zawarto�ci plik�w oraz zintegrowany
edytor do wygodnego rozwi�zywanie konflikt�w powsta�ych podczas
��czenia zawarto�ci. Posiada intuicyjny graficzny interfejs
u�ytkownika i mo�e por�wnywa� i ��czy� zawarto�� katalog�w.

%prep
%setup -q
%patch0 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
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
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_datadir}/apps/kdiff3
%{_datadir}/apps/kdiff3part
%{_datadir}/services/kdiff3part.desktop
%{_applnkdir}/Development/%{name}.desktop
%{_iconsdir}/*/*/apps/%{name}.png
