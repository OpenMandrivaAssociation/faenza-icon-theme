Name:		faenza-icon-theme
Version:	1.3
Release:	1
Summary:	Faenza icon theme
Group:		Graphical desktop/Other
License:	GPLv3+
URL:		http://tiheum.deviantart.com/art/Faenza-Icons-173323228
Source0:	http://faenza-icon-theme.googlecode.com/files/%{name}_%{version}.zip
Requires(post):	gtk+2
Requires(postun):	gtk+2
Requires:	gnome-icon-theme
Requires:	hicolor-icon-theme
BuildArch:	noarch

%description
This icon theme for Gnome provides monochromatic icons for panels, 
toolbars and buttons and colourful squared icons for devices, 
applications, folder, files and Gnome menu items.

Four themes are included to fit with light or dark themes/panels.

%prep
%setup -q -c
for f in Faenza Faenza-Ambiance Faenza-Dark Faenza-Darker Faenza-Darkest Faenza-Radiance emesene-faenza-theme
do
    tar xf ${f}.tar.gz && rm -rf ${f}.tar.gz
done

%build
#fix rights
find Faenza* -type d -exec chmod 755 {} \;
find Faenza* -type f -exec chmod 644 {} \;
find . -name "*.theme" -exec rm -rf {} \;
#find . -type f -name "*.theme" -o -name "*.cache" -exec rm -f {} \;

echo "Nothing to build"


%install
install -d -m 755 %{buildroot}%{_iconsdir}
cp -a Faenza* %{buildroot}%{_iconsdir}

# originally from Fedora .spec
# link the distributor-logo and start-here icons to the gnome icon
# as currently we don't have our own icon
for icon in %{buildroot}%{_iconsdir}/*/places/*/distributor-logo.* ./*/places/*/start-here.*
do
    pushd ${icon%/*}
        ln -sf ./start-here-gnome.${icon##*.} ${icon##*/}
    popd
done

# link the start-here-symbolic icon to the gnome icon
for icon in %{buildroot}%{_iconsdir}/*/places/*/start-here-symbolic.*
do
    pushd ${icon%/*}
        ln -sf ./start-here-gnome-symbolic.${icon##*.} ${icon##*/}
    popd
done

#rm -rf %{buildroot}%{_iconsdir}/*/{*.cache,*.theme,*.tar.gz}

# ghost files
touch %{buildroot}%{_iconsdir}/Faenza/icon-theme.cache
touch %{buildroot}%{_iconsdir}/Faenza-Ambiance/icon-theme.cache
touch %{buildroot}%{_iconsdir}/Faenza-Dark/icon-theme.cache
touch %{buildroot}%{_iconsdir}/Faenza-Darker/icon-theme.cache
touch %{buildroot}%{_iconsdir}/Faenza-Darkest/icon-theme.cache
touch %{buildroot}%{_iconsdir}/Faenza-Radiance/icon-theme.cache

%post
%update_icon_cache Faenza
%update_icon_cache Faenza-Ambiance
%update_icon_cache Faenza-Dark
%update_icon_cache Faenza-Darker
%update_icon_cache Faenza-Darkest
%update_icon_cache Faenza-Radiance

