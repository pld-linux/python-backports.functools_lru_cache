#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

%define		pypi_name	backports.functools_lru_cache

Summary:	Backport of functools.lru_cache from Python 3.3
Summary(pl.UTF-8):	Backport functools.lru_cache z Pythona 3.3
Name:		python-%{pypi_name}
Version:	1.6.4
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/backports.functools_lru_cache/
Source0:	https://files.pythonhosted.org/packages/source/b/backports.functools_lru_cache/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	8fed424f30bf9554235aa02997b7574c
URL:		https://github.com/jaraco/backports.functools_lru_cache
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm >= 3.4.1
BuildRequires:	python-toml
%if %{with tests}
BuildRequires:	python-pytest >= 4.6
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-jaraco.packaging >= 8.2
BuildRequires:	python3-rst.linker >= 1.9
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python-backports
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Backport of functools.lru_cache from Python 3.3.

%description
Backport functools.lru_cache z Pythona 3.3.

%package apidocs
Summary:	API documentation for Python backports.functools_lru_cache module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona backports.functools_lru_cache
Group:		Documentation

%description apidocs
API documentation for Python backports.functools_lru_cache module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona backports.functools_lru_cache.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif

%if %{with doc}
cd docs
sphinx-build-3 -b html . _build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/backports/__init__.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py_sitescriptdir}/backports/functools_lru_cache.py[co]
%{py_sitescriptdir}/%{pypi_name}-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
