# template function (template method)
def process_data(
        getter: callable,
        encoder: callable,
        saver: callable,
        logger: callable = print,  # default implementation
) -> None:
    data = getter()
    logger(f"Got `{data}`")

    encoded_data = encoder(data)
    saver(encoded_data)

    logger(f"`{data}` was processed")
