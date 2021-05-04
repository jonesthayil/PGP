from FTSol.ftspl.settings import mediapath, gpg, Passkey
import os


ext = ('.encrypted',)

for files in os.listdir(mediapath):
    if files.endswith(ext):
        print(files)  # printing file name of desired extension
        with open(mediapath + '\\' + files, 'rb') as f:
            resultfile = mediapath + '\\' + files.split(".")[0] + ".txt"
            status = gpg.decrypt_file(f, passphrase=Passkey, output=resultfile)
            print(status.ok)
            print(status.stderr)
    else:
        continue
