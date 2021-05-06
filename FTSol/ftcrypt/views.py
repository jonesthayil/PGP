from datetime import datetime
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ftspl.settings import DEBUG, mediapath, gpg, FTPHost, FTPUser, FTPPwd, FTPPort, FTPDir, KeyPhrase, S_fp, recipient, C_fp


@csrf_exempt
def ecrtfil(request):
    resultfile = 'Please Post your Binary Data...'
    ftpstatus = ''
    if request.method == 'POST':
        f = str(request.body).split("'")[1]
        g = request.body
        print(type(f),type(g))
        filestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        resultfile = mediapath + "\\" + str(filestamp) + ".gpg"
        resultfile, log = ftecrt(f, resultfile)
    return HttpResponse(resultfile, log)


# Encrypt & FTP
def ftecrt(data, filename):
    log = {'ftp': 'FTP Transfer : Success'}
    if C_fp:
        status = gpg.encrypt(data, recipients=C_fp, sign=S_fp, passphrase=KeyPhrase,
                             armor=False, always_trust=True, output=filename)
        if DEBUG: print("ok: \n", status.ok, "status: \n", status.status, "stderr: \n", status.stderr)
    else:
        print("error")
        log.update({'public Key': 'No Public Key Found. Please import keys...'})
    # ftp = FTP(FTPHost)
    # ftp.login(user=FTPUser, passwd=FTPPwd)
    # ftp.cwd(FTPDir)
    # ftp.storbinary('STOR ' + resultfile, open(resultfile, 'rb'))
    # ftp.quit()
    return filename, log
