#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%define		pdir	Gtk2
%define		pnam	SourceView
Summary:	Perl gtksourceview bindings
Summary(pl.UTF-8):	Wiązania gtksourceview dla Perla
Name:		perl-Gtk2-SourceView
Version:	1.013
Release:	1
License:	LGPL v2+
Group:		Development/Languages/Perl
Source0:	https://downloads.sourceforge.net/gtk2-perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	91e0878718f3f13815c66935ba77ab0f
Patch0:		%{name}-build.patch
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	gtksourceview-devel >= 1.7.2
BuildRequires:	perl-ExtUtils-Depends >= 0.205
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.07
BuildRequires:	perl-Glib-devel >= 1.132
BuildRequires:	perl-Gnome2-Print-devel >= 0.951
BuildRequires:	perl-Gtk2-devel >= 1.133
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Requires:	perl-Glib >= 1.132
Requires:	perl-Gnome2-Print >= 0.951
Requires:	perl-Gtk2 >= 1.133
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides Perl access to gtksourceview library.

Note: this module is deprecated and no longer maintained.

%description -l pl.UTF-8
Ten moduł daje dostęp z poziomu Perla do biblioteki gtksourceview.

Uwaga: ten moduł jest przestarzały i nie jest już utrzymywany.

%package devel
Summary:	Development files for Perl Gtk2-SourceView bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań Gtk2-SourceView dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	gtksourceview-devel >= 1.7.2
Requires:	perl-Cairo-devel
Requires:	perl-Glib-devel >= 1.132
Requires:	perl-Gnome2-Print-devel >= 0.951
Requires:	perl-Gtk2-devel >= 1.133

%description devel
Development files for Perl Gtk2-SourceView bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Gtk2-SourceView dla Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%{__rm} xs/GtkSourcePrintJob.xs

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Gtk2/SourceView/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%{perl_vendorarch}/Gtk2/SourceView.pm
%dir %{perl_vendorarch}/Gtk2/SourceView
%dir %{perl_vendorarch}/auto/Gtk2/SourceView
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk2/SourceView/SourceView.so
%{_mandir}/man3/Gtk2::SourceView*.3pm*

%files devel
%defattr(644,root,root,755)
%{perl_vendorarch}/Gtk2/SourceView/Install
