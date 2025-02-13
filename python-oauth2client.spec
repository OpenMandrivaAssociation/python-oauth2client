Name:		python-oauth2client
Version:	4.1.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/o/oauth2client/oauth2client-%{version}.tar.gz
Summary:	OAuth 2.0 client library
URL:		https://pypi.org/project/oauth2client/
License:	Apache 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
OAuth 2.0 client library

%files
%{py_sitedir}/oauth2client
%{py_sitedir}/oauth2client-*.*-info
