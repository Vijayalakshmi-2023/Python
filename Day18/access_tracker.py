import datetime

class SecureData:
    def __init__(self, secret):
        self._secret = secret

    @property
    def secret(self):
        # Log every read access
        print(f"[ACCESS LOG] Secret accessed at {datetime.datetime.now()}")
        return self._secret

    @secret.setter
    def secret(self, value):
        raise AttributeError("❌ Write access denied: 'secret' is a read-only property.")
data = SecureData("TOP-SECRET-123")

# Accessing secret (logs it)
print("Secret is:", data.secret)

# Attempting to change it (raises error)
try:
    data.secret = "HACKED"
except AttributeError as e:
    print(e)
