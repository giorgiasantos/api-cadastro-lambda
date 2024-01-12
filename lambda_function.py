import json

def lambda_handler(event, context):
    
    nome = event.get("nome")
    email = event.get("email")
    idade = event.get("idade")

    response = {
        "statusCode": 201,
        "body": json.dumps({
            "message": "Cadastro realizado com sucesso!"
        })
    }
    return response