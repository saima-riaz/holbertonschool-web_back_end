# Personal_Data
![image](https://github.com/user-attachments/assets/6c5888fd-9c3c-4771-9638-784967b99ad8)

## Introduction
 This project is focused on protecting sensitive data, particularly Personally Identifiable Information (PII). It covers several key concepts like obfuscating sensitive information in logs, securely handling user passwords, and managing database authentication using environment variables.

 ---
 ## Resources


- **What Is PII, non-PII, and Personal Data?**
- **[Logging documentation](https://docs.python.org/3/library/logging.html)**
- **[bcrypt package](https://pypi.org/project/bcrypt/)**
- **Logging to Files, Setting Levels, and Formatting**

---
## Learning Objectives

1. Identify examples of Personally Identifiable Information (PII).
2. Implement a log filter to obfuscate PII fields.
3. Encrypt a password and verify the validity of an input password.
4. Authenticate to a database securely using environment variables.


## Requirements for Project

- All files are interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3.9**.
- Every file must end with a new line.
- The first line of all files must be exactly `#!/usr/bin/env python3`.
- A `README.md` file is mandatory in the root directory of the project.
- Your code must follow **pycodestyle** (version 2.5).
- All files must be executable.
- The length of the files will be tested using `wc`.
- All modules must have proper documentation.
- All classes and functions (inside and outside a class) must have docstrings explaining their purpose.
- All functions should have type annotations.



## Project Tasks

### 0. Regex-ing
A function `filter_datum` is implemented to obfuscate certain fields in a log message using regular expressions.

### 1. Log Formatter
The `RedactingFormatter` class is used to format log records while obfuscating sensitive information.

### 2. Create Logger
A `get_logger` function creates a logger with a `RedactingFormatter` that filters out PII fields.

### 3. Connect to Secure Database
The `get_db` function connects to a secure MySQL database using credentials stored as environment variables.

### 4. Read and Filter Data
The `main` function retrieves data from the `users` table and logs each record with sensitive fields obfuscated.

### 5. Encrypting Passwords
The `hash_password` function hashes a given password using the `bcrypt` package.

### 6. Check Valid Password
The `is_valid` function verifies if a password matches a hashed password using `bcrypt`.

## Author
- **Name:** Saima RIAZ
- **GitHub:** [saima_riaz](https://github.com/saima-riaz/holbertonschool-web_back_end/tree/main/personal_data)

