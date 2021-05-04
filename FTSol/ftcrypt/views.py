from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from ftspl.settings import mediapath, gpg, C_Email, ftp, S_Key, S_Key, S_Passkey
from .serializers import FTCRYPTSerializer
import os
import gnupg

class ECRTFILE(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FTCRYPTSerializer(data=request.data)
        if file_serializer.is_valid():
            obj = file_serializer.save()
            ecrtfile = ftecrt('\\' + str(obj))
            # os.remove(ecrtfile)
            obj.delete()
            return Response(ecrtfile, status=status.HTTP_200_OK)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Encrypt & FTP
def ftecrt(filename):
    sigfile = mediapath + "\\signatures" + filename.split(".")[0] + ".sig"
    resultfile = mediapath + "\\encrypted" + filename.split(".")[0] + ".gpg"
    f = ''
    with open(mediapath + filename, 'r') as file:
        f = file.read()
    status = gpg.encrypt(f, recipients=[C_Email], sign=S_Key, passphrase=S_Passkey,output=resultfile)
    print("ok: ", status.ok)
    print("status: ", status.status)
    print("stderr: ", status.stderr)
    # ftp.storbinary('STOR ' + resultfile, open(resultfile, 'rb'))
    # ftp.quit()
    return str(resultfile)