%files
%doc AUTHORS README ChangeLog
%dir %{_iconsdir}/Faenza
%dir %{_iconsdir}/Faenza-Ambiance
%dir %{_iconsdir}/Faenza-Dark
%dir %{_iconsdir}/Faenza-Darker
%dir %{_iconsdir}/Faenza-Darkest
%dir %{_iconsdir}/Faenza-Radiance
%dir %{_iconsdir}/Faenza-Ambiance/status
%dir %{_iconsdir}/Faenza-Ambiance/status/22
%dir %{_iconsdir}/Faenza-Ambiance/stock
%dir %{_iconsdir}/Faenza-Ambiance/stock/22
%dir %{_iconsdir}/Faenza-Dark/actions
%dir %{_iconsdir}/Faenza-Dark/actions/16
%dir %{_iconsdir}/Faenza-Dark/actions/22
%dir %{_iconsdir}/Faenza-Dark/actions/24
%dir %{_iconsdir}/Faenza-Dark/actions/32
%dir %{_iconsdir}/Faenza-Dark/actions/48
%dir %{_iconsdir}/Faenza-Dark/actions/64
%dir %{_iconsdir}/Faenza-Dark/actions/96
%dir %{_iconsdir}/Faenza-Dark/actions/scalable
%dir %{_iconsdir}/Faenza-Dark/apps
%dir %{_iconsdir}/Faenza-Dark/apps/16
%dir %{_iconsdir}/Faenza-Dark/apps/22
%dir %{_iconsdir}/Faenza-Dark/apps/24
%dir %{_iconsdir}/Faenza-Dark/apps/32
%dir %{_iconsdir}/Faenza-Dark/apps/48
%dir %{_iconsdir}/Faenza-Dark/apps/64
%dir %{_iconsdir}/Faenza-Dark/apps/96
%dir %{_iconsdir}/Faenza-Dark/apps/scalable
%dir %{_iconsdir}/Faenza-Dark/categories
%dir %{_iconsdir}/Faenza-Dark/categories/16
%dir %{_iconsdir}/Faenza-Dark/categories/22
%dir %{_iconsdir}/Faenza-Dark/categories/24
%dir %{_iconsdir}/Faenza-Dark/categories/32
%dir %{_iconsdir}/Faenza-Dark/categories/48
%dir %{_iconsdir}/Faenza-Dark/categories/64
%dir %{_iconsdir}/Faenza-Dark/categories/96
%dir %{_iconsdir}/Faenza-Dark/categories/scalable
%dir %{_iconsdir}/Faenza-Dark/devices
%dir %{_iconsdir}/Faenza-Dark/devices/22
%dir %{_iconsdir}/Faenza-Dark/devices/24
%dir %{_iconsdir}/Faenza-Dark/extras
%dir %{_iconsdir}/Faenza-Dark/extras/deadbeef
%dir %{_iconsdir}/Faenza-Dark/extras/deadbeef/pixmaps
%dir %{_iconsdir}/Faenza-Dark/extras/keepassx
%dir %{_iconsdir}/Faenza-Dark/extras/keepassx/icons
%dir %{_iconsdir}/Faenza-Dark/extras/lastfm
%dir %{_iconsdir}/Faenza-Dark/extras/lastfm/icons
%dir %{_iconsdir}/Faenza-Dark/extras/liferea
%dir %{_iconsdir}/Faenza-Dark/extras/liferea/pixmaps
%dir %{_iconsdir}/Faenza-Dark/extras/pixmaps
%dir %{_iconsdir}/Faenza-Dark/extras/pixmaps/guake
%dir %{_iconsdir}/Faenza-Dark/extras/radiotray
%dir %{_iconsdir}/Faenza-Dark/extras/radiotray/images
%dir %{_iconsdir}/Faenza-Dark/places
%dir %{_iconsdir}/Faenza-Dark/places/22
%dir %{_iconsdir}/Faenza-Dark/places/24
%dir %{_iconsdir}/Faenza-Dark/places/32
%dir %{_iconsdir}/Faenza-Dark/places/48
%dir %{_iconsdir}/Faenza-Dark/places/64
%dir %{_iconsdir}/Faenza-Dark/places/96
%dir %{_iconsdir}/Faenza-Dark/places/scalable
%dir %{_iconsdir}/Faenza-Dark/status
%dir %{_iconsdir}/Faenza-Dark/status/16
%dir %{_iconsdir}/Faenza-Dark/status/22
%dir %{_iconsdir}/Faenza-Dark/status/24
%dir %{_iconsdir}/Faenza-Dark/status/32
%dir %{_iconsdir}/Faenza-Dark/status/48
%dir %{_iconsdir}/Faenza-Dark/status/64
%dir %{_iconsdir}/Faenza-Dark/status/96
%dir %{_iconsdir}/Faenza-Dark/status/scalable
%dir %{_iconsdir}/Faenza-Dark/stock
%dir %{_iconsdir}/Faenza-Dark/stock/16
%dir %{_iconsdir}/Faenza-Dark/stock/22
%dir %{_iconsdir}/Faenza-Dark/stock/24
%dir %{_iconsdir}/Faenza-Dark/stock/32
%dir %{_iconsdir}/Faenza-Dark/stock/48
%dir %{_iconsdir}/Faenza-Dark/stock/64
%dir %{_iconsdir}/Faenza-Dark/stock/96
%dir %{_iconsdir}/Faenza-Dark/stock/scalable
%dir %{_iconsdir}/Faenza-Darker/actions
%dir %{_iconsdir}/Faenza-Darker/actions/16
%dir %{_iconsdir}/Faenza-Darker/actions/22
%dir %{_iconsdir}/Faenza-Darker/actions/24
%dir %{_iconsdir}/Faenza-Darker/actions/32
%dir %{_iconsdir}/Faenza-Darker/actions/48
%dir %{_iconsdir}/Faenza-Darker/actions/64
%dir %{_iconsdir}/Faenza-Darker/actions/96
%dir %{_iconsdir}/Faenza-Darker/actions/scalable
%dir %{_iconsdir}/Faenza-Darker/apps
%dir %{_iconsdir}/Faenza-Darker/apps/16
%dir %{_iconsdir}/Faenza-Darker/apps/22
%dir %{_iconsdir}/Faenza-Darker/apps/24
%dir %{_iconsdir}/Faenza-Darker/apps/32
%dir %{_iconsdir}/Faenza-Darker/apps/48
%dir %{_iconsdir}/Faenza-Darker/apps/64
%dir %{_iconsdir}/Faenza-Darker/apps/96
%dir %{_iconsdir}/Faenza-Darker/apps/scalable
%dir %{_iconsdir}/Faenza-Darker/stock
%dir %{_iconsdir}/Faenza-Darker/stock/16
%dir %{_iconsdir}/Faenza-Darker/stock/22
%dir %{_iconsdir}/Faenza-Darker/stock/24
%dir %{_iconsdir}/Faenza-Darker/stock/32
%dir %{_iconsdir}/Faenza-Darker/stock/48
%dir %{_iconsdir}/Faenza-Darker/stock/64
%dir %{_iconsdir}/Faenza-Darker/stock/96
%dir %{_iconsdir}/Faenza-Darker/stock/scalable
%dir %{_iconsdir}/Faenza-Darkest/actions
%dir %{_iconsdir}/Faenza-Darkest/actions/16
%dir %{_iconsdir}/Faenza-Darkest/actions/22
%dir %{_iconsdir}/Faenza-Darkest/actions/24
%dir %{_iconsdir}/Faenza-Darkest/actions/32
%dir %{_iconsdir}/Faenza-Darkest/actions/48
%dir %{_iconsdir}/Faenza-Darkest/actions/64
%dir %{_iconsdir}/Faenza-Darkest/actions/96
%dir %{_iconsdir}/Faenza-Darkest/actions/scalable
%dir %{_iconsdir}/Faenza-Darkest/apps
%dir %{_iconsdir}/Faenza-Darkest/apps/16
%dir %{_iconsdir}/Faenza-Darkest/apps/22
%dir %{_iconsdir}/Faenza-Darkest/apps/24
%dir %{_iconsdir}/Faenza-Darkest/apps/32
%dir %{_iconsdir}/Faenza-Darkest/apps/48
%dir %{_iconsdir}/Faenza-Darkest/apps/64
%dir %{_iconsdir}/Faenza-Darkest/apps/96
%dir %{_iconsdir}/Faenza-Darkest/apps/scalable
%dir %{_iconsdir}/Faenza-Darkest/stock
%dir %{_iconsdir}/Faenza-Darkest/stock/16
%dir %{_iconsdir}/Faenza-Darkest/stock/22
%dir %{_iconsdir}/Faenza-Darkest/stock/24
%dir %{_iconsdir}/Faenza-Darkest/stock/32
%dir %{_iconsdir}/Faenza-Darkest/stock/48
%dir %{_iconsdir}/Faenza-Darkest/stock/64
%dir %{_iconsdir}/Faenza-Darkest/stock/96
%dir %{_iconsdir}/Faenza-Darkest/stock/scalable
%dir %{_iconsdir}/Faenza-Radiance/status
%dir %{_iconsdir}/Faenza-Radiance/status/22
%dir %{_iconsdir}/Faenza-Radiance/stock
%dir %{_iconsdir}/Faenza-Radiance/stock/22
%dir %{_iconsdir}/Faenza/actions
%dir %{_iconsdir}/Faenza/actions/16
%dir %{_iconsdir}/Faenza/actions/22
%dir %{_iconsdir}/Faenza/actions/24
%dir %{_iconsdir}/Faenza/actions/32
%dir %{_iconsdir}/Faenza/actions/48
%dir %{_iconsdir}/Faenza/actions/64
%dir %{_iconsdir}/Faenza/actions/96
%dir %{_iconsdir}/Faenza/actions/scalable
%dir %{_iconsdir}/Faenza/apps
%dir %{_iconsdir}/Faenza/apps/16
%dir %{_iconsdir}/Faenza/apps/22
%dir %{_iconsdir}/Faenza/apps/24
%dir %{_iconsdir}/Faenza/apps/32
%dir %{_iconsdir}/Faenza/apps/48
%dir %{_iconsdir}/Faenza/apps/64
%dir %{_iconsdir}/Faenza/apps/96
%dir %{_iconsdir}/Faenza/apps/scalable
%dir %{_iconsdir}/Faenza/categories
%dir %{_iconsdir}/Faenza/categories/16
%dir %{_iconsdir}/Faenza/categories/22
%dir %{_iconsdir}/Faenza/categories/24
%dir %{_iconsdir}/Faenza/categories/32
%dir %{_iconsdir}/Faenza/categories/48
%dir %{_iconsdir}/Faenza/categories/64
%dir %{_iconsdir}/Faenza/categories/96
%dir %{_iconsdir}/Faenza/categories/scalable
%dir %{_iconsdir}/Faenza/devices
%dir %{_iconsdir}/Faenza/devices/16
%dir %{_iconsdir}/Faenza/devices/22
%dir %{_iconsdir}/Faenza/devices/24
%dir %{_iconsdir}/Faenza/devices/32
%dir %{_iconsdir}/Faenza/devices/48
%dir %{_iconsdir}/Faenza/devices/64
%dir %{_iconsdir}/Faenza/devices/96
%dir %{_iconsdir}/Faenza/devices/scalable
%dir %{_iconsdir}/Faenza/emblems
%dir %{_iconsdir}/Faenza/emblems/16
%dir %{_iconsdir}/Faenza/emblems/22
%dir %{_iconsdir}/Faenza/emblems/24
%dir %{_iconsdir}/Faenza/emblems/32
%dir %{_iconsdir}/Faenza/emblems/48
%dir %{_iconsdir}/Faenza/emblems/64
%dir %{_iconsdir}/Faenza/emblems/8
%dir %{_iconsdir}/Faenza/emblems/96
%dir %{_iconsdir}/Faenza/emblems/scalable
%dir %{_iconsdir}/Faenza/extras
%dir %{_iconsdir}/Faenza/extras/deadbeef
%dir %{_iconsdir}/Faenza/extras/deadbeef/pixmaps
%dir %{_iconsdir}/Faenza/extras/keepassx
%dir %{_iconsdir}/Faenza/extras/keepassx/icons
%dir %{_iconsdir}/Faenza/extras/lastfm
%dir %{_iconsdir}/Faenza/extras/lastfm/icons
%dir %{_iconsdir}/Faenza/extras/liferea
%dir %{_iconsdir}/Faenza/extras/liferea/pixmaps
%dir %{_iconsdir}/Faenza/extras/pixmaps
%dir %{_iconsdir}/Faenza/extras/pixmaps/guake
%dir %{_iconsdir}/Faenza/extras/radiotray
%dir %{_iconsdir}/Faenza/extras/radiotray/images
%dir %{_iconsdir}/Faenza/mimetypes
%dir %{_iconsdir}/Faenza/mimetypes/16
%dir %{_iconsdir}/Faenza/mimetypes/22
%dir %{_iconsdir}/Faenza/mimetypes/24
%dir %{_iconsdir}/Faenza/mimetypes/32
%dir %{_iconsdir}/Faenza/mimetypes/48
%dir %{_iconsdir}/Faenza/mimetypes/64
%dir %{_iconsdir}/Faenza/mimetypes/96
%dir %{_iconsdir}/Faenza/mimetypes/scalable
%dir %{_iconsdir}/Faenza/places
%dir %{_iconsdir}/Faenza/places/16
%dir %{_iconsdir}/Faenza/places/22
%dir %{_iconsdir}/Faenza/places/24
%dir %{_iconsdir}/Faenza/places/32
%dir %{_iconsdir}/Faenza/places/48
%dir %{_iconsdir}/Faenza/places/64
%dir %{_iconsdir}/Faenza/places/96
%dir %{_iconsdir}/Faenza/places/scalable
%dir %{_iconsdir}/Faenza/status
%dir %{_iconsdir}/Faenza/status/16
%dir %{_iconsdir}/Faenza/status/22
%dir %{_iconsdir}/Faenza/status/24
%dir %{_iconsdir}/Faenza/status/32
%dir %{_iconsdir}/Faenza/status/48
%dir %{_iconsdir}/Faenza/status/64
%dir %{_iconsdir}/Faenza/status/96
%dir %{_iconsdir}/Faenza/status/scalable
%dir %{_iconsdir}/Faenza/stock
%dir %{_iconsdir}/Faenza/stock/16
%dir %{_iconsdir}/Faenza/stock/22
%dir %{_iconsdir}/Faenza/stock/24
%dir %{_iconsdir}/Faenza/stock/32
%dir %{_iconsdir}/Faenza/stock/48
%dir %{_iconsdir}/Faenza/stock/64
%dir %{_iconsdir}/Faenza/stock/96
%dir %{_iconsdir}/Faenza/stock/io
%dir %{_iconsdir}/Faenza/stock/io/16
%dir %{_iconsdir}/Faenza/stock/io/22
%dir %{_iconsdir}/Faenza/stock/io/24
%dir %{_iconsdir}/Faenza/stock/io/32
%dir %{_iconsdir}/Faenza/stock/io/48
%dir %{_iconsdir}/Faenza/stock/io/64
%dir %{_iconsdir}/Faenza/stock/io/96
%dir %{_iconsdir}/Faenza/stock/io/scalable
%dir %{_iconsdir}/Faenza/stock/scalable
%{_iconsdir}/Faenza*/*/*/*.icon
%{_iconsdir}/Faenza*/*/*/*.png
%{_iconsdir}/Faenza*/*/*/*/*.png
%{_iconsdir}/Faenza*/*/*/*.xpm
%{_iconsdir}/Faenza*/*/*/*.svg
%{_iconsdir}/Faenza*/*/*/*/*.svg
%ghost %{_iconsdir}/Faenza/icon-theme.cache
%ghost %{_iconsdir}/Faenza-Ambiance/icon-theme.cache
%ghost %{_iconsdir}/Faenza-Dark/icon-theme.cache
%ghost %{_iconsdir}/Faenza-Darker/icon-theme.cache
%ghost %{_iconsdir}/Faenza-Darkest/icon-theme.cache
%ghost %{_iconsdir}/Faenza-Radiance/icon-theme.cache
