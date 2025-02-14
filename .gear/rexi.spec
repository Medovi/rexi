%define _unpackaged_files_terminate_build 1

Name:       rexi
Version:    1.2.0
Release:    alt1
BuildArch:  noarch

License:    MIT
Group:      Terminal
Summary:    Terminal UI for Regex Testing

Url:        https://github.com/royreznik/rexi
Source:     %name-%version.tar
Patch:      %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry
Requires:   python3-module-textual
Requires:   python3-module-colorama
Requires:   python3-module-typer
Requires:   python3-module-%name

%description
Rexi is a simple yet powerful CLI tool designed for developers,
data scientists, and anyone interested in working with regular
expressions directly from the terminal. Built with Python and
leveraging the textual library, rexi offers a user-friendly terminal
UI to interactively work with regular expressions.

%package -n python3-module-%name
Group:      Other
Summary:    Python module for rexi.
BuildArch:  noarch

%description -n python3-module-%name
Rexi is a simple yet powerful CLI tool designed for developers,
data scientists, and anyone interested in working with regular
expressions directly from the terminal. Built with Python and
leveraging the textual library, rexi offers a user-friendly terminal
UI to interactively work with regular expressions.

Package contains python module for %name.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.*
%_bindir/%name

%files -n python3-module-%name
%python3_sitelibdir/*

%changelog
* Mon Feb 10 2025 Sergey Savelev <savelevsa@basealt.ru> 1.2.0-alt1
- Initial build for Sisyphus

