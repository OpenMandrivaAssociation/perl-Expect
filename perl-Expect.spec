%define modname	Expect
%define modver 1.32

Summary:	Expect for Perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	5
License:	GPLv2
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/%{modname}/%{modname}-%{modver}.tar.gz
Patch0:	%{name}-paths.patch
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires: perl(Test::Exception)
BuildRequires:	perl(IO::Tty) >= 1.02
BuildRequires:  bc
# temporary dep due to the perl-5.14 bump
BuildRequires:	perl-List-MoreUtils >= 0.320.0-4

%description
The Expect module is a successor of Comm.pl and a descendent of Chat.pl. It
more closely ressembles the Tcl Expect language than its predecessors. It does
not contain any of the networking code found in Comm.pl. I suspect this would
be obsolete anyway given the advent of IO::Socket and external tools such as
netcat.

Expect.pm is an attempt to have more of a switch() & case feeling to make
decision processing more fluid. Three separate types of debugging have been
implemented to make code production easier.

It is now possible to interconnect multiple file handles (and processes) much
like Tcl's Expect. An attempt was made to enable all the features of Tcl's
Expect without forcing Tcl on the victim programmer :-) .

%prep
%setup -qn %{modname}-%{modver}
%autopatch -p1
perl -pi -e 's|/usr/local/bin/perl|%{__perl}|' examples/kibitz/kibitz

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes  examples tutorial
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
