%global tl_name lebhart
%global tl_revision 78004

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Write your articles in a colorful way
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/lebhart
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lebhart.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lebhart.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(colorist)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a LaTeX class for typesetting articles with a
colorful design. Currently, it has native support for Chinese
(simplified and traditional), English, French, German, Italian,
Japanese, Portuguese (European and Brazilian), Russian and Spanish
typesetting. It compiles with either XeLaTeX or LuaLaTeX. This is part
of the colorist class series and depends on colorist.sty from the
colorist package. The package name "lebhart" is taken from the German
word "lebhaft" ("vivid"), combined with the first three letters of
"Artikel" ("article").

