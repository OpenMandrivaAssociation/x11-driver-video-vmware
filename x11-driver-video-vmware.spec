#define	gitdate	20120529

Name:		x11-driver-video-vmware
Version:	13.0.0
Release:	1
Summary:	X.org driver for VMWare(tm)
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-vmware-%{version}.tar.bz2
Patch0:		vmware-11.0.3-vgahw.patch
Patch1:		vmware-12.0.1-vgahw.patch

BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	pkgconfig(xorg-server) >= 1.12
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	libdrm-devel

Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts:	xorg-x11-server < 7.0

%description
x11-driver-video-vmware is the X.org driver for VMWare(tm).

%prep
%setup -qn xf86-video-vmware-%{version}
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


%changelog
* Fri Oct 19 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 12.0.3-0.20120529.1
+ Revision: 819027
- update to latest from git to build against new x
- fix a couple of crashes (from fedora, rhbz #782995 & #801546)
- removal of .la files are now handled by spec-helper
- cosmetics

  + Bernhard Rosenkraenzer <bero@bero.eu>
    - Build for x11-server 1.13

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 12.0.2-2
+ Revision: 787289
- Rebuild for x11-server 1.12

* Mon Mar 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 12.0.2-1
+ Revision: 786922
- version update 12.0.2

* Thu Mar 15 2012 Alexander Khrukin <akhrukin@mandriva.org> 12.0.1-1
+ Revision: 785042
- version update 12.0.1

* Sat Mar 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 12.0.0-1
+ Revision: 783802
- version update 12.0.0

* Mon Jan 16 2012 Alexander Khrukin <akhrukin@mandriva.org> 11.1.0-1
+ Revision: 761669
- version update 11.1.0

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 11.0.3-6
+ Revision: 748491
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 11.0.3-5
+ Revision: 703682
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 11.0.3-4
+ Revision: 683592
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 11.0.3-3
+ Revision: 671186
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 11.0.3-2mdv2011.0
+ Revision: 595716
- require xorg server with proper ABI
- new release

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 11.0.2-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Mon Aug 16 2010 Thierry Vignaud <tv@mandriva.org> 11.0.2-1mdv2011.0
+ Revision: 570276
- new release

* Wed Mar 24 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 11.0.1-1mdv2010.1
+ Revision: 527187
- New version: 11.0.1
- New version: 11.0.0

* Wed Dec 30 2009 Frederik Himpe <fhimpe@mandriva.org> 10.16.9-1mdv2010.1
+ Revision: 484093
- update to new version 10.16.9

* Tue Nov 10 2009 Thierry Vignaud <tv@mandriva.org> 10.16.8-2mdv2010.1
+ Revision: 464346
- rebuild for new xserver

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 10.16.8-1mdv2010.0
+ Revision: 434779
- new release

* Tue Jul 21 2009 Frederik Himpe <fhimpe@mandriva.org> 10.16.7-1mdv2010.0
+ Revision: 398319
- update to new version 10.16.7

* Tue Jun 02 2009 Thierry Vignaud <tv@mandriva.org> 10.16.6-1mdv2010.0
+ Revision: 382148
- new release

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 10.16.5-3mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Sun Nov 30 2008 Adam Williamson <awilliamson@mandriva.org> 10.16.5-2mdv2009.1
+ Revision: 308188
- rebuild for new X server

* Fri Sep 05 2008 Thierry Vignaud <tv@mandriva.org> 10.16.5-1mdv2009.0
+ Revision: 281099
- new release

* Sun Jul 20 2008 Colin Guthrie <cguthrie@mandriva.org> 10.16.3-1mdv2009.0
+ Revision: 238849
- New version: 10.16.3

* Fri Jun 13 2008 Colin Guthrie <cguthrie@mandriva.org> 10.16.2-1mdv2009.0
+ Revision: 218784
- New version

  + Thierry Vignaud <tv@mandriva.org>
    - improved description
    - add missing dot at end of description
    - improved summary

* Mon May 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 10.16.1-1mdv2009.0
+ Revision: 206245
- Update to upstream release 10.16.1.

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 10.16.0-1mdv2009.0
+ Revision: 194131
- Update to version 10.1.6.0.

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 10.15.2-4mdv2008.1
+ Revision: 166217
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 10.15.2-3mdv2008.1
+ Revision: 156630
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 10.15.2-2mdv2008.1
+ Revision: 154769
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Note local tag xf86-video-vmware-10.15.2@mandriva suggested on upstream
  Tag at git checkout 62d898669baccfd4c312f3ed8f228d0c3217d3c3
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 11 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 10.15.2-1mdv2008.1
+ Revision: 97104
- new upstream version: 10.15.2
- minor spec cleanup

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages


* Tue Feb 13 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 10.15.0-1mdv2007.0
+ Revision: 120342
- new upstream version: 10.15.0

* Fri Dec 08 2006 Thierry Vignaud <tvignaud@mandriva.com> 10.14.1-1mdv2007.1
+ Revision: 93726
- new release

* Tue Nov 21 2006 Thierry Vignaud <tvignaud@mandriva.com> 10.14.0-1mdv2007.1
+ Revision: 85899
- new release
- fix group

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - new upstream release
    - rebuild to fix cooker uploading
    - increment release
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

