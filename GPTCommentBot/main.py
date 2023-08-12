import vk
import config
import constants


def create_comment(api: vk.API, owner_id: int, post_id: int, message: str) -> int:
    """Creates a comment in specified wall and post, returns its id"""
    res: dict = api.wall.createComment(owner_id=owner_id, post_id=post_id, message=message)
    return res.get("comment_id")


if __name__ == "__main__":
    api = vk.API(access_token=config.ACCESS_TOKEN, v=constants.VK_VERSION)
    # print(create_comment(api, -205429509, 12, "Бывают же люди в наше время"))
    # print(api.groups.setLongPollSettings(group_id=205429509, enabled=1, wall_post_new=1))
    # print(api.groups.getLongPollServer(group_id=205429509))
    # {'key': 'eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJxdWV1ZV9pZCI6IjIwNTQyOTUwOSIsInVudGlsIjoxNjkxODc0OTE4NTIxMzQ1OTg5fQ.oeCEKW35nZOU365RR7Y7YWE2ctyM6HgEab1IFE4pRrkv6jba4RBOwuJEod6rC8rDX8P1IunKc7jfRTTiD9s9Cw',
    # 'server': 'https://lp.vk.com/whp/205429509', 'ts': '0'}
