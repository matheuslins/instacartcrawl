import re


def parse_cookies(cookies):
    new_cookies = []

    for _, cookie in cookies.items():
        parsed_cookie = f"{cookie.key}={cookie.value}"
        new_cookies.append(parsed_cookie)

    return ";".join(new_cookies)


def remove_special_chars(element):
    clean_string = re.findall(r'\w+', element)
    return '-'.join([e.lower() for e in clean_string])
