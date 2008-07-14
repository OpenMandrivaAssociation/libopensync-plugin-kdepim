Name: 	 	libopensync-plugin-kdepim
Version: 	0.22
Epoch:		1
Release: 	%mkrel 3
Summary: 	KDE plugin for OpenSync synchronization tool
URL:		http://www.opensync.org
Source:		http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
License:	GPLv2
Group:		Office
BuildRequires:	libopensync-devel < 0.30
BuildRequires:	kdepim-devel >= 1:3.5.9-7
BuildRequires:  qt3-devel
Requires:	libopensync >= %{epoch}:%{version}
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
    --with-qt-dir=%{qt3dir} \
    --with-qt-libraries=%{qt3lib} \
    --enable-libsuffix=`echo %_lib | sed '/lib//'`
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
