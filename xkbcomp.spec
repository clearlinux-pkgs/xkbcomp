#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE23B7E70B467F0BF (office@who-t.net)
#
Name     : xkbcomp
Version  : 1.4.2
Release  : 15
URL      : https://xorg.freedesktop.org/releases/individual/app/xkbcomp-1.4.2.tar.gz
Source0  : https://xorg.freedesktop.org/releases/individual/app/xkbcomp-1.4.2.tar.gz
Source99 : https://xorg.freedesktop.org/releases/individual/app/xkbcomp-1.4.2.tar.gz.sig
Summary  : XKB keymap compiler
Group    : Development/Tools
License  : HPND
Requires: xkbcomp-bin = %{version}-%{release}
Requires: xkbcomp-license = %{version}-%{release}
Requires: xkbcomp-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
Patch1: dontwarn.patch

%description
X Keyboard Extension
--------------------
The X Keyboard Extension essentially replaces the core protocol definition of
keyboard. The extension makes possible to clearly and explicitly specify most
aspects of keyboard behaviour on per-key basis and to more closely track the
logical and physical state of the keyboard. It also includes a number of
keyboard controls designed to make keyboards more accessible to people with
physical impairments.

%package bin
Summary: bin components for the xkbcomp package.
Group: Binaries
Requires: xkbcomp-license = %{version}-%{release}

%description bin
bin components for the xkbcomp package.


%package dev
Summary: dev components for the xkbcomp package.
Group: Development
Requires: xkbcomp-bin = %{version}-%{release}
Provides: xkbcomp-devel = %{version}-%{release}
Requires: xkbcomp = %{version}-%{release}
Requires: xkbcomp = %{version}-%{release}

%description dev
dev components for the xkbcomp package.


%package license
Summary: license components for the xkbcomp package.
Group: Default

%description license
license components for the xkbcomp package.


%package man
Summary: man components for the xkbcomp package.
Group: Default

%description man
man components for the xkbcomp package.


%prep
%setup -q -n xkbcomp-1.4.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559832529
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1559832529
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xkbcomp
cp COPYING %{buildroot}/usr/share/package-licenses/xkbcomp/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xkbcomp

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/xkbcomp.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xkbcomp/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xkbcomp.1
