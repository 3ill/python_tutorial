---
title: 
tags: 
type: 
author: 
creationDate: 
alias:
---

>[!summary] 
>In Python, the double underscore (`__`) is used for special variables and methods, often called "dunder" (double underscore) name


```python
def main():
    print("Hello from fast-api-tutorial!")


if __name__ == "__main__":
    main()

```


- `__name__` is a special built-in variable in Python.
- When a Python file is run directly, `__name__` is set to `"__main__"`.
- If the file is imported as a module in another script, `__name__` will be set to the module's name (the filename, without `.py`).

>[!important] 
This pattern is commonly used to ensure that certain code only runs when the file is executed directly, not when it is imported elsewhere. For example, you might put test code or the main entry point of your application inside this block.

##### Go Back: [[05- Arithmetic]]

##### Up Next: [[07-Imports and project structure]]
