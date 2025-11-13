# 🔑 Encryption_Tool

A simple standalone command-line tool for encrypting and decrypting text using symmetric encryption.

## 📖 Prerequisites

### Install [uv](https://docs.astral.sh/uv/):

Windows:
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Linux/macOS:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
### Install dependencies
```bash
uv sync
```

## 📖 Build From Source

Run the following command to create a single-file executable:

```bash
uvx pyinstaller --onefile encryption_tool.py
```

ℹ️ This will generate a standalone executable under `dist/` called `encryption_tool`.
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

If you want to, you can also just run encryption_tool.py directly with Python:

```bash
python encryption_tool.py --help
```

You can also download pre-built binaries from the [Releases](https://github.com/RR-BTSL/encryption_tool/releases) section.
