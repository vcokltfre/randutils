# vcokltfre/randutils

## A collection of utilities to work with random data, usually text.

Example usage:
```py
from randutils import randomstring, formatstring

print(randomstring(16))
print(randomstring(16, charset="abcd"))
print(randomstring(16, as_list=True))
print(fromatstring("xxxx-xxxxxxxx-xxxx"))
```

# List of functions:

### `randomstring(length: int, charset: str = default_charset, as_list: bool = False) -> str`
---
### ``