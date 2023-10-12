Summary:	A GTK3-based panel for wayfire
Name:		wf-shell
Version:	0.8.0
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/WayfireWM/wf-shell/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	93e11f418814743e7212ee1d1dd08f87
URL:		https://wayfire.org/
BuildRequires:	alsa-lib-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk-layer-shell-devel >= 0.6
BuildRequires:	gtkmm3-devel >= 3.24
BuildRequires:	libdbusmenu-gtk3-devel
BuildRequires:	libstdc++-devel >= 6:9
BuildRequires:	meson >= 0.51.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 2.0
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	wayfire-devel
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols
BuildRequires:	wf-config-devel >= 0.8.0
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GTK3-based panel for wayfire.

%package devel
Summary:	Development files for wf-shell
Group:		Development/Libraries

%description devel
Development files for wf-shell.

%prep
%setup -q

%build
%meson build
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md wf-shell.ini.example
%attr(755,root,root) %{_bindir}/wayland-logout
%attr(755,root,root) %{_bindir}/wf-background
%attr(755,root,root) %{_bindir}/wf-dock
%attr(755,root,root) %{_bindir}/wf-panel
%{_datadir}/wayfire/icons/wayfire.png
%{_datadir}/wayfire/metadata/wf-shell
%{_datadir}/wayfire/wallpaper.jpg
%{_mandir}/man1/wayland-logout.1*

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/wf-shell.pc
