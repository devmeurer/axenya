## Stack utilizada
**Back-end:** Python3.9, FastAPI, Uvicorn, Docker

##  Rodando localmente
```bash
docker-compose up --build
```
## Parar
```
docker-compose down
```
## Swagger do projeto
```
 http://0.0.0.0:8000/docs#/
```
## Dados passados na rota
```
uf: string
cidade: string
rua: string
```
## Rota

exemplo curl
```curl -X 'POST' \
  'http://0.0.0.0:8000/validate/cep?UF=sc&cidade=florianopolis&rua=venezuela' \
  -H 'accept: application/json' \
  -d ''
```


## Autor  

- [@eltonmeurer](https://www.linkedin.com/in/elton-meurer-174191229/)

