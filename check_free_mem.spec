%define version          1.2.0
%define release          1
%define sourcename       check_free_mem
%define packagename      nagios-plugins-check-free-mem
%define nagiospluginsdir %{_libdir}/nagios/plugins

# No binaries in this package
%define debug_package    %{nil}

Summary:    Nagios plugin that checks the amount of free physical memory
Name:       %{packagename}
Obsoletes:  check_free_mem <= 100
Version:    %{version}
Release:    %{release}%{?dist}
License:    GPLv3+
Packager:   Matteo Corti <matteo@corti.li>
Group:      Applications/System
BuildRoot:  %{_tmppath}/%{packagename}-%{version}-%{release}-root-%(%{__id_u} -n)
URL:        https://trac.id.ethz.ch/projects/nagios_plugins/wiki/check_free_mem
Source:     http://www.id.ethz.ch/people/allid_list/corti/%{sourcename}-%{version}.tar.gz

# Fedora build requirement (not needed for EPEL{4,5})
BuildRequires: perl(ExtUtils::MakeMaker)

Requires:      nagios-plugins
Requires:      perl(Readonly)

%description
check_free_mem is a Nagios plugin that checks the amount of free physical memory

%prep
%setup -q -n %{sourcename}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor \
    INSTALLSCRIPT=%{nagiospluginsdir} \
    INSTALLVENDORSCRIPT=%{nagiospluginsdir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name "*.pod" -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS Changes NEWS README.md TODO COPYING COPYRIGHT
%{nagiospluginsdir}/%{sourcename}
%{_mandir}/man1/%{sourcename}.1*

%changelog
* Fri Jun 26 2020 Matteo Corti <matteo@corti.li> - 1.2.0-1
- Added dependency to Readonly

* Mon Nov 25 2019 Matteo Corti <matteo@corti.li> - 1.2.0-0
- Updated to 1.2.0

* Tue Nov  1 2016 Matteo Corti <matteo@corti.li> - 1.1.2-1
- Updated to 1.1.2

* Sun Mar 15 2015 Matteo Corti <matteo.corti@id.ethz.ch> - 1.1.1-1
- Updated to 1.1.1

* Sun Mar 15 2015 Matteo Corti <matteo.corti@id.ethz.ch> - 1.1.0-1
- Updated to 1.1.0

* Mon Apr 18 2011 Matteo Corti <matteo.corti@id.ethz.ch> - 1.0.1-0
New package name, several fixes

* Thu Mar 20 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.11.3-0
- ePN compatibility

* Sun Jan 13 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.11.0-0
- updated to 0.11.0, --free can be used to specify the path of 'free'

* Sun Jan 13 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.10.0-0
- updated to 0.10.0 with --swap to monitor swap space

* Wed Jan  9 2008 Matteo Corti <matteo.corti@id.ethz.ch> - 0.9.0-0
- Initial revision

