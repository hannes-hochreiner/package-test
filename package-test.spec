# Generated by rust2rpm 16
%bcond_without check
%global __cargo_skip_build 0

%global crate package-test

Name:           rust-%{crate}
Version:        0.1.0
Release:        1%{?dist}
Summary:        A packaging test

# Upstream license specification: None
License:        MIT

URL:            https://github.com/hannes-hochreiner/package-test
Source:         _service:obs_scm:%{name}-%{version}.obscpio # %{crates_source}

#ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%doc README.md
%{_bindir}/package-test

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
