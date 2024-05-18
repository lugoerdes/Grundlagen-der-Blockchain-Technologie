import gnupg

# Erstelle eine Instanz von GnuPG
gpg = gnupg.GPG()

# Generiere ein Schlüsselpaar
input_data = gpg.gen_key_input(
    name_email='user@example.com',
    passphrase='your_passphrase',
    key_type='RSA',
    key_length=2048
)
key = gpg.gen_key(input_data)

# Extrahiere den öffentlichen Schlüssel
public_key = gpg.export_keys(key.fingerprint)
print("Öffentlicher PGP-Schlüssel:\n", public_key)
