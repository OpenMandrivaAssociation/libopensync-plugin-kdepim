%define name	libopensync-plugin-kdepim
%define version	0.35
%define release %mkrel 1

Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	KDE plugin for opensync synchronization tool
URL:		http://www.opensync.org
Source:		http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
License:	GPL
Group:		Office
BuildRequires:	opensync-devel >= %version
BuildRequires:	kdepim-devel
BuildRequires:  qt3-devel
BuildRequires:	cmake
Obsoletes:	multisync-kdepim
Provides:	multisync-kdepim
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This plugin allows applications using OpenSync to synchronise to and from
KDE.

%prep
%setup -q

%build
%cmake
%make
										
%install
rm -rf %{buildroot}
cd build
%makeinstall_std
cd -

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README
%{_libdir}/opensync-1.0/plugins/*
%{_datadir}/opensync-1.0/defaults/*
