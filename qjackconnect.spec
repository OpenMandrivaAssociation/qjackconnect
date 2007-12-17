Summary: 	Qt based patchbay for Jack
Name: 		qjackconnect
Version: 	0.0.3b
Release: 	%mkrel 8
License:	GPL
Group: 		Sound
URL:		http://www.suse.de/~mana/jack.html
Source: 	%{name}-%{version}.tar.bz2
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
mkdir -p $RPM_BUILD_ROOT/%{_menudir}
cat > $RPM_BUILD_ROOT/%{_menudir}/%{name} <<EOF
?package(%{name}): \
icon="sound_section.png" \
needs="x11" \
section="Multimedia/Sound" \
title="Qjackconnect" \
longtitle="Qt-based Jackit Connector" \
command="%{_bindir}/%{name}" \
xdg="true"
EOF

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

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc INSTALL LICENSE
%{_bindir}/*
%{_menudir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
