import logging

from template_method.python_implementation.client_code import get_pdf, save_pdf_to_db, encode_to_utf_8, get_csv, \
    save_csv_to_db
from template_method.python_implementation.module import process_data

if __name__ == '__main__':
    # pdf data process
    process_data(
        get_pdf,
        encode_to_utf_8,
        save_pdf_to_db,
    )

    # csv data process
    log = logging.getLogger('csv')
    log.setLevel(logging.DEBUG)
    log.addHandler(logging.StreamHandler())

    process_data(
        get_csv,
        encode_to_utf_8,
        save_csv_to_db,
        logger=log.info,
    )
