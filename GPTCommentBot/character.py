import random
import time
from functools import cached_property

import vk

import config
import constants
import messages
from proxy import GPTProxy
import pymorphy2


class Character:
    def __init__(
            self,
            phrase: str,
            access_token: str,
            group_id: int,
            gpt_query: str = messages.GPT_QUERY,
            frequency: float = 0.2,
            min_delay: int = 60,
            max_delay: int = 300,
    ):
        self.phrase = phrase
        self.api = vk.API(access_token=access_token, v=constants.VK_VERSION)
        self.proxy = GPTProxy()
        self.group_id = group_id
        self.frequency = frequency
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.gpt_query = gpt_query
        print(f"Create Character {phrase}")

    @cached_property
    def gent_phrase(self) -> str:
        morph = pymorphy2.MorphAnalyzer()
        res: str = ""
        for word in self.phrase.split():
            if morph.parse(word)[0].inflect({'gent'}):
                res += f"{morph.parse(word)[0].inflect({'gent'}).word} "
            else:
                res += f"{word} "
        return res

    def create_comment(self, owner_id: int, post_id: int, post_text: str) -> int:
        """Creates a comment in specified wall and post, returns its id"""
        print(f"Character {self.phrase} is creating a comment to post {post_id}...")

        post_summary: str = self.proxy.ask(message=messages.FIRST_PHRASE.format(post=post_text))
        comment: str = self.proxy.ask(message=self.gpt_query.format(phrase=self.gent_phrase, post=post_summary))

        res: dict = self.api.wall.createComment(owner_id=owner_id, post_id=post_id, message=comment)
        if "comment_id" in res.keys():
            print(f"Comment {res.get('comment_id')} has been posted.")
        return res.get("comment_id")

    def process_post(self, post_id: int, text: str):
        print(f"Character {self.phrase} is processing post {post_id}...")

        if random.random() > self.frequency:
            print(f"Character {self.phrase} choose not to comment.")
            return

        delay = random.randint(self.min_delay, self.max_delay)
        print(f"Character {self.phrase} is sleeping for {delay} seconds.")
        time.sleep(delay)

        self.create_comment(-self.group_id, post_id, text)
