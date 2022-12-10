from fastapi import FastAPI

from app.services.via_cep_validation import ViaCepValidation

app = FastAPI()

viacep = ViaCepValidation()

@app.post("/validate/cep")
def read_item(
    UF,
    cidade,
    rua,
):
    result = viacep.create_route(UF, cidade, rua)
    return result
