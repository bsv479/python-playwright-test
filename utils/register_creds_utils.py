import json
import random

from faker import Faker
from pydantic import ValidationError

from objects.register_creds import RegisterCreds

REGISTER_CREDS_JSON = 'tests/e2e/playwright/.auth/register_creds.json'


def save_register_creds(register_creds: RegisterCreds) -> None:
    with open(REGISTER_CREDS_JSON, 'w') as json_file:
        json.dump(register_creds.model_dump(), json_file)


def read_register_creds() -> RegisterCreds:
    with open(REGISTER_CREDS_JSON, 'r') as json_file:
        data = json.load(json_file)
        try:
            return RegisterCreds.model_validate(data)
        except ValidationError as e:
            print(e.errors())


def get_random_register_creds() -> RegisterCreds:
    faker = Faker()
    first_name = faker.first_name()
    last_name = faker.last_name()
    login_name = f"{first_name}-{last_name}_{random.randint(1, 999)}"
    email = f"{login_name}@fakemail.com"
    return RegisterCreds(
        first_name=first_name,
        last_name=last_name,
        email=email,
        address_1=faker.address(),
        address_2=faker.address(),
        phone=faker.basic_phone_number(),
        company=faker.company(),
        fax=faker.basic_phone_number(),
        city=faker.city(),
        zip_code=faker.zipcode(),
        login_name=login_name,
        password=faker.password(),
    )
