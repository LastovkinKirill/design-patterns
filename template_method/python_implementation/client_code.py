# pdf data process
def get_pdf() -> str:
    return "pdf data"


def save_pdf_to_db(data: bytes) -> None:
    print(f"[SAVE PDF] {data} to db")


# csv data process
def get_csv() -> str:
    return "csv data"


def save_csv_to_db(data: bytes) -> None:
    print(f"[SAVE CSV] {data} to db")


# encoders
def encode_to_utf_8(data: str) -> bytes:
    return data.encode("utf-8")
