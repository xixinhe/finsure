from .serializers import LenderSerializer, CsvDownloadSerializer, CsvUploadSerializer
from .models import Lender
from rest_framework import viewsets
from rest_framework import generics, mixins
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_csv import renderers as r
from rest_framework.response import Response
from .renderers import LenderCsvRenderer
from rest_framework_csv.parsers import CSVParser
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework import status
from django.http import HttpResponse
from .parsers import CsvFileUploadParser
# Create your views here.

class LenderViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['active']

    serializer_class = LenderSerializer
    queryset = Lender.objects.all()

class CsvDownloadView(generics.ListAPIView):
    renderer_classes = [LenderCsvRenderer]
    parser_classes = [FileUploadParser]
    serializer_class = CsvDownloadSerializer

    queryset = Lender.objects.all()

    def get(self, request):
        lenders = self.get_queryset()
        serializer = self.get_serializer(lenders, many=True)
        return Response(serializer.data, 
                        content_type='text/csv', 
                        headers={
                            'Content-disposition': 'attachment;filename=lenders.csv'
                            })

class CsvUploadView(generics.CreateAPIView):
    parser_classes = [CsvFileUploadParser]
    serializer_class = CsvUploadSerializer

    def post(self, request):
        serializer = CsvDownloadSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
