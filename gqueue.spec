%define name 	gqueue
%define version 0.99.1
%define release 2mdk

Name: 		%{name}
Summary: 	GNOME2 frontend for CUPS
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://web.tiscali.it/no-redirect-tiscali/diegobazzanella/
License:	GPL
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	cups-devel pkgconfig libgnomeui2-devel gettext ImageMagick

%description
gQueue is a Gnome2 frontend for lpq and lprm working with Cups queues.

%prep
%setup -q -n %name

%build
rm -f COPYING depcomp INSTALL install-sh missing mkinstalldirs
./autogen.sh
%configure
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="GQueue" longtitle="Control print jobs" section="Configuration/Printing"
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 pixmaps/gqueueicon.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 pixmaps/gqueueicon.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 pixmaps/gqueueicon.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS
%{_bindir}/%name
%{_datadir}/pixmaps/%name
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

