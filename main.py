if __name__ == '__main__':
    from pdf import convert_png_to_pdf, merge_write_pdfs

    png_root = r""

    pdf_root = r""

    file_names = [(f'{png_root} {s}', f'{pdf_root} {s}') for s in range(1,20)]

    converted_pdf_paths = []
    for (source_file_path, destination_file_path) in file_names:
        source_png_path = source_file_path + '.png'
        converted_pdf_path = destination_file_path + '.pdf'
        converted_pdf_paths.append(converted_pdf_path)
        convert_png_to_pdf(source_file_path=source_png_path,destination_file_path= converted_pdf_path)

    merged_file_path = f''
    merge_write_pdfs(merged_file_path, converted_pdf_paths)
