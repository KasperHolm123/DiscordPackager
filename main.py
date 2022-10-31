from struct import pack
from fetch import packager

# See README.md if you don't know how to get these data
credentials = {
    "Authorization": "YOUR AUTHROIZATION DATA",
    "Server" : "YOUR SERVER DATA",
    "Channels": {}
}

if __name__ == "__main__":
    client = packager(credentials)
    client.fetch_content()