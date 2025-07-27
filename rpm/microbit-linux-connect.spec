Name:           microbit-connect
Version:        1.0
Release:        1%{?dist}
Summary:        Auto-connect driver for BBC micro:bit over USB

License:        MIT
URL:            https://github.com/yourusername/microbit-connect
Source0:        %{name}-%{version}.tar.gz

Requires:       python3, python3-serial, systemd, udev

%description
Automatically detects BBC micro:bit USB devices and connects via serial.

%prep
%setup -q

%install
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/etc/udev/rules.d
mkdir -p %{buildroot}/usr/lib/systemd/system

install -m 0755 src/microbit_driver.py %{buildroot}/usr/local/bin/microbit_driver.py
install -m 0644 src/microbit_driver.rules %{buildroot}/etc/udev/rules.d/microbit_driver.rules
install -m 0644 systemd/microbit_connect.service %{buildroot}/usr/lib/systemd/system/microbit_connect.service

%post
udevadm control --reload-rules
systemctl daemon-reload
systemctl enable microbit_connect.service

%files
/usr/local/bin/microbit_driver.py
/etc/udev/rules.d/microbit_driver.rules
/usr/lib/systemd/system/microbit_connect.service

%changelog
* Mon Oct 27 2025 Aaron P Laju - 1.0-0
- Initial release
