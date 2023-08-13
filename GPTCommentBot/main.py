import time

import vk

import config
import constants
import messages
from character import Character
from proxy import GPTProxy
import threading

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


characters: list[Character] = []


def process_post(post_id: int, text: str):
    # time.sleep(60)
    global characters
    for character in characters:
        character.create_comment(-constants.GROUP_ID, post_id, text)


def listen_group(group_id: int, group_token: str, process_post: "(post_id: int, text: str) -> None"):
    print("Listening...")
    while True:
        api = vk_api.VkApi(token=group_token)
        long_poll = VkBotLongPoll(api, group_id)
        try:
            for event in long_poll.listen():
                if event.type == VkBotEventType.WALL_POST_NEW:
                    print("New post!")
                    threading.Thread(target=process_post, args=(event.obj.id, event.obj.text)).start()

        except Exception as e:
            print(e)


if __name__ == "__main__":
    api = vk.API(access_token=config.ACCESS_TOKEN, v=constants.VK_VERSION)
    proxy = GPTProxy()
    characters.append(Character("агрессивного школьника", api, proxy))
    characters.append(Character("инста-блогерши", api, proxy))
    characters.append(Character("матери-одиночки", api, proxy))
    characters.append(Character("бати с завода", api, proxy))
    characters.append(Character("ворчливого деда", api, proxy))
    listen_group(constants.GROUP_ID, config.GROUP_TOKEN, process_post)


    # create_comment(api, constants.GROUP_ID, 23, f"писсуары — это хорошая идея!")
    # print(create_comment(api, -205429509, 12, "Бывают же люди в наше время"))
    # print(api.groups.setLongPollSettings(group_id=205429509, enabled=1, wall_post_new=1))
    # print(api.groups.getLongPollServer(group_id=205429509))
    # {'key': 'eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJxdWV1ZV9pZCI6IjIwNTQyOTUwOSIsInVudGlsIjoxNjkxODc0OTE4NTIxMzQ1OTg5fQ.oeCEKW35nZOU365RR7Y7YWE2ctyM6HgEab1IFE4pRrkv6jba4RBOwuJEod6rC8rDX8P1IunKc7jfRTTiD9s9Cw',
    # 'server': 'https://lp.vk.com/whp/205429509', 'ts': '0'}
