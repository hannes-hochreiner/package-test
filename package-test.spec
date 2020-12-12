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
cargo build --release

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp target/release/%{name} $RPM_BUILD_ROOT%{_bindir}

%files
%{_bindir}/%{name}
