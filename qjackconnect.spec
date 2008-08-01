Summary: 	Qt based patchbay for Jack
Name: 		qjackconnect
Version: 	0.0.3b
Release: 	%mkrel 11
License:	GPL
Group: 		Sound
URL:		http://www.suse.de/~mana/jack.html
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	jackit >= 0.44.0
BuildRequires:	jackit-devel >= 0.44.0, libalsa-devel qt3-devel

%description
A Qt based patchbay for Jack (the Jack Audio Connection Kit)

%prep
%setup -q

%build
make QT_LIB_DIR=$QTDIR/%_lib -f make_qjackconnect

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 0755 qjackconnect $RPM_BUILD_ROOT/%{_bindir}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Qjackconnect
Comment=Qt-based Jackit Connector
Exec=%{_bindir}/%{name}
Icon=sound_section
Terminal=false
Type=Application
Categories=Qt;X-MandrivaLinux-Multimedia-Sound;Audio;
Encoding=UTF-8
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc INSTALL LICENSE
%{_bindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
