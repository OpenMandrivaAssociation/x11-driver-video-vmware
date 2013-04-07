%define _disable_ld_no_undefined 1

Summary:	X.org driver for VMWare(tm)
Name:		x11-driver-video-vmware
Version:	13.0.0
Release:	4
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vmware-%{version}.tar.bz2
Patch0:		vmware-11.0.3-vgahw.patch
Patch1:		vmware-12.0.1-vgahw.patch
Patch2:		remove_mibstore_h.patch

BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server) >= 1.12
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-vmware is the X.org driver for VMWare(tm).

%prep
%setup -qn xf86-video-vmware-%{version}
%apply_patches
autoreconf -i

%build
%configure2_5x	--enable-vmwarectrl-client
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/vmware_drv.so
%{_mandir}/man4/vmware.*

