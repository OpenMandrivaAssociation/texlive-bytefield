Name:		texlive-bytefield
Version:	2.1
Release:	1
Summary:	Create illustrations for network protocol specifications
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bytefield
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bytefield.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bytefield.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bytefield.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The bytefield package helps the user create illustrations for
network protocol specifications and anything else that utilizes
fields of data. These illustrations show how the bits and bytes
are laid out in a packet or in memory. Users should note that
the present version 2.0 offers a different (and incompatible)
user interface from earlier versions.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
