#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : appdirs
Version  : 1.4.3
Release  : 16
URL      : http://pypi.debian.net/appdirs/appdirs-1.4.3.tar.gz
Source0  : http://pypi.debian.net/appdirs/appdirs-1.4.3.tar.gz
Summary  : A small Python module for determining appropriate platform-specific dirs, e.g. a "user data dir".
Group    : Development/Tools
License  : MIT
Requires: appdirs-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
.. image:: https://secure.travis-ci.org/ActiveState/appdirs.png
:target: http://travis-ci.org/ActiveState/appdirs

%package python
Summary: python components for the appdirs package.
Group: Default

%description python
python components for the appdirs package.


%prep
%setup -q -n appdirs-1.4.3

%build
export LANG=C
export SOURCE_DATE_EPOCH=1488896867
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
export SOURCE_DATE_EPOCH=1488896867
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
