# 🔑 Encryption_Tool

A simple command-line tool for encrypting and decrypting text using symmetric encryption.
Using python's Fernet 2-=

## 📖 Prerequisites

To Install dependencies use pip or uv:

### pip:

```bash
pip install cryptography pyinstaller
```

### [uv](https://docs.astral.sh/uv/)

#### Install uv:

Windows:
```PowerShell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Linux/macOS:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
#### Install dependencies
```bash
uv sync
```

## 📖 Build From Source

Run the following command to create a single-file executable:

```bash
pyinstaller --onefile encryption_tool.py
```

This will generate a standalone executable under `dist/` called `encryption_tool`.
Your build is platform-specific. A Windows build will generate a .exe binary, and a Linux build will generate a Linux binary.
Don't forget to give execute permissions to the binary on Linux/macOS:

```bash
chmod +x encryption_tool
```

## 📖 Usage

See the --help option for usage instructions:

```bash
./encryption_tool --help
```
