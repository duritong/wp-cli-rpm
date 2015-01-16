Name:		wp-cli
Version:	0.18.0
Release:	1%{?dist}
Summary:	A Wordpress CLI

Group:		Applications/Internet
License:	MIT
URL:		http://wp-cli.org
Source0:	https://github.com/wp-cli/wp-cli/releases/download/v%{version}/wp-cli-%{version}.phar

Requires:	php-cli

%description
A Wordpress CLI


%prep



%build

%install
install -D -m 0755 -p %{SOURCE0} %{buildroot}/%{_libexecdir}/%{name}/wp-cli.phar
mkdir -p %{buildroot}/%{_bindir}
echo -e "#!/bin/bash\nphp -d suhosin.executor.include.whitelist=phar %{_libexecdir}/%{name}/wp-cli.phar \"\$@\"\n" > %{buildroot}/%{_bindir}/wp-cli
chmod +x %{buildroot}/%{_bindir}/wp-cli


%files
%{_libexecdir}/%{name}
%{_bindir}/wp-cli


%changelog

* Fri Jan 16 2015 mh <mh@immerda.ch> - 0.18.0
- Initial spec file
