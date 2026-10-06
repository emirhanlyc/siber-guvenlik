from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os


sifreleyici = AESGCM(AESGCM.generate_key(bit_length=128))


rastgele_deger = os.urandom(12) 


sifreli_mesaj = sifreleyici.encrypt(rastgele_deger, b"Tutar: 100 TL", None)

orijinal_mesaj = sifreleyici.decrypt(rastgele_deger, sifreli_mesaj, None)


print("Çözülen mesaj:", orijinal_mesaj.decode())