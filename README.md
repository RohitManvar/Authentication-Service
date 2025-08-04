# 🔐 FastAPI Authentication Service

A high-performance and secure authentication microservice using **FastAPI**, **MongoDB**, **Redis**, and **JWT**. This service handles user registration, login, protected routes, and token-based authentication, with optional session/token management via Redis.

---

## 🚀 Features

- 🧾 JWT-based token authentication (Access + Refresh tokens)
- 🗃️ MongoDB for user data storage (`motor` async driver)
- 🔄 Redis for refresh/session token storage or blacklisting
- 🔑 Secure password hashing with Bcrypt
- ✅ Input validation with Pydantic
- 🌐 minimal frontend for login/register testing

---

## 🛠️ Tech Stack

- **FastAPI** – Modern Python web framework
- **MongoDB** – NoSQL database for storing users
- **Redis** – Session/token storage & blacklisting
- **Pydantic** – Data validation
- **bcrypt** – Password hashing
- **python-jose** – JWT handling


---
### Login
<img width="833" height="857" alt="image" src="https://github.com/user-attachments/assets/9f74c875-5dbd-49d0-bbd7-e21cec584126" />
### Register
<img width="888" height="901" alt="image" src="https://github.com/user-attachments/assets/b922042f-3098-437e-bb12-0fa2eca41921" />
### Authetication Successful 
<img width="917" height="847" alt="image" src="https://github.com/user-attachments/assets/beed0cc3-aeb1-47a4-b814-477f90019ddc" />


