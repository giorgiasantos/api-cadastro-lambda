from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pessoa
from .serializers import PessoaSerializer
from .services import PessoaService

@api_view(["GET", "POST"])
def pessoa_list(request):
    if request.method == "GET":
        pessoas = PessoaService.get_all()
        serializer = PessoaSerializer(pessoas, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = PessoaSerializer(data=request.data)
        if serializer.is_valid():
            pessoa = PessoaService.create_pessoa(serializer.validated_data)
            return Response(pessoa, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
