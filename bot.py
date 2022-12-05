from telethon import TelegramClient
from telethon import functions, types
import os
import logging

"""Logger"""
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


"""API ID and hash from my.telegram.org to create a telegram client"""

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')


# client =  TelegramClient('client', api_id, api_hash)

class Bot:
    def __init__(self, api_id, api_hash):
        self.api_id = api_id
        self.api_hash = api_hash
        self.client = TelegramClient('session_name', self.api_id, self.api_hash)
        self.client.start()
        self.client.run_until_disconnected()  
        print('Bot is running') 

    """Check and return the channel information"""
    def get_channel_info(self, username):
        channel = self.client.get_entity(username)
        print(channel.stringify())
        return channel
    """get media files from a channel"""

    def get_media(self, username, limit=10):
        media = self.client.GetFullChannelRequest(
        channel=username
    )
        print('The channel has:', media.message)
        print(media.stringify())
        return media
    """download media files from a channel"""

    def download_media(self, username, limit=10):
        media = self._get_media(username, limit)
        for i in media:
            self.client.download_media(i, file=media)
            print('Downloaded:', media.message)
        

def main():
    bot = Bot(api_id, api_hash)
    bot._get_media('th_read')
    bot._download_media('th_read')
    

if __name__ == '__main__':
    main()


