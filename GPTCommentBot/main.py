import time

import vk

import config
import constants
import messages
from character import Character
from listen_group import listen_group
from proxy import GPTProxy


characters: list[Character] = []


def process_post(post_id: int, text: str):
    # time.sleep(60)
    global characters
    for character in characters:
        character.create_comment(-constants.GROUP_ID, post_id, text)


if __name__ == "__main__":
    api = vk.API(access_token=config.ACCESS_TOKEN, v=constants.VK_VERSION)
    proxy = GPTProxy()
    characters.append(Character("агрессивного школьника", api, proxy))
    characters.append(Character("инста-блогерши", api, proxy))
    characters.append(Character("матери-одиночки", api, proxy))
    listen_group(constants.GROUP_ID, config.GROUP_TOKEN, process_post)


    # create_comment(api, constants.GROUP_ID, 23, f"писсуары — это хорошая идея!")
    # print(create_comment(api, -205429509, 12, "Бывают же люди в наше время"))
    # print(api.groups.setLongPollSettings(group_id=205429509, enabled=1, wall_post_new=1))
    # print(api.groups.getLongPollServer(group_id=205429509))
    # {'key': 'eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJxdWV1ZV9pZCI6IjIwNTQyOTUwOSIsInVudGlsIjoxNjkxODc0OTE4NTIxMzQ1OTg5fQ.oeCEKW35nZOU365RR7Y7YWE2ctyM6HgEab1IFE4pRrkv6jba4RBOwuJEod6rC8rDX8P1IunKc7jfRTTiD9s9Cw',
    # 'server': 'https://lp.vk.com/whp/205429509', 'ts': '0'}
