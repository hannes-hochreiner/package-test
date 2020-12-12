Name: package-test
Summary: Package test
License: MIT
Version: 1.0.0
Release: 1%{?dist}
Source: %{name}-%{version}.tar.xz
BuildRequires: cargo

%description

%prep
%autosetup -n %{name}-%{version_no_tilde} -p1
ls .
ls /home/abuild/rpmbuild/SOURCES

%build
cd /home/abuild/rpmbuild/SOURCES/%{name}-%{version_no_tilde}; cargo build

%install

%post

%files
