from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from ftspl.settings import mediapath, gpg, Email, ftp
from .serializers import FTCRYPTSerializer


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
    with open(mediapath + filename, 'rb') as f:
        resultfile = mediapath + filename.split(".")[0] + ".encrypted"
        status = gpg.encrypt_file(
            f, recipients=[Email], output=resultfile)
        print(status.ok)
        print(status.stderr)
    # ftp.storbinary('STOR ' + resultfile, open(resultfile, 'rb'))
    # ftp.quit()
    return str(resultfile)
