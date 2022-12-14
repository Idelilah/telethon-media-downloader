import os
import asyncio
import logging

from telethon import TelegramClient
from telethon import functions, types

from dotenv import load_dotenv

load_dotenv()


"""Logger"""
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)


"""API ID and hash from my.telegram.org to create a telegram client"""

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')




class Bot(TelegramClient):
    def __init__(self, limit=10, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.limit = limit
        print("Bot created")


    """
    Get media essages from a channel
    @param channel: channel username
    @return: list of media messages
    """

    async def get_media(self, channel):
        messages = await self.get_messages(channel, limit=self.limit)
        media = []
        for message in messages:
            if message.media:
                media.append(message.media)
        logger.info("Found {} files".format(len(media)))
        print(messages)
        return media

    """
    Create a file path for a media message
    @param channel: channel username
    @param message: media message
    @return: file path
    """
    def create_path(self, channel, message):
        file_name = message.file.name
        file_path = os.path.join(channel, file_name)
        return file_path

    """
    Get and download media messages from a channel
    @param channel: channel username
    @return: list of downloaded media messages
    """
    async def download_files(self, channel):
        await self.connect()
        media = await self.get_media(channel)
        file_paths = []
        for m in media:
            file_path = self.create_path(channel, m)
            await m.download_media(m)
            file_paths.append(file_path)
        logger.info("Downloaded {} files".format(len(media)))
        return media


async def main(
    limit,
    session_name,
    api_id,
    api_hash,
):

    bot = Bot(
        limit, session_name, api_id, api_hash
    )
    await bot.start()
    await bot.download_files(channel_name)


if __name__ == "__main__":

    try:
        asyncio.run(
            main(
                limit=10,
                session_name="session_name",
                api_id=api_id,
                api_hash=api_hash,
            )
        )
    except KeyboardInterrupt:
        print("\n STOP EXPORTING")


