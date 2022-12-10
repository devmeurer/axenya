import json
import requests

class ViaCepRequest:
    def get_cep_by_address(self, UF, cidade, rua):
        url = "http://viacep.com.br/ws/{}/{}/{}/json/".format(UF, cidade, rua)
        response = requests.get(url)
        
        return json.loads(response.text)
