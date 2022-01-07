%define		kdeappsver	21.12.1
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kimap
Summary:	IMAP library
Name:		ka5-%{kaname}
Version:	21.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	83bc55bf44d916337e3b77539cd9dec7
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Test-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	cyrus-sasl-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-kmime-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KIMAP provides libraries to interface and communicate with IMAP mail
servers.

%description -l pl.UTF-8
KIMAP dostarcza biblioteki do komunikacji z serwerami IMAP.

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
%cmake -G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%ghost %{_libdir}/libKF5IMAP.so.5
%{_libdir}/libKF5IMAP.so.5.*.*
%{_libdir}/libkimaptest.a
%{_datadir}/qlogging-categories5/kimap.categories
%{_datadir}/qlogging-categories5/kimap.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KIMAP
%{_includedir}/KF5/kimap_version.h
%{_includedir}/KF5/kimaptest
%{_libdir}/cmake/KF5IMAP
%{_libdir}/libKF5IMAP.so
%{_libdir}/qt5/mkspecs/modules/qt_KIMAP.pri
