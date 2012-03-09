%define is10list	en-US pt-BR ca cs de es-ES fr

%define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom
%define _provides_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom

Name:		celtx
Version:	2.5.1
Release:	%mkrel 3
Summary:	Celtx : preproduction media application
License:	MPL-like
Group:		Office 
URL:		http://www.celtx.com
Source0:	http://www.celtx.com/download/%{name}-2-5-1-src.tar.bz2
Source1:	http://www.celtx.com/download/%{name}-2-5-1-l10n.tar.bz2
Source2:	celtx-icons.tar.bz2
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libIDL-2.0)
BuildRequires:  zip
BuildRequires:	tcsh
BuildRequires:  pkgconfig(xft) 
BuildRequires:  pkgconfig(gdk-2.0) >= 2.4.0
BuildRequires:  pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:  krb5-devel


#---------------------------------
# common files
%description
Celtx common files

%files
%defattr(0755,root,root,0755)
%{_iconsdir}/*
#---------------------------------

#---------------------------------
# en_US
%package -n celtx-en-US

%define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom
%define _provides_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom

Summary:	Celtx for en-US language
License:	MPL-like
Group:		Office
URL:		http://www.celtx.com
Obsoletes:	celtx-dictionary
Requires:	celtx
Requires:	myspell-en_US

%description -n celtx-en-US
Celtx is the world's first fully integrated solution for media
pre-production and collaboration. It replaces old fashioned 'paper,
pen & binder' media creation with a digital approach to writing and
organizing that's more complete, simpler to work with, and easier
to share.
Package for en_US language

%files -n celtx-en-US
%defattr(0755,root,root,0755)
%_bindir/celtx-en-US
%_libdir/celtx-en-US
%{_datadir}/applications/celtx-en-US.desktop
#---------------------------------

#---------------------------------
# pt-BR
%package -n celtx-pt-BR

%define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom
%define _provides_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom

Summary:	Celtx for pt-BR language
License:	MPL-like
Group:		Office
URL:		http://www.celtx.com
Obsoletes:	celtx-dictionary
Requires:	celtx
Requires:	myspell-pt_BR

%description -n celtx-pt-BR
Celtx is the world's first fully integrated solution for media
pre-production and collaboration. It replaces old fashioned 'paper,
pen & binder' media creation with a digital approach to writing and
organizing that's more complete, simpler to work with, and easier
to share.
Package for pt-BR language

%files -n celtx-pt-BR
%defattr(0755,root,root,0755)
%_bindir/celtx-pt-BR
%_libdir/celtx-pt-BR
%{_datadir}/applications/celtx-pt-BR.desktop
#---------------------------------

#---------------------------------
# ca
%package -n celtx-ca

%define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom
%define _provides_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom

Summary:	Celtx for ca language
License:	MPL-like
Group:		Office
URL:		http://www.celtx.com
Obsoletes:	celtx-dictionary
Requires:	celtx
Requires:	myspell-ca_ES

%description -n celtx-ca
Celtx is the world's first fully integrated solution for media
pre-production and collaboration. It replaces old fashioned 'paper,
pen & binder' media creation with a digital approach to writing and
organizing that's more complete, simpler to work with, and easier
to share.
Package for ca-ES language

%files -n celtx-ca
%defattr(0755,root,root,0755)
%_bindir/celtx-ca
%_libdir/celtx-ca
%{_datadir}/applications/celtx-ca.desktop
#---------------------------------

#---------------------------------
# cs
%package -n celtx-cs

%define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom
%define _provides_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom

Summary:	Celtx for cs language
License:	MPL-like
Group:		Office
URL:		http://www.celtx.com
Obsoletes:	celtx-dictionary
Requires:	celtx
Requires:	myspell-cs_CZ

%description -n celtx-cs
Celtx is the world's first fully integrated solution for media
pre-production and collaboration. It replaces old fashioned 'paper,
pen & binder' media creation with a digital approach to writing and
organizing that's more complete, simpler to work with, and easier
to share.
Package for cs_CZ language

%files -n celtx-cs
%defattr(0755,root,root,0755)
%_bindir/celtx-cs
%_libdir/celtx-cs
%{_datadir}/applications/celtx-cs.desktop
#---------------------------------

#---------------------------------
# de
%package -n celtx-de

%define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom
%define _provides_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom

Summary:	Celtx for de language
License:	MPL-like
Group:		Office
URL:		http://www.celtx.com
Obsoletes:	celtx-dictionary
Requires:	celtx
Requires:	myspell-de_DE

%description -n celtx-de
Celtx is the world's first fully integrated solution for media
pre-production and collaboration. It replaces old fashioned 'paper,
pen & binder' media creation with a digital approach to writing and
organizing that's more complete, simpler to work with, and easier
to share.
Package for de_DE language

%files -n celtx-de
%defattr(0755,root,root,0755)
%_bindir/celtx-de
%_libdir/celtx-de
%{_datadir}/applications/celtx-de.desktop
#---------------------------------

#---------------------------------
# es-ES
%package -n celtx-es-ES

%define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom
%define _provides_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom

Summary:	Celtx for es-ES language
License:	MPL-like
Group:		Office
URL:		http://www.celtx.com
Obsoletes:	celtx-dictionary
Requires:	celtx
Requires:	myspell-es_ES

%description -n celtx-es-ES
Celtx is the world's first fully integrated solution for media
pre-production and collaboration. It replaces old fashioned 'paper,
pen & binder' media creation with a digital approach to writing and
organizing that's more complete, simpler to work with, and easier
to share.
Package for es-ES language

%files -n celtx-es-ES
%defattr(0755,root,root,0755)
%_bindir/celtx-es-ES
%_libdir/celtx-es-ES
%{_datadir}/applications/celtx-es-ES.desktop
#---------------------------------

#---------------------------------
# fr
%package -n celtx-fr

%define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom
%define _provides_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom

Summary:	Celtx for fr language
License:	MPL-like
Group:		Office
URL:		http://www.celtx.com
Obsoletes:	celtx-dictionary
Requires:	celtx
Requires:	myspell-fr_FR

%description -n celtx-fr
Celtx is the world's first fully integrated solution for media
pre-production and collaboration. It replaces old fashioned 'paper,
pen & binder' media creation with a digital approach to writing and
organizing that's more complete, simpler to work with, and easier
to share.
Package for fr_FR language

%files -n celtx-fr
%defattr(0755,root,root,0755)
%_bindir/celtx-fr
%_libdir/celtx-fr
%{_datadir}/applications/celtx-fr.desktop
#---------------------------------

#---------------------------------
# it
#package -n celtx-it

#define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom
#define _provides_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom

#Summary:	Celtx for it language
#License:	MPL-like
#Group:		Office
#URL:		http://www.celtx.com
#Obsoletes:	celtx-dictionary
#Requires:	celtx
#Requires:	myspell-it_IT

#%description -n celtx-it
#Celtx is the world's first fully integrated solution for media
#pre-production and collaboration. It replaces old fashioned 'paper,
#pen & binder' media creation with a digital approach to writing and
#organizing that's more complete, simpler to work with, and easier
#to share.
#Package for it_IT language

#%files -n celtx-it
#%defattr(0755,root,root,0755)
#%_bindir/celtx-it
#%_libdir/celtx-it
#%{_datadir}/applications/celtx-it.desktop
#---------------------------------

#---------------------------------
# ro
#%package -n celtx-ro

#define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom
#define _provides_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom

#Summary:	Celtx for ro language
#License:	MPL-like
#Group:		Office
#URL:		http://www.celtx.com
#Obsoletes:	celtx-dictionary
#Requires:	celtx

#%description -n celtx-ro
#Celtx is the world's first fully integrated solution for media
#pre-production and collaboration. It replaces old fashioned 'paper,
#pen & binder' media creation with a digital approach to writing and
#organizing that's more complete, simpler to work with, and easier
#to share.
#Package for ro language

#%files -n celtx-ro
#%defattr(0755,root,root,0755)
#%_bindir/celtx-ro
#%_libdir/celtx-ro
#---------------------------------

#---------------------------------
# ru
#%package -n celtx-ru

#define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom
#define _provides_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom

#Summary:	Celtx for ru language
#License:	MPL-like
#Group:		Office
#URL:		http://www.celtx.com
#Obsoletes:	celtx-dictionary
#Requires:	celtx

#%description -n celtx-ru
#Celtx is the world's first fully integrated solution for media
#pre-production and collaboration. It replaces old fashioned 'paper,
#pen & binder' media creation with a digital approach to writing and
#organizing that's more complete, simpler to work with, and easier
#to share.
#Package for ru language

#%files -n celtx-ru
#%defattr(0755,root,root,0755)
#%_bindir/celtx-ru
#%_libdir/celtx-ru
#---------------------------------

#---------------------------------
# sl
#%package -n celtx-sl

#define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom
#define _provides_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom

#Summary:	Celtx for sl language
#License:	MPL-like
#Group:		Office
#URL:		http://www.celtx.com
#Obsoletes:	celtx-dictionary
#Requires:	celtx

#%description -n celtx-sl
#Celtx is the world's first fully integrated solution for media
#pre-production and collaboration. It replaces old fashioned 'paper,
#pen & binder' media creation with a digital approach to writing and
#organizing that's more complete, simpler to work with, and easier
#to share.
#Package for sl language

#%files -n celtx-sl
#%defattr(0755,root,0755)
#%_bindir/celtx-sl
#%_libdir/celtx-sl
#---------------------------------

#---------------------------------
# tr
#%package -n celtx-tr
#
#define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom
#define _provides_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom

#Summary:	Celtx for tr language
#License:	MPL-like
#Group:		Office
#URL:		http://www.celtx.com
#Obsoletes:	celtx-dictionary
#Requires:	celtx
#
#%description -n celtx-tr
#Celtx is the world's first fully integrated solution for media
#pre-production and collaboration. It replaces old fashioned 'paper,
#pen & binder' media creation with a digital approach to writing and
#organizing that's more complete, simpler to work with, and easier
#to share.
#Package for tr language

#%files -n celtx-tr
#%defattr(0755,root,0755)
#%_bindir/celtx-tr
#%_libdir/celtx-tr
#---------------------------------

%prep
#%setup -q -n mozilla
%setup -q -n celtx-2-5-1-src
cd ../
tar -jxf %{SOURCE1}
mv celtx-2-5-1-l10n/l10n celtx-2-5-1-src/l10n

%build
cd mozilla
for l10n in %is10list; do
	cp -f mozconfig-nodebug-linux .mozconfig
	%{__rm} -rf ../objdir-$l10n
	sed -i -e s/objdir/objdir-$l10n/ .mozconfig
	sed -i -e s/en-US/$l10n/ .mozconfig
	make -f client.mk build
	# for space optimization we do installer in the build process and copy the resultat in a tmp dir
	make -C ../objdir-$l10n/celtx/installer
	cp -a ../objdir-$l10n/dist/celtx ../%{name}-$l10n
        %{__rm} -rf ../objdir-$l10n
done

%install
cd mozilla
%{__rm} -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_iconsdir}/{mini,large}
tar -C $RPM_BUILD_ROOT%{_iconsdir} -jxf %{SOURCE2}
mv $RPM_BUILD_ROOT%{_iconsdir}/celtx-16.png $RPM_BUILD_ROOT%{_iconsdir}/mini/celtx.png
mv $RPM_BUILD_ROOT%{_iconsdir}/celtx-32.png $RPM_BUILD_ROOT%{_iconsdir}/celtx.png
mv $RPM_BUILD_ROOT%{_iconsdir}/celtx-48.png $RPM_BUILD_ROOT%{_iconsdir}/large/celtx.png
for l10n in %is10list; do
	mv ../%{name}-$l10n ${RPM_BUILD_ROOT}%{_libdir}/%{name}-$l10n
	#dont need dictionary : use myspell provides
	%{__rm} -rf ${RPM_BUILD_ROOT}%{_libdir}/%{name}-$l10n/dictionaries
	ln -s %{_datadir}/dict/ooo ${RPM_BUILD_ROOT}%{_libdir}/%{name}-$l10n/dictionaries
	#adapt the bin script
	mv ${RPM_BUILD_ROOT}%{_libdir}/%{name}-$l10n/%{name} ${RPM_BUILD_ROOT}%{_bindir}/%{name}-$l10n
	sed -i -e "s!/usr/local/lib!%{_libdir}!g" ${RPM_BUILD_ROOT}%{_bindir}/%{name}-$l10n
	sed -i -e "s!%{name}-%{version}!%{name}-${l10n}!g" ${RPM_BUILD_ROOT}%{_bindir}/%{name}-$l10n
	mv ${RPM_BUILD_ROOT}%{_libdir}/%{name}-$l10n/%{name}-bin ${RPM_BUILD_ROOT}%{_libdir}/%{name}-$l10n/%{name}-${l10n}-bin
	#xdg menu entry
	mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/applications
	cat > ${RPM_BUILD_ROOT}%{_datadir}/applications/celtx-${l10n}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Celtx
Comment=Screenplay Editor
Exec=%{_bindir}/celtx-${l10n}
Icon=celtx
Terminal=false
Type=Application
Categories=Office;WordProcessor;
EOF

done

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
