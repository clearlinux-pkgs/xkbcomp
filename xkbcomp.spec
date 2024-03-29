#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v3
# autospec commit: 750e50d
#
# Source0 file verified with key 0xCFDF148828C642A7 (alanc@freedesktop.org)
#
Name     : xkbcomp
Version  : 1.4.7
Release  : 21
URL      : https://www.x.org/releases/individual/app/xkbcomp-1.4.7.tar.gz
Source0  : https://www.x.org/releases/individual/app/xkbcomp-1.4.7.tar.gz
Source1  : https://www.x.org/releases/individual/app/xkbcomp-1.4.7.tar.gz.sig
Summary  : XKB keymap compiler
Group    : Development/Tools
License  : HPND
Requires: xkbcomp-bin = %{version}-%{release}
Requires: xkbcomp-license = %{version}-%{release}
Requires: xkbcomp-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n xkbcomp-1.4.7
cd %{_builddir}/xkbcomp-1.4.7
pushd ..
cp -a xkbcomp-1.4.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707156373
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1707156373
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xkbcomp
cp %{_builddir}/xkbcomp-%{version}/COPYING %{buildroot}/usr/share/package-licenses/xkbcomp/67b69067a1b7bf806fbe7a83fd01884393c15fe0 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/xkbcomp
/usr/bin/xkbcomp

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/xkbcomp.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xkbcomp/67b69067a1b7bf806fbe7a83fd01884393c15fe0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xkbcomp.1
