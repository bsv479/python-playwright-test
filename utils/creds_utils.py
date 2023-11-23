import json

from pydantic import ValidationError

from objects.register_creds import RegisterCreds


def save_creds(register_creds: RegisterCreds) -> None:
    with open('playwright/.auth/register_creds.json', 'w') as json_file:
        json.dump(register_creds.model_dump(), json_file)


def read_creds() -> RegisterCreds:
    with open('playwright/.auth/register_creds.json', 'r') as json_file:
        data = json.load(json_file)
        try:
            return RegisterCreds.model_validate(data)
        except ValidationError as e:
            print(e.errors())
