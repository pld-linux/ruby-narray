Summary:	Numerical Ruby
Summary(pl):	Numeryczny Ruby
Name:		ruby-NArray
Version:	0.5.7p4
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://www.ir.isas.ac.jp/~masa/ruby/dist/narray-%{version}.tar.gz
# Source0-md5:	6c6a5b680b91514e37992c92c74cf5ea
URL:		http://www.ir.isas.ac.jp/~masa/ruby/index-e.html
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NArray is a class of Numerical N-dimensional Array, whose elements are
1/2/4-byte Integer, single/double-prec Real/Complex, and Ruby Object.
This extension library incorporates fast calculation and easy
manipulation of large numerical arrays into the Ruby language. NArray
has features similar to NumPy, but NArray has vector and matrix
subclasses.

%description -l pl
NArray to klasa numerycznej N-wymiarowej tablicy, której elementami s±
1/2/4-bajtowy Integer, pojedynczej/podwójnej precyzji Real/Complex
oraz Ruby Object. Ta biblioteka rozszerzenia w³±cza do jêzyka Ruby
szybkie obliczenia oraz ³atwe operacjami na du¿ych tablicach
numerycznych. NArray ma mo¿liwo¶ci podobne do NumPy, ale Narray ma
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

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%{ruby_rubylibdir}/n*.rb
%attr(755,root,root) %{ruby_archdir}/narray.so
%{ruby_ridir}/NArray
