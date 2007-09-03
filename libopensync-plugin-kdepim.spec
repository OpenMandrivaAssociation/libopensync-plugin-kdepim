%define name	libopensync-plugin-kdepim
%define version	0.22
%define release %mkrel 1

Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	KDE plugin for opensync synchronization tool
URL:		http://www.opensync.org
Source:		http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2
License:	GPL
Group:		Office
BuildRequires:	opensync-devel
BuildRequires:	kdepim-devel
BuildRequires:  qt3-devel
Obsoletes:	multisync-kdepim
Provides:	multisync-kdepim
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
										
%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*


