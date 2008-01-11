%define name xpired
%define version 1.22
%define release %mkrel 13

Summary: Action puzzle game
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}-linux_source.tar.bz2
URL: http://xpired.temnet.org/
License: GPL
Group: Games/Arcade
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libSDL_gfx-devel >= 2.0.8
BuildRequires: libSDL_mixer-devel 
BuildRequires: libSDL_image-devel 

%description

X-Pired is an action puzzle game. The goal of the game in each level
is to reach the exit square, avoiding exploding barrels and other
deadly stuff.

%prep
%setup -q -n src

%build
%make PREFIX=%_prefix SHARE_PREFIX=%_gamesdatadir/xpired

%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=%buildroot/%_prefix SHARE_PREFIX=%buildroot/%_gamesdatadir/xpired

mkdir -p %buildroot/%_gamesbindir
mv %buildroot/%_bindir/* %buildroot/%_gamesbindir

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=X-Pired
Comment=Action-puzzle game
Exec=%_gamesbindir/%{name}
Icon=arcade_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc *.txt README*
%_datadir/applications/mandriva*
%_gamesbindir/*
%_gamesdatadir/*


