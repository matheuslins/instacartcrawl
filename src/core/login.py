from bs4 import BeautifulSoup


class LoginHandler:
    response = None
    soup = None
    login_data = {}
    keys_to_extract = {}

    def start_login(self):
        self.soup = BeautifulSoup(self.response, 'html.parser')
        self.extract_values()

    def extract_values(self):
        for key, extraction_value in self.keys_to_extract.items():
            data = self.soup.find_all(**extraction_value["params"])
            data_extracted = extraction_value["method_to_extract"](data)
            self.login_data.update(
                **{key: data_extracted}
            )
