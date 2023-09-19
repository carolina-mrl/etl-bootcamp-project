from faker import Faker
import json


def create_fake_data():
    n = input("Quantos clientes deseja criar? ")
    faker = Faker(locale="pt_BR")
    clients = []
    for i in range(1, int(n)+1):
        clients.append(
            {
                "client_code": f"000{i}",
                "name": faker.name(),
                "age": faker.random_int(min=0, max=15),
            }
        )
    return clients


def create_json():
    accounts = create_fake_data()
    with open("data/clients_data.json", "w") as file:
        json_to_write = json.dumps(accounts, indent=2)
        file.write(json_to_write)


create_json()
