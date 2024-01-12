import boto3
import json
from .models import Pessoa

class PessoaService:

    @staticmethod
    def get_all():
        return Pessoa.objects.all()
    
    @staticmethod
    def create_pessoa(validated_data):
        pessoa =  Pessoa.objects.create(**validated_data)
        lambda_response = PessoaService.invoke_lambda(validated_data)
        return lambda_response
    
    @staticmethod
    def invoke_lambda(data):
        lambda_client = boto3.client("lambda", 
                                     region_name="sa-east-1",
                                     aws_access_key_id="",
                                     aws_secret_access_key=""
                                     )
        response = lambda_client.invoke(
            FunctionName="",
            InvocationType="RequestResponse",
            Payload=json.dumps(data),
        )
        response_payload = json.load(response["Payload"])
        return response_payload
