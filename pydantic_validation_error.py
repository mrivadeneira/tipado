from pydantic import ValidationError

external_data = {'id': 'Carlitos el Corrupto', 'signup_ts': 'ayer', 'friends': ["asd"]}
try:
    user = User(**external_data)
except ValidationError as e:
    print(e.json())
