import os, gnupg, glob
from datetime import datetime

smart_key = "pass1234"
rootpath = 'C:\\Users\\prashant\\Desktop\\PGP\\FTSol'
mediapath = rootpath + '\\media'
keypath = rootpath + '\\gnupg'
imppath = rootpath + '\\import_key'
resultfile = mediapath + '\\' + str(datetime.now().strftime("%Y%m%d%H%M%S%f")) + ".txt"

gpg = gnupg.GPG(gnupghome=keypath)
gpg.encoding = 'utf-8'
# S_fp = gpg.list_keys(True)[0]['fingerprint']
# print(S_fp)

for dirfiles in os.listdir(imppath):
    if dirfiles.endswith(".asc"):
        with open(imppath + '\\' + dirfiles, 'r') as file:
            f = file.read()
            imported_key = gpg.import_keys(f)
            print(imported_key)
gpg.trust_keys(gpg.list_keys()[1]['fingerprint'], 'TRUST_FULLY')

ext = ('.gpg',)
for dirfile in os.listdir(mediapath):
    if dirfile.endswith(ext):
        with open(mediapath + '\\' + dirfile, 'rb') as file:
            data = file.read()
            decrypted_data = gpg.decrypt(data, always_trust=True, passphrase=smart_key)
            status = gpg.decrypt(data, passphrase=smart_key, output=resultfile)
            
