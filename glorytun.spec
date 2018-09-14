Name:		glorytun
Version:	0.0.99	
Release:	1%{?dist}
Summary:	Glorytun VPN

License:	BSD
URL:		https://github.com/angt/glorytun
Source0:	https://github.com/angt/glorytun/releases/download/v0.0.99-mud/glorytun-0.0.99-mud.tar.gz

BuildRequires:	libsodium-devel, gcc-c++, meson
#Requires:	

%description
Glorytun is a small, simple and secure VPN over mud.

%prep
%setup -n  glorytun-%{version}-mud


%build
meson build


%install
ninja-build -C build
mkdir -p %{buildroot}/usr/lib/systemd/system
mkdir -p %{buildroot}/usr/lib/systemd/network
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/etc/glorytun
cp systemd/glorytun\@.service.in %{buildroot}/usr/lib/systemd/system/glorytun\@.service
sed -i 's|@bindir@|/usr/local/bin|' %{buildroot}/usr/lib/systemd/system/glorytun\@.service
cp systemd/glorytun.network %{buildroot}/usr/lib/systemd/network
cp systemd/glorytun-client.network %{buildroot}/usr/lib/systemd/network
cp systemd/glorytun-run %{buildroot}/usr/local/bin
cp systemd/glorytun-setup %{buildroot}/usr/local/bin
cp build/glorytun %{buildroot}/usr/local/bin


%files
%doc
/usr/local/bin/*
/usr/lib/systemd/network/*
/usr/lib/systemd/system/*
%dir /etc/glorytun


%changelog

