Summary:	Command line interface to the X11 clipboard
Name:		xclip
Version:	0.12
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/sourceforge/xclip/%{name}-%{version}.tar.gz
# Source0-md5:	f7e19d3e976fecdc1ea36cd39e39900d
URL:		http://sourceforge.net/projects/xclip
BuildRequires:	xorg-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xclip is a command line interface to the X11 clipboard. It can also be
used for copying files, as an alternative to sftp/scp, thus avoiding
password prompts when X11 forwarding has already been setup.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/xclip
%attr(755,root,root) %{_bindir}/xclip-copyfile
%attr(755,root,root) %{_bindir}/xclip-cutfile
%attr(755,root,root) %{_bindir}/xclip-pastefile
%{_mandir}/man1/xclip.1*
%{_mandir}/man1/xclip-copyfile.1*

