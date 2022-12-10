from app.services.via_cep_requests import ViaCepRequest


class ViaCepValidation:
    def __init__(self):
        self.viacep = ViaCepRequest()
    
    def validate_array_cep(self, UF, cidade, rua):
        result = self.viacep.get_cep_by_address(UF, cidade, rua)
        list = []
        for item in result:
            cep = item['cep']
            list.append(cep)
        return list
    
    def create_route(self, UF, cidade, rua):
        list = self.validate_array_cep(UF, cidade, rua)
        list_of_result = []
        for cep_initial in list:
            payload = {
                "Cidade": cidade,
                "Partida": cep_initial,
            }
            for cep_final in list:
                if cep_initial != cep_final:
                    payload["Destino"] = cep_final
                    list_of_result.append(payload)
            
        return list_of_result