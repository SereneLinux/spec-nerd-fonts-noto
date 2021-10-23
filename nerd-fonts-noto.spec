Summary: nerd-fonts-noto
Name: nerd-fonts-noto
Version: 2.1.0
Release: 2%{?dist}
Group: User Interface/Desktops
License: NONE
Packager: kahenteikou
Vendor: INDETAIL

Source0: https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Noto.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
%global debug_package %{nil}
%description
Nerd Noto Font
%prep
rm -rf $RPM_BUILD_ROOT

%autosetup -n Noto

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/fonts/TTF/
find . -iname "*.ttf" -not -iname "*Windows Compatible.ttf" -execdir install -Dm644 {} "$RPM_BUILD_ROOT/usr/share/fonts/TTF/{}" \;


%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Bold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Medium Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Black Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Light Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed ExtraLight Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Regular Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Black Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Bold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Condensed ExtraLight Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Condensed ExtraLight Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Bold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraCondensed ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed ExtraLight Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Bold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraLight Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Black Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Condensed SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Light Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Black Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Mono Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Condensed ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Bold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Bold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed ExtraBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed ExtraBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Thin Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono Condensed Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed ExtraLight Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Thin Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Black Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed SemiBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Bold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Bold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiCondensed ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Black Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono Regular Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Bold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Medium Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Light Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Light Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Black Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Thin Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed ExtraBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed ExtraBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Bold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Light Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed ExtraLight Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Bold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Bold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Thin Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraLight Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Light Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono Condensed Bold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed ExtraBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiCondensed Black Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Black Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Medium Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraCondensed Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed SemiBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Light Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Regular Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Medium Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Black Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans ExtraBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono Bold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Black Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Condensed ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Light Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Thin Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Bold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Black Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Light Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Medium Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Black Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Black Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraCondensed Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Light Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Medium Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Thin Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraCondensed Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Bold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Medium Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraCondensed Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Condensed ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Medium Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Bold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Black Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed ExtraLight Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Emoji Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed SemiBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Black Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Black Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Condensed SemiBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Regular Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Thin Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Black Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Bold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiCondensed Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans SemiBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed SemiBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Medium Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiCondensed Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed ExtraLight Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Black Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed ExtraLight Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed ExtraBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Light Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Black Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed SemiBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Regular Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Black Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Black Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Bold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono Bold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Medium Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Bold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Thin Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono Condensed ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed SemiBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Black Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif SemiBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Condensed SemiBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Condensed ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono Condensed Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Bold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Black Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Medium Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Medium Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Black Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraLight Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Bold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Medium Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraCondensed Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Black Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Medium Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Thin Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Bold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed ExtraBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Bold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Bold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Light Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Black Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiCondensed ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Black Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Bold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Black Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Medium Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraCondensed ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Thin Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed SemiBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Bold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed SemiBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraLight Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Bold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Thin Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Condensed ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Condensed ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Black Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Thin Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Bold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Black Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Black Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Thin Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiCondensed SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Bold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Bold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Black Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed ExtraBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Condensed ExtraLight Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Black Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Thin Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono Condensed SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono Condensed ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Thin Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Black Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Medium Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Bold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Light Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiCondensed Black Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Light Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Bold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono Black Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Bold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed ExtraBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Regular Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Black Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed ExtraBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Bold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Light Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Light Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed ExtraBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Bold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Bold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Black Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Black Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Bold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed SemiBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Light Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Light Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Bold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed SemiBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Bold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiCondensed Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono Condensed Black Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Black Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Thin Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono Condensed ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Bold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Black Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Bold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed ExtraLight Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Medium Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Bold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Medium Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed SemiBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono Regular Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono Black Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed SemiBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed ExtraBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Light Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiCondensed SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Black Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraCondensed Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Condensed SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed ExtraLight Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Black Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Black Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Bold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Condensed SemiBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed ExtraLight Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Light Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif SemiBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Emoji Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Thin Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Light Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Bold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono Condensed Black Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Condensed ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Medium Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiCondensed Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Black Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono Condensed Bold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed ExtraLight Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed ExtraBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans ExtraBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Regular Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed ExtraLight Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono Condensed Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Mono Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Condensed SemiBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Bold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Bold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Black Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraCondensed Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Regular Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Thin Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Condensed ExtraBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed ExtraBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiCondensed Bold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Black Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed SemiBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed ExtraLight Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed ExtraLight Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Black Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed ExtraBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Black Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraCondensed ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Light Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Thin Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Medium Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Black Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Condensed ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Medium Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Black Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Bold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Medium Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Thin Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraLight Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Bold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Thin Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Medium Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraLight Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Light Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Regular Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraCondensed Black Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Bold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono Condensed Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Medium Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiCondensed Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Thin Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed ExtraBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Bold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Thin Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraCondensed Black Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Light Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed SemiBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Black Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans SemiBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraCondensed Bold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Thin Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Thin Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Black Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraCondensed ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed SemiBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono Condensed Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed SemiBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiCondensed Bold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed ExtraBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraCondensed SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed ExtraBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono Condensed Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Thin Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Bold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Bold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Black Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiCondensed Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Black Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Medium Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiCondensed ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Bold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed SemiBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Thin Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed ExtraLight Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Medium Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Bold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed SemiBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed ExtraLight Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Light Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed ExtraBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed SemiBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed ExtraBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Bold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Black Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Thin Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Black Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraLight Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Bold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Condensed Black Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Medium Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display Light Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Light Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono Condensed SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Light Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono Condensed Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Condensed ExtraLight Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Condensed Medium Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Black Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiCondensed Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiCondensed ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed SemiBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Light Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Black Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Thin Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Condensed Bold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Bold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Condensed ExtraBold Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraCondensed SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Medium Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed ExtraLight Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Medium Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display ExtraCondensed ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Condensed ExtraBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Black Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraLight Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraCondensed Bold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Light Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed ExtraLight Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed ExtraLight Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Black Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono ExtraCondensed Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Condensed SemiBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Bold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed Medium Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display SemiCondensed Medium Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed Thin Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono Condensed ExtraLight Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display ExtraCondensed ExtraLight Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Condensed SemiBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Mono SemiCondensed Medium Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed Light Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans ExtraCondensed ExtraBold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif SemiCondensed ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif ExtraCondensed Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono Condensed Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Medium Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Bold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans SemiCondensed Light Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans ExtraBold Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Bold Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Display SemiCondensed ExtraLight Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Display Light Italic Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Serif Condensed ExtraBold Italic Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Serif Display Thin Nerd Font Complete.ttf
/usr/share/fonts/TTF/Noto Sans Mono Thin Nerd Font Complete Mono.ttf
/usr/share/fonts/TTF/Noto Sans Display Condensed Light Italic Nerd Font Complete.ttf
%changelog
