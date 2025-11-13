import argparse
import sys

from cryptography.fernet import Fernet
from src.SecretsManager import SecretsManager


def main() -> None:
    help_message = """Example Usage:
    Generate a new key:
        python encryption_tool.py --generate-key
    
    Encrypt a secret:
        python encryption_tool.py --key ESupV_-COXwAaRcAItGVbN2bU_Ujqb42gXFDjTN-lw0= --encrypt "Sup3rS3cr3tP4ssw0rd!"
    
    Decrypt a secret (if you want to verify):
        python encryption_tool.py --key ESupV_-COXwAaRcAItGVbN2bU_Ujqb42gXFDjTN-lw0= --decrypt "gAAA...Bg=="
    """

    parser = argparse.ArgumentParser(description=help_message, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--generate-key", action="store_true", help="Generate a new encryption key.")
    parser.add_argument("--encrypt", type=str, metavar="PLAINTEXT_SECRET", help="Encrypt the plaintext secret.")
    parser.add_argument("--decrypt", type=str, metavar="ENCRYPTED_SECRET", help="Decrypt the encrypted secret.")
    parser.add_argument("--key", type=str, help="The encryption key.")

    # Show help if no arguments provided
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    # Handle key generation
    if args.generate_key:
        key = Fernet.generate_key()
        print(key.decode())
        return

    # Validate that either --encrypt or --decrypt is provided
    if not args.encrypt and not args.decrypt:
        parser.error("please provide either --encrypt or --decrypt with a secret")

    if args.encrypt and args.decrypt:
        parser.error("please provide either --encrypt or --decrypt, not both")

    if not args.key:
        parser.error("--key is required for encryption or decryption")

    key = args.key

    try:
        SecretsManager().set_key(key.encode())

        if args.decrypt:
            decrypted_secret = SecretsManager().decrypt(args.decrypt)
            print(decrypted_secret)
        else:
            encrypted_secret = SecretsManager().encrypt(args.encrypt)
            print(encrypted_secret)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
