#
#    fty-scripts-rest - Scripts REST API
#
#    NOTE: This file was customized after generation, be sure to keep it
#
#    Copyright (C) 2014 - 2018 Eaton
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

# To build with draft APIs, use "--with drafts" in rpmbuild for local builds or add
#   Macros:
#   %_with_drafts 1
# at the BOTTOM of the OBS prjconf
%bcond_with drafts
%if %{with drafts}
%define DRAFTS yes
%else
%define DRAFTS no
%endif
Name:           fty-scripts-rest
Version:        1.0.0
Release:        1
Summary:        scripts rest api
License:        GPL-2.0+
URL:            https://42ity.org
Source0:        %{name}-%{version}.tar.gz
Group:          System/Libraries
# Note: ghostscript is required by graphviz which is required by
#       asciidoc. On Fedora 24 the ghostscript dependencies cannot
#       be resolved automatically. Thus add working dependency here!
BuildRequires:  ghostscript
BuildRequires:  asciidoc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xmlto
BuildRequires:  gcc-c++
BuildRequires:  cxxtools-devel
BuildRequires:  log4cplus-devel
BuildRequires:  fty-common-logging-devel
BuildRequires:  libsodium-devel
BuildRequires:  zeromq-devel
BuildRequires:  czmq-devel >= 3.0.2
BuildRequires:  malamute-devel >= 1.0.0
BuildRequires:  openssl-devel
BuildRequires:  fty-common-devel
BuildRequires:  fty-common-mlm-devel
BuildRequires:  tntnet-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  tntdb-devel
BuildRequires:  fty-common-db-devel
BuildRequires:  fty-common-rest-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
fty-scripts-rest scripts rest api.

%package -n libfty_scripts_rest1
Group:          System/Libraries
Summary:        scripts rest api shared library

%description -n libfty_scripts_rest1
This package contains shared library for fty-scripts-rest: scripts rest api

%post -n libfty_scripts_rest1 -p /sbin/ldconfig
%postun -n libfty_scripts_rest1 -p /sbin/ldconfig

# Note: the .so file is delivered as part of main package for tntnet to find it
%files -n libfty_scripts_rest1
%defattr(-,root,root)
%{_libdir}/libfty_scripts_rest.so.*
%{_libdir}/libfty_scripts_rest.so

%package devel
Summary:        scripts rest api
Group:          System/Libraries
Requires:       libfty_scripts_rest1 = %{version}
Requires:       cxxtools-devel
Requires:       log4cplus-devel
Requires:       fty-common-logging-devel
Requires:       libsodium-devel
Requires:       zeromq-devel
Requires:       czmq-devel >= 3.0.2
Requires:       malamute-devel >= 1.0.0
Requires:       openssl-devel
Requires:       fty-common-devel
Requires:       fty-common-mlm-devel
Requires:       tntnet-devel
Requires:       cyrus-sasl-devel
Requires:       tntdb-devel
Requires:       fty-common-db-devel
Requires:       fty-common-rest-devel

%description devel
scripts rest api development tools
This package contains development files for fty-scripts-rest: scripts rest api

# Note: the .so file is delivered as part of main package for tntnet to find it
%files devel
%defattr(-,root,root)
%{_includedir}/*
###%{_libdir}/libfty_scripts_rest.so
%{_libdir}/libfty_scripts_rest.so
%{_libdir}/pkgconfig/libfty_scripts_rest.pc
%{_mandir}/man3/*
%{_mandir}/man7/*

%prep

%setup -q

%build
sh autogen.sh
%{configure} --enable-drafts=%{DRAFTS}
make %{_smp_mflags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}

# remove static libraries
find %{buildroot} -name '*.a' | xargs rm -f
find %{buildroot} -name '*.la' | xargs rm -f


%changelog
