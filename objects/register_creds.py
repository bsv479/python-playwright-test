from pydantic import BaseModel


class RegisterCreds(BaseModel):
    first_name: str
    last_name: str
    address: str
    city: str
    state: str
    zip_code: str
    phone: str
    ssn: str
    username: str
    password: str
