from struct import pack
from fetch import packager
import os
from dotenv import load_dotenv

# Load environmental variables
load_dotenv(dotenv_path=".env")

# Amount of messages to fetch
message_amount = 5

auth_details = os.getenv('AUTH')

# See README.md if you don't know how to get these data

# dotenv approach
credentials_dotenv = {
    "Authorization": f"{auth_details}",
    "Channels": {
        "yoinkies": "506870974315233285"
        } 
}

# dangerous approach
credentials = {
    "Authorization": "YOUR AUTHORIZATION DATA",
    "Server" : "YOUR SERVER DATA",
    "Channels": {}
}

if __name__ == "__main__":
    client = packager(credentials_dotenv)
    client.fetch_content(message_amount)
