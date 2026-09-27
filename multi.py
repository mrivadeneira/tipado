from typing import Union

def multi_call(num:int , alt: bool = False ) -> int:
    if alt:
        return num * 5
    return num * -2


b = multi_call(23, True)


def multi_call_control(num: Union[init,float], alt: bool = False) -> Union[int,float]:
    assert isinstance(num, int), f"Invalid type :{type(num)}"
    if alt:
        return num * 5
    return num * -2
