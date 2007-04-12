%define name	libopensync-plugin-kdepim
%define version	0.20
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	KDE plugin for opensync synchronization tool
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://www.opensync.org
License:	GPL
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot

BuildRequires:	opensync-devel
BuildRequires:	kdepim-devel
BuildRequires:  qt3-devel
BuildRequires:	chrpath

Obsoletes:	multisync-kdepim
Provides:	multisync-kdepim

%description
This plugin allows applications using OpenSync to synchronise to and from
KDE.

%prep
%setup -q

%build
%configure2_5x \
    --with-qt-dir=%_prefix/lib/qt3 \
    --with-qt-libraries=%_prefix/lib/qt3/%_lib \
    --enable-libsuffix=`echo %_lib | sed '/lib//'`
%make
chrpath -d .libs/kdepim_lib.so
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*


