from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from .forms import FileUploaderForm
from .serializers import FileUploaderSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from .models import FileUploader
from .auth import CsrfExemptSessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework import viewsets

import pyexcel


class FileUploadView(APIView):
    serializer_class = FileUploaderSerializer
    parser_classes = (MultiPartParser, FormParser,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    queryset = FileUploader.objects.all().order_by('-upload_date')

    def get(self, request, graphId):
        print(request.data)
        if FileUploader.objects.last() is None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        if graphId < 1:
            path = FileUploader.objects.last().file.path
        else:
            path = FileUploader.objects.filter(id=graphId).last().file.path
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

    def post(self, request, graphId):
        form = FileUploaderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("File uploaded successfully")
        else:
            return HttpResponse("File upload error")

class GraphListView(APIView):
    serializer_class = FileUploaderSerializer    

    def get(self, request):
        queryset = FileUploader.objects.all().order_by('-upload_date')
        serializer = FileUploaderSerializer(queryset, many=True)
        list_data = list(queryset)
        print(list_data)
        return Response(serializer.data)

@api_view(['GET'])
def getGraphList(request):
    print(request.data)
    data = list(FileUploader.objects.all().order_by('-upload_date').values('id', 'file', 'upload_date'))
    for graph in data:
        graph['file'] = graph['file'].split("/")[1]
        graph['upload_date'] = graph['upload_date'].strftime("%d/%m/%Y %H:%M:%S")
    return Response(data)