from ftspl.settings import mediapath, gpg, Email, ftp
from django.http import HttpResponse
from .models import FTCRYPT
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.core.files import File
from .serializers import FTCRYPTSerializer
import gnupg
import os


class ECRTFILE(APIView):
	parser_classes = (MultiPartParser, FormParser)

	def post(self, request, *args, **kwargs):
		file_serializer = FTCRYPTSerializer(data=request.data)
		if file_serializer.is_valid():
			obj = file_serializer.save()
			ecrtfile = ftecrt('\\'+str(obj))
			os.remove(ecrtfile)
			obj.delete()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Encrypt & FTP
def ftecrt(filename):
	with open(mediapath+filename, 'rb') as f:
		resultfile = mediapath+filename.split(".")[0]+".encrypted"
		status = gpg.encrypt_file(
			f, recipients=[Email], output=resultfile)
		print(status.ok)
		print(status.stderr)
	# ftp.storbinary('STOR ' + resultfile, open(resultfile, 'rb'))
	# ftp.quit()
	return str(resultfile)
