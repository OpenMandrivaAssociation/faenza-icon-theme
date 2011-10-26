%define name	 faenza-icon-theme
%define version	 1.1
%define release	 %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Faenza icon theme
Group:          Graphical desktop/Other
License:        GPLv3+
URL:            http://tiheum.deviantart.com/art/Faenza-Icons-173323228
Source0:	http://faenza-icon-theme.googlecode.com/files/%{name}_%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
Requires(post): gtk2 >= 2.6.0
Requires(postun): gtk2 >= 2.6.0
BuildRequires:	icon-naming-utils >= 0.8.7
Requires:       gnome-icon-theme
Requires:	tango-icon-theme
Requires:       gnome-themes

%description
This icon theme for Gnome provides monochromatic icons for panels, toolbars and
buttons and colourful squared icons for devices, applications, folder, files and
Gnome menu items.

Four themes are included to fit with light or dark themes/panels.

%prep
%setup -q -c %{name}-%{version}

%install
%__rm -rf %{buildroot}
find Faenza* -type d -exec chmod 755 {} \;
find Faenza* -type f -exec chmod 644 {} \;
%__install -d -m 755 %{buildroot}%{_iconsdir}
%__mv Faenza* %{buildroot}%{_iconsdir}
touch %{buildroot}%{_iconsdir}/Faenza/icon-theme.cache
touch %{buildroot}%{_iconsdir}/Faenza-Dark/icon-theme.cache
touch %{buildroot}%{_iconsdir}/Faenza-Darker/icon-theme.cache
touch %{buildroot}%{_iconsdir}/Faenza-Darkest/icon-theme.cache

%post
%update_icon_cache Faenza
%update_icon_cache Faenza-Dark
%update_icon_cache Faenza-Darker
%update_icon_cache Faenza-Darkest

%postun
%clean_icon_cache Faenza
%clean_icon_cache Faenza-Dark
%clean_icon_cache Faenza-Darker
%clean_icon_cache Faenza-Darkest

%clean
%__rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog COPYING README
%dir %{_datadir}/icons/Faenza
%dir %{_datadir}/icons/Faenza-Dark
%dir %{_datadir}/icons/Faenza-Darker
%dir %{_datadir}/icons/Faenza-Darkest
%{_iconsdir}/Faenza*
%ghost %{_iconsdir}/Faenza/icon-theme.cache
%ghost %{_iconsdir}/Faenza-Dark/icon-theme.cache
%ghost %{_iconsdir}/Faenza-Darker/icon-theme.cache
%ghost %{_iconsdir}/Faenza-Darkest/icon-theme.cache
