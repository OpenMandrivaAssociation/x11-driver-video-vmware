%define _disable_ld_no_undefined 1
%define git %nil

Summary:	X.org driver for VMWare(tm)
Name:		x11-driver-video-vmware
Version:	13.4.0
Release:	1
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vmware-%{version}.tar.xz
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xatracker)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server) >= 1.18
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(libudev)
Requires:	%{_lib}dri-drivers-vmwgfx
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)
ExclusiveArch:	%{x86_64}

%description
x11-driver-video-vmware is the X.org driver for VMWare(tm).

%prep
%setup -qn xf86-video-vmware-%{version}
%autopatch -p1
for i in vmware.c vmware_bootstrap.c vmware.h; do
    sed -i -e 's/if XSERVER_LIBPCIACCESS/ifdef XSERVER_LIBPCIACCESS/g' src/$i
    sed -i -e 's/if !XSERVER_LIBPCIACCESS/ifndef XSERVER_LIBPCIACCESS/g' src/$i
done

%build
#export CC=gcc
%configure --enable-vmwarectrl-client
%make_build

%install
%make_install

%files
%{_bindir}/vmwarectrl
%{_libdir}/xorg/modules/drivers/vmware_drv.so
%{_mandir}/man4/vmware.*
