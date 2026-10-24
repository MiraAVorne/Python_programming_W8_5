########################################################
# Task A8_5
# Developer Sami Viljanen
# Date 2025-10-25
########################################################


import hashlib
import os

# Constants
CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"

def load_credentials() -> list[tuple[int, str, str]]:
    if not os.path.exists(CREDENTIALS_FILE):
        return []
    
    users = []

    with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            parts = line.split(";")
            if len(parts) == 3:
                user_id, username, password_hash = parts
                users.append((int(user_id), username, password_hash))
    return users

def save_credentials(credentials: list[tuple[int, str, str]]) -> None:
    with open(CREDENTIALS_FILE, "w", encoding="utf-8") as f:
        for user_id, username, password_hash in credentials:
            f.write(f"{user_id};{username};{password_hash}\n")


def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


def register(PUsername: str, PPassword: str) -> None:
    users = load_credentials()

    # Tarkistetaan, ettei käyttäjänimi ole jo käytössä tai tyhjä
    if not PUsername:
        print("Username cannot be empty.")
        return
    
    if any(user[1] == PUsername for user in users):
        print("Username already exists. Please choose a different username.")
        return
    
    # Luodaan uusi käyttäjä
    password_hash = hash_password(PPassword)
    user_id = max((user[0] for user in users), default=0) + 1
    users.append((user_id, PUsername, password_hash))
    save_credentials(users)
    print(f"User '{PUsername}' registered successfully!")

def login(PUsername: str, PPassword: str) -> bool:
    users = load_credentials()
    password_hash = hash_password(PPassword)

    for _, stored_username, stored_hash in users:
        if stored_username == PUsername and stored_hash == password_hash:
            return True
        
    return False

def viewProfile(PUsername: str) -> list[str]:
    users = load_credentials()
    
    for user_id, username, _ in users:
        if username == PUsername:
            return [str(user_id), username]
    
    return []

def change_password(PUsername: str, PNewPassword: str) -> bool:
    users = load_credentials()
    
    for i, (user_id, username, stored_hash) in enumerate(users):
        if username == PUsername:
            users[i] = (user_id, username, hash_password(PNewPassword))
            save_credentials(users)
            return True
    return False