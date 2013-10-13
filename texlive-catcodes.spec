# revision 28210
# category Package
# catalog-ctan /macros/generic/catcodes
# catalog-date 2012-11-08 10:49:44 +0100
# catalog-license lppl1.3
# catalog-version 0.3a
Name:		texlive-catcodes
Epoch:		1
Version:	0.3a
Release:	1
Summary:	Generic handling of TeX category codes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/catcodes
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catcodes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catcodes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catcodes.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
