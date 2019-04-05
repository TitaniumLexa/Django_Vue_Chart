from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from .forms import FileUploaderForm
from .serializers import FileUploaderSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from .models import FileUploader
from .auth import CsrfExemptSessionAuthentication
from rest_framework.authentication import BasicAuthentication

import pyexcel


class FileUploadView(APIView):
    serializer_class = FileUploaderSerializer
    parser_classes = (MultiPartParser, FormParser,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    queryset = FileUploader.objects.all().order_by('-upload_date')

    def get(self, request):
        if FileUploader.objects.last() is None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        path = FileUploader.objects.last().file.path

        # Excel Parsing, cleaning from empty rows and cells
        excel_data = pyexcel.get_array(file_name=path)
        excel_data = [list(filter(None, el)) for el in excel_data]
        excel_data = list(filter(None, excel_data))
        excel_data.pop(0)

        # Checking number of columns
        testdata = []
        if excel_data[0].__len__() == 2:
            for (i, row) in enumerate(excel_data):
                testdata.append(dict(x=row[0], y=row[1]))
        else:
            if excel_data[0].__len__() == 1:
                for (i, row) in enumerate(excel_data):
                    testdata.append(dict(x=i, y=row[0]))
        resEx = dict(points=testdata)
        return Response(resEx, status=status.HTTP_200_OK)

    def post(self, request):
        form = FileUploaderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("File uploaded successfully")
        else:
            return HttpResponse("File upload error")
