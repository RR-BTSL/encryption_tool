import argparse
import sys

from SecretsManager import SecretsManager


def main() -> None:
    parser = argparse.ArgumentParser(description="Encrypt a plaintext secret using a specified key.")
    parser.add_argument("plaintext_secret", type=str, help="The plaintext secret to encrypt.")
    parser.add_argument("--key", type=str, required=True, help="The encryption key.")
    args = parser.parse_args()

    plaintext_secret = args.plaintext_secret
    key = args.key


    try:
        SecretsManager().set_key(key.encode())
        encrypted_secret = SecretsManager().encrypt(plaintext_secret)
        print(encrypted_secret)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
