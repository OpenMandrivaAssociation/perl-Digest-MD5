%define upstream_name    Digest-MD5
%define upstream_version 2.53

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:     MD5 message digest algorithm
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Digest/Digest-MD5-%{upstream_version}.tar.gz

BuildRequires: perl(Digest::base)
BuildRequires: perl(File::Spec)
BuildRequires: perl(XSLoader)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The 'Digest::MD5' module allows you to use the RSA Data Security Inc. MD5
Message Digest algorithm from within Perl programs. The algorithm takes as
input a message of arbitrary length and produces as output a 128-bit
"fingerprint" or "message digest" of the input.

Note that the MD5 algorithm is not as strong as it used to be. It has since
2005 been easy to generate different messages that produce the same MD5
digest. It still seems hard to generate messages that produce a given
digest, but it is probably wise to move to stronger algorithms for
applications that depend on the digest to uniquely identify a message.

The 'Digest::MD5' module provide a procedural interface for simple use, as
well as an object oriented interface that can handle messages of arbitrary
length and which can read files directly.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 2.510.0-2mdv2011.0
+ Revision: 681422
- mass rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 2.51

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 2.400.0-3mdv2011.0
+ Revision: 562421
- rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.400.0-2mdv2011.0
+ Revision: 555796
- rebuild for perl 5.12

* Mon Jul 12 2010 Jérôme Quelin <jquelin@mandriva.org> 2.400.0-1mdv2011.0
+ Revision: 551219
- update to 2.40

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 2.390.0-1mdv2010.0
+ Revision: 395357
- import perl-Digest-MD5


* Sun Jul 12 2009 cpan2dist 2.39-1mdv
- initial mdv release, generated with cpan2dist

