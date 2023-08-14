from functools import cached_property

import vk

import config
import constants
import messages
from proxy import GPTProxy
import pymorphy2


class Character:
    def __init__(self, phrase: str, access_token: str, group_id: int):
        self.phrase = phrase
        self.api = vk.API(access_token=access_token, v=constants.VK_VERSION)
        self.proxy = GPTProxy()
        self.group_id = group_id
        print(f"Create Character {phrase}")

    @cached_property
    def gent_phrase(self) -> str:
        morph = pymorphy2.MorphAnalyzer()
        parsed_phrase = morph.parse(self.phrase)[0]
        return parsed_phrase.inflect({'gent'}).word

    def create_comment(self, owner_id: int, post_id: int, post_text: str) -> int:
        """Creates a comment in specified wall and post, returns its id"""

        print(f"Character {self.phrase} is creating a comment to post {post_id}...")
        comment: str = self.proxy.ask(message=messages.GPT_QUERY.format(phrase=self.phrase, post=post_text))
        res: dict = self.api.wall.createComment(owner_id=owner_id, post_id=post_id, message=comment)
        return res.get("comment_id")

    def process_post(self, post_id: int, text: str):
        # time.sleep(60)
        print(f"Character {self.phrase} is processing post {post_id}...")
        self.create_comment(-self.group_id, post_id, text)
