%define name	celtx
%define version	0.9.9.7
%define release	%mkrel 1
%define Summary	Celtx : preproduction media application

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
License:	MPL-like
Group:		Office 
URL:		http://www.celtx.com
Source0:	http://www.celtx.com/download/%{name}-0997-src.tar.bz2
Source1:	celtx-icons.tar.bz2
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libIDL-devel
BuildRequires:  zip tcsh
BuildRequires:  libxft-devel
BuildRequires:	libxt-devel
BuildRequires:  gtk+2-devel >= 2.4.0
BuildRequires:  gnome-vfs2-devel
BuildRequires:	libgnomeui2-devel
BuildRequires:  krb-devel


%description
Celtx is the world's first fully integrated solution for media
pre-production and collaboration. It replaces old fashioned 'paper,
pen & binder' media creation with a digital approach to writing and
organizing that's more complete, simpler to work with, and easier
to share.

%prep
%setup -q -n %{name}-0997-src

%build
cd mozilla
cp mozconfig-nodebug-linux .mozconfig
echo "ac_add_options --enable-system-cairo" >>.mozconfig
make -f client.mk build

%install
%{__rm} -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_iconsdir}/{mini,large}
tar -C $RPM_BUILD_ROOT%{_iconsdir} -jxf %{SOURCE1}
mv $RPM_BUILD_ROOT%{_iconsdir}/celtx-16.png $RPM_BUILD_ROOT%{_iconsdir}/mini/celtx.png
mv $RPM_BUILD_ROOT%{_iconsdir}/celtx-32.png $RPM_BUILD_ROOT%{_iconsdir}/celtx.png
mv $RPM_BUILD_ROOT%{_iconsdir}/celtx-48.png $RPM_BUILD_ROOT%{_iconsdir}/large/celtx.png
cd mozilla
make -C ../objdir/celtx/installer
cp -a ../objdir/dist/celtx ${RPM_BUILD_ROOT}%{_libdir}/%{name}-%{version}
mv ${RPM_BUILD_ROOT}%{_libdir}/%{name}-%{version}/%{name} ${RPM_BUILD_ROOT}%{_bindir}/%{name}
sed -i -e 's/local//g' ${RPM_BUILD_ROOT}%{_bindir}/%{name}

#xdg menu entry
install -d -m755 ${RPM_BUILD_ROOT}%{_datadir}/applications
cat > ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Celtx
Comment=Screenplay Editor
Exec=%{_bindir}/%{name}
Icon=%{name}.png
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Office-Wordprocessors;
EOF

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(0755,root,root,0755)
%{_bindir}/*
%{_libdir}/%{name}-%{version}
%{_datadir}/*
%{_iconsdir}/*
