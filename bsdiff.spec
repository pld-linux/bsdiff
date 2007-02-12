Summary:	Binary diff/patch utilities
Summary(pl.UTF-8):	Narzędzia diff/patch dla plików binarnych
Name:		bsdiff
Version:	4.3
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	http://www.daemonology.net/bsdiff/%{name}-%{version}.tar.gz
# Source0-md5:	e6d812394f0e0ecc8d5df255aa1db22a
URL:		http://www.daemonology.net/bsdiff/
BuildRequires:	bzip2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bsdiff and bspatch are tools for building and applying patches to
binary files. By using suffix sorting (specifically, Larsson and
Sadakane's qsufsort) and taking advantage of how executable files
change, bsdiff routinely produces binary patches 50-80% smaller than
those produced by Xdelta, and 15% smaller than those produced by
.RTPatch.

%description -l pl.UTF-8
bsdiff i bspatch to narzędzia do tworzenia i aplikowania łat dla
plików binarnych. Dzięki użyciu sortowania przyrostkowego (w
szczególności qsufsort Larssona i Sadakane'a) i uwzględnieniu sposobu,
w jaki zmieniają się pliki wykonywalne, bsdiff zwykle tworzy łaty
binarne 50-80%% mniejsze niż tworzone przez program Xdelta i 15%%
mniejsze niż tworzone przez .RTPatch.

%prep
%setup -q

%build
%{__cc} bsdiff.c  -o bsdiff  %{rpmcflags} -lbz2
%{__cc} bspatch.c -o bspatch %{rpmcflags} -lbz2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install bsdiff bspatch $RPM_BUILD_ROOT%{_bindir}
install bsdiff.1 bspatch.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
