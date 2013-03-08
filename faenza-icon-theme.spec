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
BuildRequires:	icon-naming-utils >= 0.8.7
Requires:	gnome-icon-theme
Requires:	tango-icon-theme
Requires:	gnome-themes

BuildArch:	noarch

%description
This icon theme for Gnome provides monochromatic icons for panels, 
toolbars and buttons and colourful squared icons for devices, 
applications, folder, files and Gnome menu items.

Four themes are included to fit with light or dark themes/panels.

%prep
%setup -q -n %{name}-%{version}

%install
find Faenza* -type d -exec chmod 755 {} \;
find Faenza* -type f -exec chmod 644 {} \;
install -d -m 755 %{buildroot}%{_iconsdir}
mv Faenza* %{buildroot}%{_iconsdir}
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

%postun
%clean_icon_cache Faenza
%clean_icon cache Faenza-Ambiance
%clean_icon_cache Faenza-Dark
%clean_icon_cache Faenza-Darker
%clean_icon_cache Faenza-Darkest
%clean_icon_cache Faenza_Radiance

%files
%defattr(0644,root,root,0755)
%{_iconsdir}/Faenza*

