%define		kdeappsver	18.04.0
%define		qtver		5.3.2
%define		kaname		kimap
Summary:	kimap
Name:		ka5-%{kaname}
Version:	18.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	f9c3df6792442aaea02c6e94ffd4e305
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	ka5-kmime-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kimap.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.


%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kimap.categories
/etc/xdg/kimap.renamecategories
%ghost %{_libdir}/libKF5IMAP.so.5
%{_libdir}/libKF5IMAP.so.5.*.*
%{_libdir}/libkimaptest.a

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KIMAP
%{_includedir}/KF5/kimap_version.h
%{_includedir}/KF5/kimaptest
%{_libdir}/cmake/KF5IMAP
%{_libdir}/libKF5IMAP.so
%{_libdir}/qt5/mkspecs/modules/qt_KIMAP.pri
