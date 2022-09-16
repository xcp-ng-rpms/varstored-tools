Name:           varstored-tools
Version:        1.0.0
Release:        2%{?dist}
Summary:        Variables store for UEFI guests
License:        BSD
URL:            https://github.com/xapi-project/varstored
Source0:        https://github.com/xapi-project/varstored/archive/v%{version}/varstored-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libxml2-devel
BuildRequires:  libseccomp-devel
BuildRequires:  openssl-devel

%description
Command-line utilities for varstored/uefistored

%prep
%autosetup -p1 -n varstored-%{version}

%build
make tools
make create-auth

%install
install -d %{buildroot}%{_bindir}
install -m 0755 tools/varstore-get %{buildroot}%{_bindir}/
install -m 0755 tools/varstore-ls %{buildroot}%{_bindir}/
install -m 0755 tools/varstore-rm %{buildroot}%{_bindir}/
install -m 0755 tools/varstore-sb-state %{buildroot}%{_bindir}/
install -m 0755 tools/varstore-set %{buildroot}%{_bindir}/
install -d %{buildroot}/opt/xensource/libexec
install -m 0755 create-auth %{buildroot}/opt/xensource/libexec/

%files
%doc LICENSE
%{_bindir}/varstore-get
%{_bindir}/varstore-ls
%{_bindir}/varstore-rm
%{_bindir}/varstore-sb-state
%{_bindir}/varstore-set
/opt/xensource/libexec/create-auth

%changelog
* Fri Sep 16 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0.0-2
- Rebuild for XCP-ng 8.3 alpha

* Mon Jan 24 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0.0-1
- Update to 1.0.0
- Drop varstored-0.9.1-sb-state-only-load-auth-data-if-needed.XCP-ng.patch merged upstream

* Thu Jul 15 2021 Bobby Eshleman <bobbyeshleman@gmail.com> - 0.9.1-1.2
- Update varstored-0.9.1-sb-state-only-load-auth-data-if-needed.XCP-ng.patch
- Updated to upstream version of the patch after PR merge
- Renamed to varstored-0.9.1-sb-state-only-load-auth-data-if-needed.backport.patch

* Mon Jun 28 2021 Bobby Eshleman <bobbyeshleman@gmail.com> - 0.9.1-1.1
- Change varstore-sb-state setup to not load auth data
- Patch varstored-0.9.1-sb-state-only-load-auth-data-if-needed.XCP-ng.patch added

* Wed Nov 25 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 0.9.1-1
- Initial XCP-ng build
