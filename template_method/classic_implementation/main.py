from template_method.classic_implementation.client_code import PdfDataProcessor, CsvDataProcessor

if __name__ == '__main__':
    # pdf data process
    PdfDataProcessor().process_data()

    # csv data process
    CsvDataProcessor().process_data()
