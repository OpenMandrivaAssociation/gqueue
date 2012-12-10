%define name 	gqueue
%define version 0.99.1
%define release  6

Name: 		%{name}
Summary: 	GNOME2 frontend for CUPS
Version: 	%{version}
Release: 	%{release}

Source0:		%{name}-%{version}.tar.bz2
URL:		http://web.tiscali.it/no-redirect-tiscali/diegobazzanella/
License:	GPL
Group:		Graphical desktop/GNOME
BuildRequires:	cups-devel pkgconfig pkgconfig(libgnomeui-2.0) gettext imagemagick

%description
gQueue is a Gnome2 frontend for lpq and lprm working with Cups queues.

%prep
%setup -q -n %name

%build
export LIBS="-lX11"
rm -f COPYING depcomp INSTALL install-sh missing mkinstalldirs
./autogen.sh
%configure
%make
										
%install
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=%{name}
Name=GQueue
Comment=Control print jobs
Categories=HardwareSettings;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 pixmaps/gqueueicon.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 pixmaps/gqueueicon.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 pixmaps/gqueueicon.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS
%{_bindir}/%name
%{_datadir}/pixmaps/%name
%{_datadir}/applications/mandriva-%name.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.99.1-6mdv2011.0
+ Revision: 619251
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.99.1-5mdv2010.0
+ Revision: 429319
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.99.1-4mdv2009.0
+ Revision: 246598
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.99.1-2mdv2008.1
+ Revision: 131679
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import gqueue


* Sun Feb 6 2005 Austin Acton <austin@mandrake.org> 0.99.1-2mdk
- birthday
- fix summary and menu

* Wed Dec 31 2003 Austin Acton <austin@linux.ca> 0.99.1-1mdk
- 0.99.1
- fix buildrequires

* Thu Dec 11 2003 Austin Acton <austin@linux.ca> 0.9-1mdk
- 0.9
- convert icons on-the-fly

* Tue May 27 2003 Austin Acton <aacton@yorku.ca> 0.8-2mdk
- distlit (DIRM)

* Fri Mar 21 2003 Austin Acton <aacton@yorku.ca> 0.8-1mdk
- 0.8

* Tue Feb 11 2003 Austin Acton <aacton@yorku.ca> 0.6-1mdk
- 0.6

* Tue Jan 21 2003 Austin Acton <aacton@yorku.ca> 0.3-1mdk
- initial package
