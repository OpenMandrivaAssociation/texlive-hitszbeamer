Name:		texlive-hitszbeamer
Version:	54381
Release:	1
Summary:	A beamer theme for Harbin Institute of Technology, ShenZhen
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hitszbeamer
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hitszbeamer.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hitszbeamer.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hitszbeamer.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a beamer theme designed for Harbin Institute of
Technology, ShenZhen (HITSZ).

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/hitszbeamer
%{_texmfdistdir}/tex/latex/hitszbeamer
%{_texmfdistdir}/bibtex/bst/hitszbeamer
%doc %{_texmfdistdir}/doc/latex/hitszbeamer

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
