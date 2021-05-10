import paramiko
import os
from datetime import datetime
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ftspl.settings import mediapath, gpg, S_fp, C_fp


@csrf_exempt
def ecrtfil(request):
    resultfile = 'Please Post your Binary Data...'
    log = {'ftp': 'FTP Transfer : Failed'}
    if request.method == 'POST':
        f = str(request.body).split("'")[1]
        filestamp = "AIL_DFT_REQ_Jones_" + str(datetime.now().strftime("%Y%m%d%H%M%S%f")) + ".txt"
        resultfile = mediapath + '\\' + filestamp
        resultfile, log = ftecrt(f, resultfile, filestamp)

    return HttpResponse(resultfile, log)


# Encrypt & FTP
def ftecrt(data, filename, fname):
    remotepath = "//AARTIINDUSTRIE//"
    if C_fp:
        status = gpg.encrypt(data, recipients=C_fp, sign=S_fp, passphrase='pass1234',
                             armor=True, always_trust=True, output=filename)

        # SFTP Transfer
        HOSTNAME = "150.105.184.107"
        USERNAME = "AARTIINDUSTRIE"
        PASSWORD = "w0bo5qz9D0"

        ssh_transport = paramiko.Transport(HOSTNAME, 22)
        ssh_transport.connect(username=USERNAME, password=PASSWORD)

        sftp_session = paramiko.SFTPClient.from_transport(ssh_transport)
        # sftp_session.chdir(path='/TEST')

        dirlist = sftp_session.listdir(".")
        print("Dirlist: %s" % dirlist)

        sftp_session.put(filename, remotepath + fname, confirm=False)
        sftp_session.close()
        ssh_transport.close()
        log = {'ftp': 'FTP Transfer : Success'}

    return filename, log
