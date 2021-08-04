def xor(condition1, condition2) -> bool:
    """
    XOR (Exclusive OR) Function.
    If one of the provided conditions is true, return True,
    if both are true, return False.
    :param condition1:
    :param condition2:
    :return:
    """
    if condition1 and condition2:
        return False
    if condition1 or condition2:
        return True


def join_urls(url1, url2) -> str:
    """
    Joins 2 paths (specifically URLs) together neatly.
    If url1 is "https://test.com/"
    and url2 is "/admin/login/", the method will return
    "https://test.com/admin/login/". and won't give you double
    forward slashes like it would if you were just
    combining the 2 paths: https://test.com//admin/login

    :param url1:
    :param url2:
    :return:
    """

    if xor(url1[-1] == "/", url2[0] == "/"):
        # If one but not both of the urls have a "/"
        # return the URLs combined.
        return url1 + url2
    elif url1[-1] != "/" and url2[0] != "/":
        # If neither of the URLs have a "/", add one between them.
        return f"{url1}/{url2}"
    else:
        # Both URLs have a "/", remove the "/" from the first
        # URL and return the URLs combined
        return url1[:-1] + url2


def stringify(lst, separator=None) -> str:
    """
    This function takes a list and returns all of the
    list items chained together in a string.
    You can optionally provide a separator to separate
    each list item when it's in the string
    :param lst:
    :param separator:
    :return:
    """
    out_str = ""
    for item in lst:
        # This if statement checks to see if the current list item
        # is the last item in the list. If it is, don't add the separator
        # to the end of the string.
        if lst.index(item) == len(lst) - 1:
            out_str += str(item)
        else:
            # Otherwise just add the separator the string.
            out_str += str(item) + separator
    return out_str


def get_last_url_char(url) -> str:
    """
    This function gets the last character in a URL;
    :param url:
    :return:
    """
    for i in range(1, len(url)):
        char = url[-i]
        if char != "/":
            return char


def parse_name(name) -> str:
    """
    Removes the parentheses from the end of the player name.
    :param name:
    :return:
    """
    parsed_name = ""
    i = 0
    while i <= len(name):
        char = name[i]
        if char == "(":
            return remove_trailing_whitespace(parsed_name)
        else:
            parsed_name += char
        i += 1
    return remove_trailing_whitespace(parsed_name)


def remove_trailing_whitespace(string) -> str:
    """
    Removes trailing whitespace from the end of a string
    :param string:
    :return:
    """
    string_list = list(string)
    while string_list[-1] == " ":
        string_list[-1] = ""
    return stringify(string_list, "")
