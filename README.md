# Encryption Tool

## Prerequisites

Install dependencies:

**pip:**

1.
   ```bash
   pip install cryptography pyinstaller
   ```

**Or using [uv](https://docs.astral.sh/uv/)!**

1. **Install uv:**

   Windows:
   ```bash
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

   Linux/macOS:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

## Build From Source

Run the following command to create a single-file executable:

```bash
pyinstaller --onefile encryption_tool.py
```

This will generate a standalone executable under `dist/` called `encryption_tool`.

## Usage

See the --help option for usage instructions:

```bash
dist/encryption_tool --help
```
