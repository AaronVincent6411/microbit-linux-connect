# microbit-linux-connect

A lightweight Linux userspace driver that auto-connects your BBC micro:bit via USB.

## 🧩 Features
- Automatically detects BBC micro:bit devices on USB
- Creates `/dev/microbit` alias for easy access
- Starts background service for serial communication
- Works on Ubuntu and Fedora

## 🛠 Installation
### Ubuntu/Debian
``` sudo apt install ./microbit-linux-connect_1.0_all.deb```

### Fedora
```sudo dnf install ./microbit-linux-connect-1.0-1.noarch.rpm```

### 🔍 Verify
```sudo systemctl status microbit-linux-connect```
