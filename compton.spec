%global commit 2343e4b
%global vermagic 0.1_beta2
%global gitdescribe v%{vermagic}-83-g%{commit}
%global snapshot .git20160628.%{commit}

Name:           compton
Version:        %{vermagic}
Release:        1%{snapshot}%{?dist}
Summary:        A compositor for X11

License:        MIT
URL:            https://github.com/chjj/compton
# git clone https://github.com/chjj/compton
# cd compton
# git archive --prefix=compton/ master | bzip2 >../compton.tar.bz2
Source0:        compton.tar.bz2

BuildRequires:  asciidoc
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(dbus-1)
Requires:       hicolor-icon-theme

%description
Compton is a compositor for X, and a fork of xcompmgr-dana.


%prep
%setup -q -n %{name}


%build
echo '#!/bin/bash' > configure
chmod +x configure
%configure
make COMPTON_VERSION=%{gitdescribe} %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :


%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/*/*
%{_mandir}/man1/*.1*


%changelog
* Tue Jun 28 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.1_beta2-1.git20160628.2343e4b
- Public release
