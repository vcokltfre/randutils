from random import choices
from typing import List

default_charset = "0123456789abcdef"

def replace(text: str, content: List[str], letter: str = "x"):
    output = ""
    for l in text:
        if l == letter:
            output += content.pop(0)
        else:
            output += l
    return output

def randomstring(length: int, charset: str = default_charset, as_list: bool = False) -> str:
    items = choices(charset, k=length)
    if not as_list:
        return "".join(items)
    return items

def formatstring(text: str, letter: str = "x", charset: str = default_charset) -> str:
    return replace(text, randomstring(text.count(letter), as_list=True))
