#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : appdirs
Version  : 1.4.3
Release  : 45
URL      : http://pypi.debian.net/appdirs/appdirs-1.4.3.tar.gz
Source0  : http://pypi.debian.net/appdirs/appdirs-1.4.3.tar.gz
Summary  : A small Python module for determining appropriate platform-specific dirs, e.g. a "user data dir".
Group    : Development/Tools
License  : MIT
Requires: appdirs-license = %{version}-%{release}
Requires: appdirs-python = %{version}-%{release}
Requires: appdirs-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. image:: https://secure.travis-ci.org/ActiveState/appdirs.png
:target: http://travis-ci.org/ActiveState/appdirs

%package license
Summary: license components for the appdirs package.
Group: Default

%description license
license components for the appdirs package.


%package python
Summary: python components for the appdirs package.
Group: Default
Requires: appdirs-python3 = %{version}-%{release}

%description python
python components for the appdirs package.


%package python3
Summary: python3 components for the appdirs package.
Group: Default
Requires: python3-core

%description python3
python3 components for the appdirs package.


%prep
%setup -q -n appdirs-1.4.3
cd %{_builddir}/appdirs-1.4.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576007753
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/appdirs
cp %{_builddir}/appdirs-1.4.3/LICENSE.txt %{buildroot}/usr/share/package-licenses/appdirs/105885d8433c92e504e27d9134781d0c752e1166
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/appdirs/105885d8433c92e504e27d9134781d0c752e1166

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
