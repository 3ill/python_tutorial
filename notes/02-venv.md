---
title: creating venv
tags:
  - code
  - note
  - python
type: note
author: 3ilBaby
creationDate: 2025-01-02T21:41:00
aliases:
---

> [!NOTE] Overview
> This note shows how and why to use venv 

`venv` or virtual environment is an isolated environment that holds its own instance of python, compiler and interpreter. this is useful for isolating large projects to prevent dependency issues. 

#### Why use a venv
- **Dependency Management**: Different projects may require different versions of the same library. For example, if Project A uses Django 4.0 and Project B uses Django 4.1, installing them globally could lead to conflicts. A venv allows you to install each version in its isolated environment
- **Avoiding System Python Issues**: Most Linux systems come with a pre-installed Python version that is used by system utilities. Modifying this system Python (e.g., by installing packages globally) can lead to system instability or corruption. Using a venv ensures that you do not interfere with the system Python
- **Project Isolation**: Each project can have its own dependencies without affecting others, making it easier to manage multiple projects simultaneously

### Create  venv
```Shell
python3 -m venv .venv
```

### Activate venv
```Shell
source .venv/bin/activate
```



##### Up Next: [[03-Typecasting]]
