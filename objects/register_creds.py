from pydantic import BaseModel


class RegisterCreds(BaseModel):
    first_name: str
    last_name: str
    email: str
    address_1: str
    address_2: str
    city: str
    zip_code: str
    phone: str
    fax: str
    login_name: str
    password: str
    company: str
