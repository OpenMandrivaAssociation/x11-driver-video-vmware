Name: x11-driver-video-vmware
Version: 10.15.2
Release: %mkrel 3
Summary: The X.org driver for VMWare(tm)
Group: System/X11
URL: http://xorg.freedesktop.org
# Note local tag xf86-video-vmware-10.15.2@mandriva suggested on upstream
# Tag at git checkout 62d898669baccfd4c312f3ed8f228d0c3217d3c3
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-vmware  xorg/drivers/xf86-video-vmware
# cd xorg/drivers/xf86-video/vmware
# git-archive --format=tar --prefix=xf86-video-vmware-10.15.2/ xf86-video-vmware-10.15.2@mandriva | bzip2 -9 > xf86-video-vmware-10.15.2.tar.bz2
########################################################################
Source0: xf86-video-vmware-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-vmware-10.15.2@mandriva..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-util-macros		>= 1.1.5-4mdk
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: x11-server-devel		>= 1.4
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for VMWare(tm)

%prep
%setup -q -n xf86-video-vmware-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/vmware_drv.so
%{_mandir}/man4/vmware.*
