Name:		texlive-catcodes
Epoch:		1
Version:	38859
Release:	1
Summary:	Generic handling of TeX category codes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/catcodes
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catcodes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catcodes.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catcodes.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle deals with category code switching; the packages of
the bundle should work with any TeX format (with the support of
the plainpkg package). The bundle provides: - stacklet.sty,
which supports stacks that control the use of different
catcodes; - actcodes.sty, which deals with active characters;
and - catchdq.sty, which provides a simple quotation character
control mechanism.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/catcodes/actcodes.sty
%{_texmfdistdir}/tex/generic/catcodes/catchdq.sty
%{_texmfdistdir}/tex/generic/catcodes/catcodes.RLS
%{_texmfdistdir}/tex/generic/catcodes/stacklet.sty
%doc %{_texmfdistdir}/doc/generic/catcodes/README
%doc %{_texmfdistdir}/doc/generic/catcodes/SrcFILEs.txt
%doc %{_texmfdistdir}/doc/generic/catcodes/catcodes.pdf
#- source
%doc %{_texmfdistdir}/source/generic/catcodes/catcodes.tex
%doc %{_texmfdistdir}/source/generic/catcodes/fdatechk.tex
%doc %{_texmfdistdir}/source/generic/catcodes/makedoc.cfg
%doc %{_texmfdistdir}/source/generic/catcodes/mdoccorr.cfg
%doc %{_texmfdistdir}/source/generic/catcodes/srcfiles.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
