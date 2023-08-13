import vk

import config
import constants
import messages
from proxy import GPTProxy


class Character:
    def __init__(self, phrase: str, access_token: str):
        self.phrase = phrase
        self.api = vk.API(access_token=access_token, v=constants.VK_VERSION)
        self.proxy = GPTProxy()

    def create_comment(self, owner_id: int, post_id: int, post_text: str) -> int:
        """Creates a comment in specified wall and post, returns its id"""
        comment: str = self.proxy.ask(message=messages.GPT_QUERY.format(phrase=self.phrase, post=post_text))
        res: dict = self.api.wall.createComment(owner_id=owner_id, post_id=post_id, message=comment)
        return res.get("comment_id")

    def process_post(self, post_id: int, text: str):
        # time.sleep(60)
        self.create_comment(-constants.GROUP_ID, post_id, text)
