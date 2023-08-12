import vk
import config
import constants


api = vk.API(access_token=config.ACCESS_TOKEN, v=constants.VK_VERSION)
# print(api.wall.post(message="Жаль, что не все поймут) Не многие вспомнят))"))
post_id = 21
user_id = 521780797
print(api.wall.createComment(owner_id=user_id, post_id=post_id, message="Да уж, не так уж много олдов в наше время)"))
