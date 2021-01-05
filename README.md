# vcokltfre/randutils

## A collection of utilities to work with random data, usually text.

Example usage:
```py
from randutils import randomstring, formatstring

print(randomstring(16))
print(randomstring(16, charset="abcd"))
print(randomstring(16, as_list=True))
print(formatstring("xxxx-xxxxxxxx-xxxx"))
```

# List of functions:

### `randomstring(length: int, charset: str = default_charset, as_list: bool = False) -> str`
---
### `formatstring(text: str, letter: str = "x", charset: str = default_charset) -> str`

---

### Why does this repo exist?
Put simply, I needed these random utils for a project and didn't feel like spending a long time Googling for libs that probably wouldnt do exactly what I wanted with an obscure name.