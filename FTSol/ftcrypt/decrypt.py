import gnupg
import os

gpg = gnupg.GPG(gnupghome='C:\\Users\\prashant\\Desktop\\PGP\\FTSol\\gnupg')
gpg.encoding = 'utf-8'
mediapath = 'C:\\Users\\prashant\\Desktop\\PGP\\FTSol\\media'
C_Passkey = 'Pass@123'
ext = ('.gpg',)
resultfile = mediapath + '\\signatures\\term.txt'
for fily in os.listdir('C:\\Users\\prashant\\Desktop\\PGP\\FTSol\\media\\encrypted'):
    if fily.endswith(ext):
        with open(mediapath + '\\encrypted\\' + fily, 'r') as file:
            f = file.read()
decrypted_data = gpg.decrypt(f, passphrase=C_Passkey)
if decrypted_data.trust_level is not None and decrypted_data.trust_level >= decrypted_data.TRUST_FULLY:
    status = gpg.decrypt(f, passphrase=C_Passkey, output=resultfile)
    print(status.ok)
    print(status.stderr)
