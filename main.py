from fastapi import FastAPI

app = FastAPI()

{
    "codigo": 123123,
    "descricao": "este e um produto teste",
    "preco": 40.00
}
produtos = []


@app.get('/api/v1/produtos')
def get_produtos():
    return produtos


@app.post('/api/v1/produtos')
def post_produtos(codigo: int, descricao: str, preco: float):
    
    try:
        
        produtos.append({
        "codigo": codigo,
        "descricao": descricao,
        "preco": preco
     })
        return {'status': 200}
    except:
        return {'status': 400}
    
@app.put('/api/v1/produtos')
def put_produtos(codigo: int, descricao: str, preco: float, new_data, tipo: str):
 
    if tipo == 'codigo':
        produtos.remove({
        "codigo": new_data,
        "descricao": descricao,
        "preco": preco
        })
    if tipo == 'descricao':
        produtos.remove({
        "codigo": codigo,
        "descricao": new_data,
        "preco": preco
     })
    if tipo == 'preco':
        produtos.remove({
        "codigo": codigo,
        "descricao": descricao,
        "preco": new_data
     })

@app.delete('/api/v1/produtos')
def delete_produtos():
    produtos.pop()