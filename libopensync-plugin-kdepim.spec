%define name	libopensync-plugin-kdepim
%define version	0.33
%define svnrel	2596
%define release %mkrel 1.%{svnrel}

Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	KDE plugin for opensync synchronization tool
URL:		http://www.opensync.org
Source:		http://www.opensync.org/download/releases/%{version}/%{name}-r%{svnrel}.tar.bz2
License:	GPL
Group:		Office
BuildRequires:	opensync-devel >= %version
BuildRequires:	kdepim-devel
BuildRequires:  qt3-devel
Obsoletes:	multisync-kdepim
Provides:	multisync-kdepim
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This plugin allows applications using OpenSync to synchronise to and from
KDE.

%prep
%setup -q -n %{name}

%build
aclocal
automake --add-missing --copy --foreign || autoconf
%configure2_5x \
    --with-qt-dir=%{qt3dir} \
    --with-qt-libraries=%{qt3lib}
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README
%{_libdir}/opensync/plugins/*
%{_datadir}/opensync/defaults/*
