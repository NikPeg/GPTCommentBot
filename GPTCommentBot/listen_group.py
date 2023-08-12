import vk_api
from vk_api import VkUpload
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import threading
import requests
import random

import config
import constants

if __name__ == '__main__':
    print("Listening...")
    while True:
        session = requests.Session()
        vk_session = vk_api.VkApi(token=config.GROUP_TOKEN)
        vk = vk_session.get_api()
        upload = VkUpload(vk_session)
        longpoll = VkBotLongPoll(vk_session, constants.GROUP_ID)
        try:
            for event in longpoll.listen():
                if event.type == VkBotEventType.WALL_POST_NEW:
                    # threading.Thread(target=processing_message, args=(event.obj.from_id, event.obj.text)).start()
                    print("New post!")
        except Exception:
            pass
