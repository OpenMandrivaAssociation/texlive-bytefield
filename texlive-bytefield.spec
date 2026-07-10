%global tl_name bytefield
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.9
Release:	%{tl_revision}.1
Summary:	Create illustrations for network protocol specifications
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bytefield
License:	lppl1.3a
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bytefield.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bytefield.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bytefield.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bytefield package helps the user create illustrations for network
protocol specifications and anything else that utilizes fields of data.
These illustrations show how the bits and bytes are laid out in a packet
or in memory.

