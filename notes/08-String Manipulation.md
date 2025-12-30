---
title: 
tags: 
type: 
author: 
creationDate: 
alias:
---

>[!summary] 
>_This note outlines how to manipulate characters of string type_

#### Length

>[!note] 
>This returns the number of characters in a string

```python
# String Manipulation
newString = "I am learning python, i am liking it"
stringLength = len(newString)

print(stringLength)
```

___

#### Slice
In python it is possible to extract characters and return as a new string
```python
newString = "I am learning python, i am liking it"

# Slice
print(newString[0:3])
```


>[!note] 
>This will return the first three characters, the 3rd character is non inclusive, so if we wanted to return the first 4 characters, the last index will be 5. **If the end index is not included it will return the entire string**

___
#### Escape sequence
In Python, an escape sequence is a way to include special characters in a string that would otherwise be difficult or impossible to type directly. Escape sequences start with a backslash (`\`), followed by a character that has a special meaning.

```python
# Escape sequence
course = "\"Python\"Programming"
print(course)
```

>[!note] 
>The `\"` is an escape sequence. It tells Python to include a double quote character (`"`) inside the string, rather than treating it as the end of the string. Without the backslashes, Python would get confused about where the string starts and ends.

The returned value will be
```Shell
"Python"Programming
```

Here are a few common escape sequences in Python:

- `\"` – Double quote
- `\'` – Single quote
- `\\` – Backslash
- `\n` – Newline (line break)
- `\t` – Tab
___
#### Concatenation
concatenation is a way of joining two strings together
```python
first = "Chike"
last = "Egbu"

full = first + " " + last
print(full)
```

#### Formatted string
This is a better way of joining values together and returning a string, the expression is evaluated at run time
```python
first = "Chike"
last = "Egbu"

# Formatted Strings
formatted_full = f"{first} {last}"
print(formatted_full)
```

___

### String methods
1. `lower()`
Converts all characters to lowercase.
```/dev/null/example.py#L1-2
text = "Hello World"
print(text.lower())  # Output: hello world
```

---

### 2. `upper()`
Converts all characters to uppercase.
```python
text = "Hello World"
print(text.upper())  # Output: HELLO WORLD
```

---

### 3. `capitalize()`
Capitalizes the first character of the string.
```python
text = "hello world"
print(text.capitalize())  # Output: Hello world
```

---

### 4. `title()`
Capitalizes the first character of each word.
```python
text = "hello world"
print(text.title())  # Output: Hello World
```

---

### 5. `strip()`
Removes leading and trailing whitespace.
```python
text = "  hello world  "
print(text.strip())  # Output: hello world
```

---

### 6. `replace(old, new)`
Replaces all occurrences of a substring with another.
```python
text = "banana"
print(text.replace("a", "o"))  # Output: bonono
```

---

### 7. `find(sub[, start[, end]])`
Returns the lowest index where the substring is found, or -1 if not found.
```python
text = "hello world"
print(text.find("world"))  # Output: 6
```

---

### 8. `count(sub[, start[, end]])`
Counts the number of occurrences of a substring.
```python
text = "banana"
print(text.count("a"))  # Output: 3
```

---

### 9. `startswith(prefix[, start[, end]])`
Checks if the string starts with the specified prefix.
```/dev/null/example.py#L1-2
text = "hello world"
print(text.startswith("hello"))  # Output: True
```

---

### 10. `endswith(suffix[, start[, end]])`
Checks if the string ends with the specified suffix.
```/dev/null/example.py#L1-2
text = "hello world"
print(text.endswith("world"))  # Output: True
```

---

### 11. `split(sep=None, maxsplit=-1)`
Splits the string into a list using the specified separator.
```/dev/null/example.py#L1-2
text = "a,b,c"
print(text.split(","))  # Output: ['a', 'b', 'c']
```

---

### 12. `join(iterable)`
Joins elements of an iterable into a single string, separated by the string.
```/dev/null/example.py#L1-2
words = ["hello", "world"]
print(" ".join(words))  # Output: hello world
```

---

### 13. `isalpha()`
Returns True if all characters are alphabetic.
```/dev/null/example.py#L1-2
text = "abc"
print(text.isalpha())  # Output: True
```

---

### 14. `isdigit()`
Returns True if all characters are digits.
```/dev/null/example.py#L1-2
text = "123"
print(text.isdigit())  # Output: True
```

---

### 15. `isalnum()`
Returns True if all characters are alphanumeric (letters or numbers).
```/dev/null/example.py#L1-2
text = "abc123"
print(text.isalnum())  # Output: True
```

---

### 16. `islower()`
Returns True if all characters are lowercase.
```/dev/null/example.py#L1-2
text = "hello"
print(text.islower())  # Output: True
```

---

### 17. `isupper()`
Returns True if all characters are uppercase.
```/dev/null/example.py#L1-2
text = "HELLO"
print(text.isupper())  # Output: True
```

---

### 18. `center(width[, fillchar])`
Centers the string in a field of given width.
```python
text = "hi"
print(text.center(6, "-"))  # Output: --hi
```

___

#### in
>[!note] 
>Another important keyword to note is the `in` keyword it evaluates if a character exist in a string and returns a boolean

```python
random_string = " Chike Egbu "

print("Chike" in random_string) #Output: true
```


#### not in
This is the opposite of in
```python
random_string = " Chike Egbu "

print("Chike" not in random_string) #Output: false
```



##### Go Back: [[07-Imports and project structure]]
##### Up Next: [[09-Number manipulation]]