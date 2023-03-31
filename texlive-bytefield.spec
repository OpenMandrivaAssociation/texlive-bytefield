Name:		texlive-bytefield
Version:	60265
Release:	2
Summary:	Create illustrations for network protocol specifications
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bytefield
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bytefield.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bytefield.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bytefield.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bytefield package helps the user create illustrations for
network protocol specifications and anything else that utilizes
fields of data. These illustrations show how the bits and bytes
are laid out in a packet or in memory. Users should note that
the present version 2.0 offers a different (and incompatible)
user interface from earlier versions.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bytefield/bytefield.sty
%doc %{_texmfdistdir}/doc/latex/bytefield/README
%doc %{_texmfdistdir}/doc/latex/bytefield/bf-example.pdf
%doc %{_texmfdistdir}/doc/latex/bytefield/bf-example.tex
%doc %{_texmfdistdir}/doc/latex/bytefield/bytefield.pdf
#- source
%doc %{_texmfdistdir}/source/latex/bytefield/bytefield.dtx
%doc %{_texmfdistdir}/source/latex/bytefield/bytefield.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
