%define debug_package %{nil}
%global pkgname smartctl_exporter
%{!?pkgrevision: %global pkgrevision 1}
%if 0%{?rhel} == 8
 %define dist .el8
%endif

Name:          %{pkgname}
Version:       %{pkgversion}
Release:       %{pkgrevision}%{?dist}
Summary:       Smartctl Prometheus exporter
License:       Apache License 2.0
URL:           https://github.com/prometheus-community/smartctl_exporter

Source0:       smartctl_exporter-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Obsoletes:     smartctl_exporter

%description
[Use with BlueBanquise] Export smartctl statistics to prometheus.

%prep
%setup -n smartctl_exporter-%{version}.linux-amd64

%build

%pre

%install
%{__install} -d -m 755 %{buildroot}/etc/%{name}

%{__install} -D -m 755 smartctl_exporter %{buildroot}/usr/local/bin/smartctl_exporter

%files
%defattr(-,root,root,-)
%attr(-, root, root) /usr/local/bin/smartctl_exporter

%changelog
* Wed Nov 17 2022 Thomas Bourcey <sckyzo@gmail.com> - 1.0.0
- Initial packaging
