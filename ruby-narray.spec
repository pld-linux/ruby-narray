%define pkgname narray
Summary:	Numerical Ruby
Summary(pl.UTF-8):	Numeryczny Ruby
Name:		ruby-%{pkgname}
Version:	0.5.7p4
Release:	2
License:	Ruby's
Group:		Development/Languages
Source0:	http://www.ir.isas.ac.jp/~masa/ruby/dist/%{pkgname}-%{version}.tar.gz
# Source0-md5:	6c6a5b680b91514e37992c92c74cf5ea
URL:		http://www.ir.isas.ac.jp/~masa/ruby/index-e.html
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
Obsoletes:	ruby-NArray
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NArray is a class of Numerical N-dimensional Array, whose elements are
1/2/4-byte Integer, single/double-prec Real/Complex, and Ruby Object.
This extension library incorporates fast calculation and easy
manipulation of large numerical arrays into the Ruby language. NArray
has features similar to NumPy, but NArray has vector and matrix
subclasses.

%description -l pl.UTF-8
NArray to klasa numerycznej N-wymiarowej tablicy, której elementami są
1/2/4-bajtowy Integer, pojedynczej/podwójnej precyzji Real/Complex
oraz Ruby Object. Ta biblioteka rozszerzenia włącza do języka Ruby
szybkie obliczenia oraz łatwe operacjami na dużych tablicach
numerycznych. NArray ma możliwości podobne do NumPy, ale Narray ma
podklasy vector i matrix.

%prep
%setup -q -n narray-%{version}

%build
ruby extconf.rb
%{__make}
rdoc --op rdoc *.c
rdoc --ri --op ri *.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

%{__make} install \
	archdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	rubylibdir=$RPM_BUILD_ROOT%{ruby_rubylibdir} \
	sitelibdir=$RPM_BUILD_ROOT%{ruby_rubylibdir}

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%{ruby_rubylibdir}/n*.rb
%attr(755,root,root) %{ruby_archdir}/narray.so
%{ruby_ridir}/NArray
