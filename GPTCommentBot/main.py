import threading

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import config
from character import Character


class GPTCommentBot:
    def __init__(self, group_id: int, group_token: str, characters: list[Character] = None):
        self.group_id: int = group_id
        self.group_token: str = group_token
        self.characters = characters or []

    def listen_group(self):
        print(f"Listening group {self.group_id}...")
        while True:
            api = vk_api.VkApi(token=self.group_token)
            long_poll = VkBotLongPoll(api, self.group_id)
            try:
                for event in long_poll.listen():
                    if event.type == VkBotEventType.WALL_POST_NEW:
                        print("New post!")
                        for character in self.characters:
                            threading.Thread(target=character.process_post, args=(event.obj.id, event.obj.text)).start()

            except Exception as e:
                print(e)

    def add_character(self, phrase: str, token: str):
        self.characters.append(Character(phrase, token, self.group_id))


if __name__ == "__main__":
    bot = GPTCommentBot(config.GROUP_ID, config.GROUP_TOKEN)
    bot.add_character("агрессивный школьник", config.ACCESS_TOKEN)
    bot.add_character("инста-блогерша", config.ACCESS_TOKEN)
    bot.add_character("мать-одиночка", config.ACCESS_TOKEN)
    bot.add_character("батя с завода", config.ACCESS_TOKEN)
    bot.add_character("ворчливый дед", config.ACCESS_TOKEN)
    bot.listen_group()

    # create_comment(api, constants.GROUP_ID, 23, f"писсуары — это хорошая идея!")
    # print(create_comment(api, -205429509, 12, "Бывают же люди в наше время"))
    # print(api.groups.setLongPollSettings(group_id=205429509, enabled=1, wall_post_new=1))
    # print(api.groups.getLongPollServer(group_id=205429509))
    # {'key': 'eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJxdWV1ZV9pZCI6IjIwNTQyOTUwOSIsInVudGlsIjoxNjkxODc0OTE4NTIxMzQ1OTg5fQ.oeCEKW35nZOU365RR7Y7YWE2ctyM6HgEab1IFE4pRrkv6jba4RBOwuJEod6rC8rDX8P1IunKc7jfRTTiD9s9Cw',
    # 'server': 'https://lp.vk.com/whp/205429509', 'ts': '0'}
