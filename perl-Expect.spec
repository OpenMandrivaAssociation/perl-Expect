%define upstream_name    Expect
%define upstream_version 1.21

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Expect for Perl
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Expect/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		%{name}-paths.patch

BuildRequires:	perl-devel
BuildRequires:	perl(IO::Tty) >= 1.02
BuildArch:		noarch

# temporary dep due to the perl-5.14 bump
BuildRequires:	perl-List-MoreUtils >= 0.320.0-4
BuildRequires:	perl-IO-Tty >= 1.100.0-3

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
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README examples tutorial
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/*.pod
%{_mandir}/*/*



%changelog
* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.210.0-4mdv2012.0
+ Revision: 763243
- force it
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.210.0-3
+ Revision: 667131
- mass rebuild

  + JÃ©rÃ´me Quelin <jquelin@mandriva.org>
    - rebuild

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.210.0-1mdv2010.1
+ Revision: 403162
- rebuild using %%perl_convert_version

* Sun Mar 22 2009 Funda Wang <fwang@mandriva.org> 1.21-3mdv2009.1
+ Revision: 360219
- fix patch num

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.21-3mdv2009.0
+ Revision: 223693
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.21-2mdv2008.1
+ Revision: 180395
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.21-1mdv2008.0
+ Revision: 63955
- update to new version 1.21


* Wed Aug 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2007.0
- New version 1.20

* Sun Jul 16 2006 Emmanuel Andry <eandry@mandriva.org> 1.18-1mdv2007.0
- New release 1.18

* Tue Jun 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.17-1mdv2007.0
- New release 1.17

* Mon May 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.16-1mdv2007.0
- New release 1.16
- better summary & description
- spec cleanup

* Thu Feb 03 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.15-7mdk
- rebuild

* Wed Aug 13 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.15-6mdk
- rebuild for new perl
- rm -rf /home/guillomovitch/rpm/tmp/perl-Expect-1.20 in %%install, not %%prep
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro

