%define enable_kde4 1
%{?_with_static: %{expand: %%global enable_static 1}}

Name: 	 	libopensync-plugin-kdepim
Version: 	0.22
Epoch:		1
Release: 	%mkrel 4
Summary: 	KDE plugin for OpenSync synchronization tool
URL:		http://www.opensync.org
Source:		http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
Patch0:		libopensync-plugin-kdepim-0.22-kde4.patch
License:	GPLv2
Group:		Office
BuildRequires:	libopensync-devel < 0.30
%if %{enable_kde4}
BuildRequires:	kdepimlibs4-devel
BuildRequires:	openldap-devel
%else
BuildRequires:	kdepim-devel >= 1:3.5.9-7
BuildRequires:  qt3-devel
%endif
Requires:	libopensync >= %{epoch}:%{version}
Obsoletes:	multisync-kdepim
Provides:	multisync-kdepim
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This plugin allows applications using OpenSync to synchronise to and from
KDE.

%prep
%setup -q
%if %{enable_kde4}
%patch0 -p1 -b .kdepim4
%endif
autoreconf -i
%build
%if %{enable_kde4}
%configure2_5x \
    --with-qt-dir=%{qt4dir} \
    --with-qt-libraries=%{qt4lib} \
    --enable-libsuffix=`echo %_lib | sed '/lib//'` \
    --disable-rpath
%else
%configure2_5x \
    --with-qt-dir=%{qt3dir} \
    --with-qt-libraries=%{qt3lib} \
    --enable-libsuffix=`echo %_lib | sed '/lib//'`
%endif
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*
