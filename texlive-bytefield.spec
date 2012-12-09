# revision 23351
# category Package
# catalog-ctan /macros/latex/contrib/bytefield
# catalog-date 2011-06-22 20:08:44 +0200
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-bytefield
Version:	2.1
Release:	2
Summary:	Create illustrations for network protocol specifications
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bytefield
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bytefield.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bytefield.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bytefield.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1-2
+ Revision: 749894
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.1-1
+ Revision: 717991
- texlive-bytefield
- texlive-bytefield
- texlive-bytefield
- texlive-bytefield
- texlive-bytefield

