from pydantic import BaseModel, ValidationError, field_validator


class UserModel(BaseModel):
    name: str
    username: str

    @field_validator('name')
    def name_must_contain_carlitos(cls, v):
        if 'carlitos' not in v.lower():
            raise ValueError('only carlitos allowed!')
        return v.title()


user = UserModel(
    name='Carlitos el incorruptible',
    username='charlie123',
)
print(user)


try:
    UserModel(
        name='Otro Nombre',
        username='humai123',
    )
except ValidationError as e:
    print(e)
