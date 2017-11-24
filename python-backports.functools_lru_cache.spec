#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pypi_name	backports.functools_lru_cache

Summary:	Backport of functools.lru_cache from Python 3.3
Name:		python-%{pypi_name}
Version:	1.4
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	b954e7d5e2ca0f0f66ad2ed12ba800e5
URL:		https://github.com/jaraco/backports.functools_lru_cache
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-backports
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Backport of functools.lru_cache from Python 3.3.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

rm $RPM_BUILD_ROOT%{py_sitescriptdir}/backports/__init__.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%{py_sitescriptdir}/backports/functools_lru_cache.py[co]
%{py_sitescriptdir}/%{pypi_name}-%{version}-py*.egg-info
