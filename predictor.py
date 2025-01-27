import google.generativeai as genai
from dotenv import load_dotenv
import os


def get_ingredients(image, key):
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(["""Liste quais são os ingredientes da imagem.
    Os ingredientes devem ser apresentados em uma lista separada por vírgula, como no exemplo a seguir.
    Nenhum texto adicional deve ser gerado como resposta além dos próprios ingredientes.
    # Exemplo de saída
    arroz, pimentão, feijão 
    """, image])
    print(response.text)

    return response.text


def get_possible_recipes(ingredientes, key):
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"""Considerando a seguinte lista de ingredientes, gere uma lista de receitas culinárias que os utilizem.
    As receitas devem tentar incluir a maior parte dos ingredientes.
    Gere apenas uma lista com os nomes das receitas, separados por vírgula. 
    
    # Lista de ingredientes
    {ingredientes}
    
    # Exemplo de saída
    Receita 1, Receita 2, Receita 3
    """)
    print(response.text)
    return response.text


def get_full_recipes(ingredientes, receita, key):
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"""Crie a receita para o prato '{receita}'.
    Inclua a maior quantidade possível dos ingredientes da lista de ingredientes.
    
    # Lista de ingredientes
    {ingredientes}
    """)
    print(response.text)
    return response.text


