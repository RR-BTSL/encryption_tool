# 🔑 Encryption_Tool

A simple command-line tool for encrypting and decrypting text using symmetric encryption.

## 📖 Prerequisites

Install dependencies:

### pip:

```bash
pip install cryptography pyinstaller
```

### Or using [uv](https://docs.astral.sh/uv/)!

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

## 📖 Usage

See the --help option for usage instructions:

```bash
dist/encryption_tool --help
```
