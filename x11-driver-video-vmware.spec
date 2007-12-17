Name: x11-driver-video-vmware
Version: 10.15.2
Release: %mkrel 2
Summary: The X.org driver for VMWare(tm)
Group: System/X11
URL: http://xorg.freedesktop.org

########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-vmware  xorg/drivers/xf86-video-vmware
# cd xorg/drivers/xf86-video/vmware
# git-archive --format=tar --prefix=xf86-video-vmware-10.15.2/ master | bzip2 -9 > xf86-video-vmware-10.15.2.tar.bz2
########################################################################
Source0: xf86-video-vmware-%{version}.tar.bz2

License: MIT

########################################################################
# git-format-patch master..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11-server < 7.0

%description

%prep
%setup -q -n xf86-video-vmware-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/vmware_drv.la
%{_libdir}/xorg/modules/drivers/vmware_drv.so
%{_mandir}/man4/vmware.*


