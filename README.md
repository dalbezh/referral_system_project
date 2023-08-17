# <p align="center">REFERRAL SYSTEM</p>
### <p align="center">Приложение реализующие пользовательскую реферальную систему.</p>
___
[![Python](https://img.shields.io/badge/python-v3.9-orange)](https://www.python.org/downloads/release/python-394/)
[![Django](https://img.shields.io/badge/django-v4.2.4-green)](https://docs.djangoproject.com/en/4.2/releases/4.2.4/)
[![Postgres](https://img.shields.io/badge/postgres-v14.6-blue)](https://www.postgresql.org/docs/14/release-14-6.html)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
___
* Настроена OTP авторизация.\
По сути представление VerifyOTPView меняет поле is_active на True и логинит пользователя.
Делается через метод PATCH


- [x] Для LoginView в response вытаскивать `<pk>` для urls. 
___
#### TODO 