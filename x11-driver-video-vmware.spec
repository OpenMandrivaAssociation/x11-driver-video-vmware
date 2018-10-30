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

BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xatracker)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server) >= 1.18
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(libudev)
Requires:	%{_lib}dri-drivers-vmwgfx
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-vmware is the X.org driver for VMWare(tm).

%prep
%setup -qn xf86-video-vmware-%{version}
%apply_patches

%build
export CC=gcc
%configure --enable-vmwarectrl-client
%make

%install
%makeinstall_std

# XXX: this should ultimately rather be handled by ie. XFdrake
install -d %{buildroot}%{_sysconfdir}/modprobe.d
tee > %{buildroot}%{_sysconfdir}/modprobe.d/vmwgfx.conf << EOF
options vmwgfx enable_fbdev=1
EOF

%files
%config(noreplace) %{_sysconfdir}/modprobe.d/vmwgfx.conf
%{_bindir}/vmwarectrl
%{_libdir}/xorg/modules/drivers/vmware_drv.so
%{_mandir}/man4/vmware.*
