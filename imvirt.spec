#
# Conditional build:
%bcond_with	tests		# build with tests

Summary:	Detects several virtualizations
Name:		imvirt
Version:	0.9.6
Release:	1
Source0:	http://downloads.sourceforge.net/imvirt/%{name}-%{version}.tar.gz
# Source0-md5:	792d986e79d763a44b55c33a17abb62d
License:	GPL v2+
Group:		Applications/System
URL:		http://micky.ibh.net/~liske/imvirt.html
BuildRequires:	perl-ExtUtils-MakeMaker
Requires:	dmidecode
ExclusiveArch:	%{ix86} %{x8664} ia64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This little Perl script tries to detect if it is called from within a
virtualization container. This is detected by looking for well known
boot messages, directories and reading DMI (Desktop Management
Interface) data.

The following containers are detected:
- Virtual PC/Virtual Server
- VirtualBox
- VMware
- QEMU/KVM (experimental)
- Xen (para and non-para virtualized)
- OpenVZ/Virtuozzo
- UML
- any HVM providing CPUID 0x40000000 detection
- lguest
- ARAnyM
- LXC

%prep
%setup -q

%build
%configure
%{__make}

%if %{with tests}
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{perl_vendorarch}/auto/ImVirt/.packlist
rm $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
rm $RPM_BUILD_ROOT%{perl_vendorlib}/ImVirt.pm.in

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_sbindir}/imvirt-report
%attr(755,root,root) %{_bindir}/imvirt
%dir %{_libexecdir}/imvirt
%attr(755,root,root) %{_libdir}/%{name}/hvm
%attr(755,root,root) %{_libdir}/%{name}/hyperv
%attr(755,root,root) %{_libdir}/%{name}/pillbox
%attr(755,root,root) %{_libdir}/%{name}/vmware
%attr(755,root,root) %{_libdir}/%{name}/xen
%{_mandir}/man1/imvirt-report.1*
%{_mandir}/man1/imvirt.1*

# perl-ImVirt
%{perl_vendorlib}/ImVirt.pm
%{perl_vendorlib}/ImVirt
%{_mandir}/man3/ImVirt.3pm*
