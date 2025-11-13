from cryptography.fernet import Fernet
from src.ThreadSafeSingleton import ThreadSafeSingleton
from functools import wraps


def initialized(func):
    """Decorator that checks if a custom key has been set before executing the method."""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self._using_custom_key:
            raise RuntimeError("SecretsManager has not been initialized with a custom key. Call set_key() first.")
        return func(self, *args, **kwargs)
    return wrapper

class SecretsManager(ThreadSafeSingleton):
    """Singleton for managing secrets encryption and decryption."""
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._using_custom_key: bool = False
            self._fernet: Fernet = Fernet(Fernet.generate_key())
            self._initialized = True

    def set_key(self, key: str | bytes) -> None:
        """Sets a new encryption key."""
        self._fernet = Fernet(key)
        self._using_custom_key = True

    @initialized
    def decrypt(self, encrypted_secret: str) -> str:
        """Decrypts an encrypted secret."""
        decrypted = self._fernet.decrypt(encrypted_secret.encode())
        return decrypted.decode()

    @initialized
    def encrypt(self, plaintext_secret: str) -> str:
        """Encrypts a plaintext secret."""
        encrypted = self._fernet.encrypt(plaintext_secret.encode())
        return encrypted.decode()
