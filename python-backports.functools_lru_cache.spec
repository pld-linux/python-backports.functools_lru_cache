#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

%define		pypi_name	backports.functools_lru_cache

Summary:	Backport of functools.lru_cache from Python 3.3
Summary(pl.UTF-8):	Backport functools.lru_cache z Pythona 3.3
Name:		python-%{pypi_name}
Version:	1.5
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/backports.functools_lru_cache/
Source0:	https://files.pythonhosted.org/packages/source/b/backports.functools_lru_cache/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	20f53f54cd3f04b3346ce75a54959754
URL:		https://github.com/jaraco/backports.functools_lru_cache
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm >= 1.15.0
%if %{with tests}
BuildRequires:	python-pytest >= 2.8
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-jaraco.packaging >= 3.2
BuildRequires:	python-rst.linker
BuildRequires:	sphinx-pdg-2
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
%{__python} -m pytest tests
%endif

%if %{with doc}
cd docs
sphinx-build-2 -b html . _build/html
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
