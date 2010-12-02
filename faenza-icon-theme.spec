%define zipname	 faenza_icons_by_tiheum-d2v6x24
%define name	 faenza-icon-theme
%define version	 0.8
%define release	 %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Faenza icon theme
Group:          Graphical desktop/Other
License:        GPLv3+
URL:            http://tiheum.deviantart.com/art/Faenza-Icons-173323228
Source0:        %{zipname}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
Requires(post): gtk2 >= 2.6.0
Requires(postun): gtk2 >= 2.6.0
BuildRequires:	icon-naming-utils >= 0.8.7
Requires:       gnome-icon-theme
Requires:	tango-icon-theme
Requires:       gnome-themes

%description
This package contains the Faenza and Faenza-Drak icon themes for Gnome.

%prep
%setup -q -c %{name}-%{version}
%__tar zxf Faenza.tar.gz
%__tar zxf Faenza-Dark.tar.gz

%install
%__rm -rf %{buildroot}
find Faenza -type d -exec chmod 755 {} \;
find Faenza -type f -exec chmod 644 {} \;
find Faenza-Dark -type d -exec chmod 755 {} \;
find Faenza-Dark -type f -exec chmod 644 {} \;
%__install -d -m 755 %{buildroot}%{_iconsdir}
%__mv Faenza Faenza-Dark %{buildroot}%{_iconsdir}
touch %{buildroot}%{_iconsdir}/Faenza/icon-theme.cache
touch %{buildroot}%{_iconsdir}/Faenza-Dark/icon-theme.cache

%post
%update_icon_cache Faenza
%update_icon_cache Faenza-Dark

%postun
%clean_icon_cache Faenza
%clean_icon_cache Faenza-Dark

%clean
%__rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog COPYING README
%dir %{_datadir}/icons/Faenza
%dir %{_datadir}/icons/Faenza-Dark
%{_iconsdir}/Faenza*
%ghost %{_iconsdir}/Faenza/icon-theme.cache
%ghost %{_iconsdir}/Faenza-Dark/icon-theme.cache

