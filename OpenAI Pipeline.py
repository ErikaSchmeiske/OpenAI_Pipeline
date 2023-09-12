# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 22:15:40 2023

@author: Erika
"""

#ETAPA DE EXTRAÇÃO
#TO DO = extrair os dados de um arquivo CSV

import pandas as pd
import requests
import json



df = pd.read_csv("nome do arquivo CSV")

user_ids = df["esclher coluna"].tolist()

print(user_ids)

#obter os dados

#Recuerar os dados do usuário

def get_user(id):
    response = requests.get(f"{nome da url ou endponit}/ID desejado")
    return response.json() if response.status_code == 200
    else None
    
user = [user for id in user_ids if (user := get_user(id)) is not None] #expressão de atribuição
print(json.dumps(users, ident=2))

#TRANSFORMAÇÃO

import openai

#Usando IA para gerar uma mensagem individual para cada usuário

#pip instal openai

openai_api_key = "colocar a chave de api pessoal" #atribui a chave de API

openai.api_key = openai_api_key

def generate_ai_news(user):
    
    #copiar o código direto do site da documentação da OpenAI

responseChatGPT = completion.choices[0].message.content.strip('\"')

for user in users:
    news = generate_ai_news(user)
    print(user)
    user['news'].append(
        #atribuição do que quiser
        "description": news
        )


#ETAPA DE CARREGAMENTO (LOAD)

#atualizar os dados

def update_user(user):
    response = requests.put(f"{url desejada}/users/id", json = user)
    return True if response.status_code == 200
    else False

for user in users:
    success = update_user(user)
    print(f"User {user['name']} updated? {success}!")
    
    



        
    