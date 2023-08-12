import vk
import config
import constants


def create_comment(api: vk.API, owner_id: int, post_id: int, message: str) -> int:
    """Creates a comment in specified wall and post, returns its id"""
    res: dict = api.wall.createComment(owner_id=owner_id, post_id=post_id, message=message)
    return res.get("comment_id")


if __name__ == "__main__":
    api = vk.API(access_token=config.ACCESS_TOKEN, v=constants.VK_VERSION)
    print(create_comment(api, -205429509, 12, "Бывают же люди в наше время"))
