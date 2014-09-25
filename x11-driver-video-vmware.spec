%define _disable_ld_no_undefined 1
%define git 20131223

Summary:	X.org driver for VMWare(tm)
Name:		x11-driver-video-vmware
Version:	13.0.2
%if %git
Release:	0.%git.2
Source0:	xf86-video-vmware-%{git}.tar.xz
%else
Release:	3
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vmware-%{version}.tar.bz2
%endif
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Patch0:		vmware-11.0.3-vgahw.patch
Patch1:		vmware-12.0.1-vgahw.patch

BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(xatracker)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server) >= 1.12
BuildRequires:	pkgconfig(xproto)
Requires:	%{_lib}dri-drivers-vmwgfx
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-vmware is the X.org driver for VMWare(tm).

%prep
%if %git
%setup -qn xf86-video-vmware
%else
%setup -qn xf86-video-vmware-%{version}
%endif
%apply_patches
autoreconf -i

%build
%configure2_5x	--enable-vmwarectrl-client
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
