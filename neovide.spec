# With thanks to Chris Bouchard <chris@upliftinglemma.net> for 
# inspiration from his Copr spec file. 

# Directory where the application icon will be installed
%global xdg_icon_dir %{_datadir}/icons/hicolor/scalable/apps

# Directory where the desktop entry will be installed
%global xdg_application_dir %{_datadir}/applications
%global debug_package %{nil}

Name:           neovide
Summary:        No Nonsense Neovim Client in Rust
Version:        0.16.2
Release:        0
License:        MIT
URL:            https://github.com/neovide/neovide
Source0:        https://github.com/neovide/neovide/archive/refs/tags/%{version}.tar.gz

# Tools
BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++

# Libraries
#BuildRequires:  lib64SDL2-devel
BuildRequires:  lib64SDL-devel
BuildRequires:  lib64expat-devel
BuildRequires:  lib64fontconfig-devel
BuildRequires:  lib64freetype6-devel
BuildRequires:  lib64xext-devel
BuildRequires:  lib64openssl-devel
BuildRequires:  lib64vulkan-devel

# Base
Requires:       neovim >= 0.4.0

# Libraries
Requires:       lib64SDL2_2.0_1
Requires:       expat
Requires:       fontconfig
Requires:       lib64xext6
Requires:       openssl
Requires:       vulkan-headers
Requires:       vulkan-loader
Requires:       vulkan-tools

%description

This is a simple graphical user interface for Neovim. Where possible there are
some graphical improvements, but it should act functionally like the terminal
UI.

%prep
%setup


%build
cargo build --release --verbose


%install
install --mode=755 --directory "%{buildroot}%{_bindir}"
install --mode=755 'target/release/neovide' "%{buildroot}%{_bindir}/neovide"

install --mode=755 --directory "%{buildroot}%{xdg_icon_dir}"
install --mode=644 'assets/neovide.svg' "%{buildroot}%{xdg_icon_dir}/neovide.svg"

install --mode=755 --directory "%{buildroot}%{xdg_application_dir}"
desktop-file-install --dir="%{buildroot}%{xdg_application_dir}" \
    'assets/neovide.desktop'


%files
%license LICENSE
%{_bindir}/neovide
%{xdg_icon_dir}/neovide.svg
%{xdg_application_dir}/neovide.desktop

