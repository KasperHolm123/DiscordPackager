import requests, json, os, itertools


class packager:

    def __init__(self, data) -> None:
        self.auth = data['Authorization']
        self.channels = data['Channels'].items()
        self.modes = itertools.chain('w', itertools.cycle('a'))

        self.HEADERS = {
            'authorization': self.auth
        }

    @property
    def mode(self):
        return next(self.modes)
    
    def fetch_content(self, amount):
        # if message is text then get_texts() else get_images
        # save them in a folder named after parent channel
        for channel in self.channels:
            r = requests.get(f'https://discord.com/api/v8/channels/{channel[1]}/messages?limit={amount}', headers=self.HEADERS)
            json_object = json.loads(r.text)
            for message in json_object:
                # message with picture/attachment
                if message['attachments']:
                    self.get_images(message, channel[0])
                # message with only text, also includes discord text blocks
                if message['content'] and not message['attachments']:
                    self.get_texts(message, channel[0])

    def get_texts(self, message, channel_name):
        # create dir if it doesn't already exist
        if not os.path.exists(f'files/{channel_name}'):
            os.makedirs(f'files/{channel_name}')

        with open(f'files/{channel_name}/messages.txt', self.mode) as f:
            f.write(f'{message["author"]["username"]}\n{message["content"]}\n')

    def get_images(self, message, channel_name):
        # create dir if it doesn't already exist
        if not os.path.exists(f'files/{channel_name}'):
            os.makedirs(f'files/{chanel_name}')
        #with open(f'', 'w') as f:
            # download pictures and store in separate dir
        #    pass
        if message['content']:
            with open(f'files/{channel_name}/messages.txt', self.mode) as f:
                f.write(f'{message["author"]["username"]}\n{message["content"]}\n')
        #print('channel: ', channel_name)
        #print(message['author']['username'])
        #print('attachment:', message['attachments'][0]['url'], '\n')
