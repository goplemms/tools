class PdfClass:
    def __init__(self, file_path=None):
        from PyPDF3 import PdfFileReader
        self.__file_path = file_path
        self.__pdf = PdfFileReader(self.__file_path)


    def write(self, file_path:str):
        from PyPDF3 import PdfFileWriter
        PdfFileWriter().write(self.__pdf.stream)
