#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Gtk2
%define		pnam	SourceView
Summary:	Perl gtksourceview bindings
Summary(pl.UTF-8):   Wiązania gtksourceview dla Perla
Name:		perl-Gtk2-SourceView
Version:	1.000
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	35f859153d9c8a41260f98ad969fcb78
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	gtksourceview-devel >= 1.7.2
BuildRequires:	perl-ExtUtils-Depends >= 0.205
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.07
BuildRequires:	perl-Glib >= 1.132
BuildRequires:	perl-Gnome2-Print >= 0.951
BuildRequires:	perl-Gtk2 >= 1.133
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Glib >= 1.132
Requires:	perl-Gnome2-Print >= 0.951
Requires:	perl-Gtk2 >= 1.133
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides Perl access to gtksourceview library.

%description -l pl.UTF-8
Ten moduł daje dostęp z poziomu Perla do biblioteki gtksourceview.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Gtk2/SourceView/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%{perl_vendorarch}/Gtk2/SourceView.pm
%dir %{perl_vendorarch}/Gtk2/SourceView
%{perl_vendorarch}/Gtk2/SourceView/Install
%dir %{perl_vendorarch}/auto/Gtk2/SourceView
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/SourceView/*.so
%{perl_vendorarch}/auto/Gtk2/SourceView/*.bs
%{_mandir}/man3/*
