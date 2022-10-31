from re import A
import requests, json

class packager:

    def __init__(self, data) -> None:
        self.auth = data["Authorization"]
        self.server = data["Server"]
        self.channels = data["Channels"]
    
    def fetch_content(self):
        # if message is text then get_texts() else get_images
        # save them in a folder named after parent channel
        pass

    def get_texts(self):
        pass

    def get_images(self):
        pass