%global optflags %{optflags} -fPIC
%define _disable_ld_no_undefined 1
%define git %nil

Summary:	X.org driver for VMWare(tm)
Name:		x11-driver-video-vmware
Version:	13.4.0.1
Release:	1
Source0:	https://github.com/X11Libre/xf86-video-vmware/archive/refs/tags/xlibre-xf86-video-vmware-%{version}.tar.gz
Group:		System/X11
License:	MIT
Url:		https://xorg.freedesktop.org
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xatracker)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(libudev)
Requires:	%{_lib}dri-drivers-vmwgfx
#Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)
ExclusiveArch:	%{x86_64}
BuildSystem:	autotools
BuildOption:	--enable-vmwarectrl-client

%description
x11-driver-video-vmware is the X.org driver for VMWare(tm).

%prep -a
NOCONFIGURE=1 ./autogen.sh

%files
%{_bindir}/vmwarectrl
%{_libdir}/xorg/modules/drivers/vmware_drv.so
%{_mandir}/man4/vmware.*
