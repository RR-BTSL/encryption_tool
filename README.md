# Encryption Tool
## Prerequisites

1. Install dependencies:
   ```bash
   pip install cryptography pyinstaller
   ```

   Or using `uv`:
   ```bash
   uv sync
   ```

## Build From Source

Run the following command to create a single-file executable:

```bash
pyinstaller --onefile encryption_tool.py
```

This will generate a standalone executable under `dist/` called `encryption_tool`.

## Usage:
See the --help option for usage instructions:

```bash
dist/encryption_tool --help
```
