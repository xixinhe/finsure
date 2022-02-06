
from rest_framework.parsers import MultiPartParser
from rest_framework_csv.parsers import CSVParser

class CsvFileUploadParser(MultiPartParser):

    media_type = 'multipart/form-data'

    def parse(self, stream, media_type=None, parser_context=None):
        dataAndFiles = super().parse(stream, media_type=media_type, parser_context=parser_context)
        
        if 'file' in dataAndFiles.files:
            file = dataAndFiles.files['file']
            data = CSVParser().parse(stream=file)
            return data

