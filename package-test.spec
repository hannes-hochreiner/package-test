Name: package-test
Summary: Package test
License: MIT
Version: 1.0.0
Release: 1%{?dist}
Requires: cargo

%description

%prep
%autosetup -n %{name}-%{version_no_tilde} -p1
ls .
ls /home/abuild/rpmbuild/SOURCES

%install

%post

%files
