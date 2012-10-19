%define	gitdate	20120529

Name:		x11-driver-video-vmware
Version:	12.0.3
Release:	0.%{gitdate}.1
Summary:	X.org driver for VMWare(tm)
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vmware-%{gitdate}.tar.xz
Patch0:		vmware-11.0.3-vgahw.patch
Patch1:		vmware-12.0.1-vgahw.patch

BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	pkgconfig(xorg-server) >= 1.13
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	libdrm-devel

Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts:	xorg-x11-server < 7.0

%description
x11-driver-video-vmware is the X.org driver for VMWare(tm).

%prep
%setup -qn xf86-video-vmware-%{gitdate}
%patch0 -p1 -b .vgahw~
%patch1 -p1 -b .vgahw2~
autoreconf -i

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/vmware_drv.so
%{_mandir}/man4/vmware.*
