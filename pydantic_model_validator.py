from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    a: str
    b: str


    class ConfigDict:
        str_max_length = 10
        #error_msg_templates = {
        #    'value_error.any_str.max_length': 'max_length:{limit_value}',
        #}


try:
    Model(a='x' * 5, b='y' * 15)
except ValidationError as e:
    print(e)
