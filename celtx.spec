%define name	celtx
%define version	1.0
%define release	%mkrel 4
%define Summary	Celtx : preproduction media application

%define is10list	en-US pt-BR ca cs de es-ES fr it ro ru sl tr
#define is10list	en-US

%define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom

%define _provides_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
License:	MPL-like
Group:		Office 
URL:		http://www.celtx.com
Source0:	http://www.celtx.com/download/%{name}-10-src.tar.bz2
Source1:	http://www.celtx.com/download/%{name}-10-l10n.tar.bz2
Source2:	celtx-icons.tar.bz2
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libIDL-devel
BuildRequires:  zip tcsh
BuildRequires:  libxft-devel
BuildRequires:  gtk+2-devel >= 2.4.0
BuildRequires:  gnome-vfs2-devel
BuildRequires:	libgnomeui2-devel
BuildRequires:  krb-devel


#---------------------------------
# common files
%description
Celtx common files

%files
%defattr(0755,root,root,0755)
%{_iconsdir}/*
#---------------------------------

#---------------------------------
# Expand all packages.
%{expand:%(\
        for lang in %is10list; do\
                echo "%%{expand:%%(sed "s!__LANG__!$lang!g" %{_sourcedir}/%{name}-spec.tmpl 2> /dev/null)}";\
        done\
        )
}
#---------------------------------

%prep
%setup -q -n mozilla
cd ../
tar -jxf %{SOURCE1}

%build
for l10n in %is10list; do
	cp -f mozconfig-nodebug-linux .mozconfig
	rm -rf ../objdir-$l10n
	sed -i -e s/objdir/objdir-$l10n/ .mozconfig
	sed -i -e s/en-US/$l10n/ .mozconfig
	make -f client.mk build >/dev/null 2>&1
	find ../objdir-$l10n -type f -name "*.o" -exec rm {} \;
	find ../objdir-$l10n -type f -name "*.a" -exec rm {} \;
done

%install
%{__rm} -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_iconsdir}/{mini,large}
tar -C $RPM_BUILD_ROOT%{_iconsdir} -jxf %{SOURCE2}
mv $RPM_BUILD_ROOT%{_iconsdir}/celtx-16.png $RPM_BUILD_ROOT%{_iconsdir}/mini/celtx.png
mv $RPM_BUILD_ROOT%{_iconsdir}/celtx-32.png $RPM_BUILD_ROOT%{_iconsdir}/celtx.png
mv $RPM_BUILD_ROOT%{_iconsdir}/celtx-48.png $RPM_BUILD_ROOT%{_iconsdir}/large/celtx.png
for l10n in %is10list; do
	make -C ../objdir-$l10n/celtx/installer
	cp -a ../objdir-$l10n/dist/celtx ${RPM_BUILD_ROOT}%{_libdir}/%{name}-$l10n
	mv ${RPM_BUILD_ROOT}%{_libdir}/%{name}-$l10n/%{name} ${RPM_BUILD_ROOT}%{_bindir}/%{name}-$l10n
	sed -i -e 's!local!!g' ${RPM_BUILD_ROOT}%{_bindir}/%{name}-$l10n
	sed -i -e 's!moz_libdir=/usr/lib!moz_libdir=%{_libdir}!' ${RPM_BUILD_ROOT}%{_bindir}/%{name}-$l10n
done

%clean
%{__rm} -rf $RPM_BUILD_ROOT
