#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC7125C934883BE5 (me@adamj.eu)
#
Name     : pytest-randomly
Version  : 3.5.0
Release  : 24
URL      : https://files.pythonhosted.org/packages/b5/10/3ab5171daca93c8fe6354daa99d6674fc08c0d8589a0ddc4f5bfa7ae7c08/pytest-randomly-3.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b5/10/3ab5171daca93c8fe6354daa99d6674fc08c0d8589a0ddc4f5bfa7ae7c08/pytest-randomly-3.5.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/b5/10/3ab5171daca93c8fe6354daa99d6674fc08c0d8589a0ddc4f5bfa7ae7c08/pytest-randomly-3.5.0.tar.gz.asc
Summary  : Pytest plugin to randomly order tests and control random.seed.
Group    : Development/Tools
License  : MIT
Requires: pytest-randomly-python = %{version}-%{release}
Requires: pytest-randomly-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
pytest-randomly
        ===============

%package python
Summary: python components for the pytest-randomly package.
Group: Default
Requires: pytest-randomly-python3 = %{version}-%{release}

%description python
python components for the pytest-randomly package.


%package python3
Summary: python3 components for the pytest-randomly package.
Group: Default
Requires: python3-core
Provides: pypi(pytest_randomly)
Requires: pypi(pytest)

%description python3
python3 components for the pytest-randomly package.


%prep
%setup -q -n pytest-randomly-3.5.0
cd %{_builddir}/pytest-randomly-3.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605543562
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
