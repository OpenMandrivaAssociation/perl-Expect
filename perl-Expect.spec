%define upstream_name    Expect
%define upstream_version 1.21

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

Summary:    Expect for Perl
License:    GPL
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Expect/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:     %{name}-paths.patch

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(IO::Tty) >= 1.02
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
# temporary dep due to the perl-5.14 bump
BuildRequires:  perl-IO-Tty >= 1.100.0-3

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
%setup -q -n %{upstream_name}-%{upstream_version}

%patch0 -p1
perl -pi -e 's|/usr/local/bin/perl|%{__perl}|' examples/kibitz/kibitz

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README examples tutorial
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/*.pod
%{_mandir}/*/*

