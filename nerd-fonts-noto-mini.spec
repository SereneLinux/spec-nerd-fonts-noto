Summary: nerd-fonts-noto-mini
Name: nerd-fonts-noto-mini
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

%setup -n Noto -c

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/fonts/TTF/
cp  /usr/share/fonts/TTF/Noto Mono Nerd Font Complete.ttf $RPM_BUILD_ROOT/usr/share/fonts/TTF/


%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
"/usr/share/fonts/TTF/Noto Mono Nerd Font Complete.ttf"
%changelog
