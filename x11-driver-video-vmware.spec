Name: x11-driver-video-vmware
Version: 12.0.2
Release: 3
Summary: X.org driver for VMWare(tm)
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vmware-%{version}.tar.bz2
 
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: pkgconfig(xorg-server) >= 1.13
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: libdrm-devel

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-vmware is the X.org driver for VMWare(tm).

%prep
%setup -qn xf86-video-vmware-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/drivers/vmware_drv.so
%{_mandir}/man4/vmware.*

