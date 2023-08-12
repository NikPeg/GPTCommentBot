import vk
import config
import constants


api = vk.API(access_token=config.ACCESS_TOKEN, v=constants.VK_VERSION)
print(api.wall.post(message="Жаль, что не все поймут) Не многие вспомнят))"))
