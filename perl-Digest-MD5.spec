%define upstream_name    Digest-MD5
%define upstream_version 2.55

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:     MD5 message digest algorithm
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Digest/Digest-MD5-%{upstream_version}.tar.gz

BuildRequires: perl(Digest::base)
BuildRequires: perl(File::Spec)
BuildRequires: perl(XSLoader)
BuildRequires: perl-devel

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

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorarch/*
