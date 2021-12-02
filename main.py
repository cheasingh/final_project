from os import environ
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

password = environ.get("PASSWORD")
print(password)

print("hello world!")
