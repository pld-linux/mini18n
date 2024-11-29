Summary:	Minimal translation library
Summary(pl.UTF-8):	Minimalna biblioteka do tłumaczeń
Name:		mini18n
Version:	0.2.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://download.tuxfamily.org/yabause/releases/%{name}-%{version}.tar.gz
# Source0-md5:	a7a598d94171b56c0f0797fca91cdce4
Patch0:		%{name}-cmake.patch
URL:		http://wiki.yabause.org/index.php5?title=Mini18n
BuildRequires:	cmake >= 2.8
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mini18n is a translation library under GNU GPL.

%description -l pl.UTF-8
mini18n to biblioteka do tłumaczeń dostępna na licencji GNU GPL.

%package devel
Summary:	Header files for mini18n library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki mini18n
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for mini18n library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki mini18n.

%package static
Summary:	Static mini18n library
Summary(pl.UTF-8):	Statyczna biblioteka mini18n
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static mini18n library.

%description static -l pl.UTF-8
Statyczna biblioteka mini18n.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/libmini18n.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmini18n.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmini18n.so
%{_includedir}/mini18n.h
%{_includedir}/mini18n-multi.h
%{_mandir}/man3/mini18n.3*
%{_mandir}/man3/mini18n_set_locale.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libmini18n.a
