def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """ Print a string centred, with ** either side.

    :param text: The string to print.
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border at
        the left and right edges.
    :param screen_width: The overall width to print within
        (including the 4 spaces for the ** either side).
    :raises ValueError: if the supplied string is too long to fit.
    """
    if len(text) > screen_width - 4:
        raise ValueError(f"String {text} is larger then specified width {screen_width}")

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{}**".format(text.center(screen_width - 4))
        print(output_string)


width = 60
banner_text("*", width)
banner_text("Testing all this logic to make sure", width)
banner_text("My love of programming never", width)
banner_text(screen_width=width)
banner_text("fades into the dust", width)
banner_text("*", width)
