import requests, json

class packager:

    def __init__(self, data) -> None:
        self.auth = data['Authorization']
        self.channels = data['Channels']

        self.HEADERS = {
            'authorization': self.auth
        }
    
    def fetch_content(self):
        # if message is text then get_texts() else get_images
        # save them in a folder named after parent channel
        pass

    def get_texts(self):
        for channel in self.channels:
            r = requests.get(f'https://discord.com/api/v8/channels/{channel}/messages', headers=self.HEADERS)
            json_object = json.loads(r.text)
            for value in json_object:
                if value['content'] != '':
                    print(f'{value["author"]["username"]}: \n[{value["content"]}]\n')

    def get_images(self):
        pass
