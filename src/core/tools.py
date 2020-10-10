

def parse_cookies(cookies):
    new_cookies = []

    for _, cookie in cookies.items():
        parsed_cookie = f"{cookie.key}={cookie.value}"
        new_cookies.append(parsed_cookie)

    return ";".join(new_cookies)
