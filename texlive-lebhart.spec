Name:		texlive-lebhart
Version:	64280
Release:	2
Summary:	Write your articles in a colorful way
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lebhart
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lebhart.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lebhart.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a LaTeX class for typesetting articles
with a colorful design. Currently, it has native support for
Chinese (simplified and traditional), English, French, German,
Italian, Japanese, Portuguese (European and Brazilian), Russian
and Spanish typesetting. It compiles with either XeLaTeX or
LuaLaTeX. This is part of the colorist class series and depends
on colorist.sty from the colorist package. The package name
"lebhart" is taken from the German word "lebhaft" ("vivid"),
combined with the first three letters of "Artikel" ("article").

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/lebhart
%doc %{_texmfdistdir}/doc/latex/lebhart

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
