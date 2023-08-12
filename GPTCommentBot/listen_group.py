import threading

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


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
