from ftspl.settings import mediapath, gpg, Email, ftp
from django.http import HttpResponse
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FTCRYPT
import gnupg


def ecrtfile(request):
    filename = '\\terms.txt'
    with open(mediapath+filename, 'rb') as f:
        resultfile = mediapath+filename.split(".")[0]+".encrypted"
        status = gpg.encrypt_file(f, recipients=[Email], output=resultfile)
        print(status.ok)
        print(status.stderr)
    # ftp.storbinary('STOR ' + resultfile, open(resultfile, 'rb'))
    # ftp.quit()
    return HttpResponse('completed')


class MyUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, filename, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")
        else:
            file_obj = request.data['file']
        obj = FTCRYPT.postfile.save(filename, file_obj, save=True)
        print(obj)
        return Response(status=204)
    
    def post(self, request, filename, format=None):
        file_obj = request.FILES['file']
        obj = FTCRYPT.postfile.save(filename, file_obj, save=True)
        return Response(status=204)