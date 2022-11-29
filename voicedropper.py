from telethon import TelegramClient, events
from telethon.types import DocumentAttributeAudio, DocumentAttributeVideo


async def check_message(event):
    if event.message.document is None:
        return False   
    for attr in event.message.document.attributes:
        if isinstance(attr, DocumentAttributeAudio) and attr.voice:
            try:                
                await event.reply('**Отправка голосовых сообщений запрещена.**')
                await event.message.delete()
                return True
            except:
                pass
        elif  isinstance(attr, DocumentAttributeVideo) and attr.round_message:
            try:
                await event.message.delete()
                return True
            except Exception as e:
                pass

api_id = 1202506
api_hash = 'e2b15874f045df5fa64e6b5d0ef2c8c4'
with TelegramClient('session_test5', api_id, api_hash) as client:

    @client.on(events.NewMessage(pattern=''))
    async def handler(event):
        await check_message(event)

    client.run_until_disconnected()