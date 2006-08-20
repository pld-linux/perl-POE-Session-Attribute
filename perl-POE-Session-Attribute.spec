#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Session-Attribute
Summary:	POE::Session::Attribute - use attributes to define your POE Sessions
Summary(pl):	POE::Session::Attribute - definiowanie sesji POE z u¿yciem atrybutów
Name:		perl-POE-Session-Attribute
Version:	0.80
Release:	0.1
# "same as perl 5.8.7 or any later perl 5"
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a7fda22ae8b59cac410c1b688541abd6
URL:		http://search.cpan.org/dist/POE-Session-Attribute/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-POE
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module's purpose is to save you some boilerplate code around
POE::Session->create() method. Just inherit your class from
POE::Session::Attribute and define some states using attributes.
Method "spawn()" in your package will be provided by
POE::Session::Attribute (of course, you can override it, if any).
POE::Session::Attribute tries to be reasonably compatible with
POE::Session::AttributeBased. As for now, all material test cases from
POE::Session::AttributeBased distribution v0.03 run without errors
with POE::Session::Attribute.

%description -l pl
Celem tego modu³u jest oszczêdzenie pisania czê¶ci kodu wokó³ metody
POE::Session->create(). Wystarczy odziedziczyæ klasê z
POE::Session::Attribute i zdefiniowaæ trochê stanów przy u¿yciu
atrybutów. Metoda "spawn()" bêdzie dostarczona przez
POE::Session::Attribute (oczywi¶cie mo¿na j± przeci±¿yæ).
POE::Session::Attribute próbuje byæ w miarê kompatybilny z
POE::Session::AttributeBased. Jak na razie wszystkie przypadki testowe
z dystrybucji POE::Session::AttributeBased 0.03 dzia³aj± bez b³êdów z
POE::Session::Attribute.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/POE/Session/Attribute.pm
%{_mandir}/man3/*
