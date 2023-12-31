import threading

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk
import config
import constants
import messages
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
                            try:
                                threading.Thread(
                                    target=character.process_post,
                                    args=(event.obj.id, event.obj.text),
                                ).start()
                            except Exception as e:
                                print(e)
            except Exception as e:
                print(e)

    def start(self):
        threading.Thread(target=self.listen_group).start()

    def add_character(
            self,
            phrase: str,
            token: str,
            gpt_query: str = messages.GPT_QUERY,
            frequency: float = 0.2,
            min_delay: int = 60,
            max_delay: int = 300,
    ):
        self.characters.append(Character(phrase, token, self.group_id, gpt_query, frequency, min_delay, max_delay))


if __name__ == "__main__":
    bot = GPTCommentBot(config.US_ID, config.US_TOKEN)
    bot.add_character("зрелая кассирша", config.SVETA_TOKEN, messages.GPT_GIF_QUERY, 0.05)
    bot.add_character("геймер задрот", config.ARTEM_TOKEN, messages.GPT_GIF_QUERY, 0.08)
    bot.add_character("шутница", config.VIKA_TOKEN, messages.JOKE_QUERY, 0.1)
    bot.add_character("мужик с завода", config.SERGEY_TOKEN, messages.GPT_GIF_QUERY, 0.08)
    bot.add_character("агрессивный школьник", config.LITTLE_VOVA_TOKEN, messages.GPT_GIF_QUERY, 0.1)
    bot.add_character("эстетичная девушка интеллектуалка", config.KATYA_TOKEN, messages.GPT_GIF_QUERY, 0.06)
    bot.add_character("инстаграм блогерши", config.DASHA_TOKEN, messages.GPT_GIF_QUERY, 0.07)
    bot.add_character("ворчливый дед", config.MAX_TOKEN, messages.GPT_GIF_QUERY, 0.05)
    bot.start()

    # second_bot = GPTCommentBot(config.SECOND_GROUP_ID, config.SECOND_GROUP_TOKEN)
    # second_bot.add_character("агрессивный школьник", config.ACCESS_TOKEN)
    # second_bot.add_character("инста-блогерша", config.ACCESS_TOKEN)
    # second_bot.add_character("мать-одиночка", config.ACCESS_TOKEN)
    # second_bot.add_character("батя с завода", config.ACCESS_TOKEN)
    # second_bot.add_character("ворчливый дед", config.ACCESS_TOKEN)
    # second_bot.start()
