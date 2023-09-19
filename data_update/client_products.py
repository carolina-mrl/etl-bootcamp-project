import json
import openai


API_KEY = "insira_sua_api_key_aqui"
openai.api_key = API_KEY


def read_database():
    with open("data/clients_data.json") as file:
        read_file = json.load(file)
        return read_file


def generate_ai_news(client):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": "Você é um vendedor de uma loja de brinquedos",
            },
            {
                "role": "user",
                "content": f"Gere uma lista de produtos para um cliente de {client['age']} anos",
            },
        ],
    )

    return completion.choices[0].message.content.strip("\'")


def update_database():
    client_list = read_database()
    for client in client_list:
        products_list = generate_ai_news(client)
        client["suggested_products"] = products_list

    with open("data/clients_data.json", "w") as file:
        json_to_write = json.dumps(client_list, indent=2)
        file.write(json_to_write)


update_database()
