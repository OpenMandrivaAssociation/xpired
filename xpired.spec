%define name xpired
%define version 1.22
%define release %mkrel 19

Summary: Action puzzle game
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}-linux_source.tar.bz2
URL: http://xpired.temnet.org/
License: GPLv2+
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
Categories=Game;ArcadeGame;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc *.txt README*
%_datadir/applications/mandriva*
%_gamesbindir/*
%_gamesdatadir/*




%changelog
* Thu Sep 29 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.22-19mdv2012.0
+ Revision: 701910
- rebuild

* Sun Sep 27 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.22-18mdv2011.0
+ Revision: 450126
- rebuild for new SDL_gfx

* Tue Aug 04 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.22-17mdv2010.0
+ Revision: 408655
- update menu categories
- update license

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 1.22-16mdv2009.0
+ Revision: 262687
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.22-15mdv2009.0
+ Revision: 257683
- rebuild
- fix spacing at top of description
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.22-13mdv2008.1
+ Revision: 130484
- kill re-definition of %%buildroot on Pixel's request
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Wed Dec 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.22-13mdv2007.0
+ Revision: 100680
- Import xpired

* Wed Dec 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.22-13mdv2007.1
- Rebuild

* Tue Aug 01 2006 Götz Waschk <waschk@mandriva.org> 1.22-12mdv2007.0
- xdg menu
- Rebuild

* Wed Dec 28 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.22-11mdk
- Rebuild
- use mkrel

* Mon Dec 27 2004 Götz Waschk <waschk@linux-mandrake.com> 1.22-10mdk
- rebuild for new SDL_gfx

* Tue Nov 09 2004 Götz Waschk <waschk@linux-mandrake.com> 1.22-9mdk
- rebuild for new SDL_gfx

* Mon Aug 30 2004 Götz Waschk <waschk@linux-mandrake.com> 1.22-8mdk
- fix menu

* Wed May 19 2004 Götz Waschk <waschk@linux-mandrake.com> 1.22-7mdk
- new SDL_gfx

