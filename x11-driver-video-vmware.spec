%define _disable_ld_no_undefined 1
%define git %nil

Summary:	X.org driver for VMWare(tm)
Name:		x11-driver-video-vmware
Version:	13.3.0
Release:	3
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vmware-%{version}.tar.bz2
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
# Backported from: https://gitlab.freedesktop.org/xorg/driver/xf86-video-vmware.git
Patch0:		0001-Remove-obsolete-B16-B32-tags-in-struct-definitions.patch
Patch1:		0002-vmwgfx-Fix-XVideo-memory-leaks.patch
Patch2:		0003-vmwgfx-Fix-a-memory-leak.patch
Patch3:		0004-vmwgfx-Use-libdrm-to-obtain-the-drm-device-node-name.patch
Patch4:		0005-saa-Make-sure-damage-destruction-happens-at-the-corr.patch
Patch5:		0006-vmwgfx-Fix-invalid-memory-accesses-in-CloseScreen.patch
Patch6:		0007-vmwgfx-Don-t-exceed-the-device-command-size-limit-v3.patch
Patch7:		0008-vmwgfx-Limit-the-number-of-cliprects-in-a-drm-dirtyf.patch
Patch8:		0009-vmwgfx-Limit-the-number-of-cliprects-in-a-drm-presen.patch
Patch9:		0010-vmwgfx-Limit-the-number-of-cliprects-in-a-drm-presen.patch
Patch10:	0011-vmwgfx-Unify-style-in-scanout_update-and-present-fun.patch

BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xatracker)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server) >= 1.18
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(libudev)
Requires:	%{_lib}dri-drivers-vmwgfx
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)
ExcludeArch: %{armx} %{riscv}

%description
x11-driver-video-vmware is the X.org driver for VMWare(tm).

%prep
%setup -qn xf86-video-vmware-%{version}
%autopatch -p1

%build
export CC=gcc
%configure --enable-vmwarectrl-client
%make_build

%install
%make_install

install -d %{buildroot}%{_modulesloaddir}
tee > %{buildroot}%{_modulesloaddir}/vmwgfx.conf << EOF
options vmwgfx enable_fbdev=1
EOF

%files
%config(noreplace) %{_modulesloaddir}/vmwgfx.conf
%{_bindir}/vmwarectrl
%{_libdir}/xorg/modules/drivers/vmware_drv.so
%{_mandir}/man4/vmware.*
