from typing import List
from .pdf_class import PdfClass

def merge_write_pdfs(destination_file_path: str, pdf_file_paths: List[str]) -> None:
  list(map(validate_path, pdf_file_paths))
  from PyPDF3 import PdfFileMerger, PdfFileReader

  merger = PdfFileMerger()
  for pdf_reader in ([PdfFileReader(pdf) for pdf in pdf_file_paths]):
    merger.append(pdf_reader)

  return merger.write(destination_file_path)


def convert_png_to_pdf(source_file_path:str, destination_file_path: str) -> None:
  validate_path(source_file_path)

  from PIL import Image
  image = Image.open(source_file_path)
  converted = image.convert('RGB')
  converted.save(destination_file_path)


def validate_path(path:str) -> None:
  from pathlib import Path
  file = Path(path)
  if not file.is_file():
    raise FileNotFoundError(f'{path} did not contain a file.')
