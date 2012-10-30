# revision 27763
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-catcodes
Version:	20121030
Release:	1
Summary:	TeXLive catcodes package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catcodes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catcodes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catcodes.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive catcodes package.

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
%doc %{_texmfdistdir}/source/generic/catcodes/srcfiles.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
