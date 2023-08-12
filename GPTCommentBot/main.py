import vk
import config

vk_api = vk.session.API(access_token=config.ACCESS_TOKEN)

# vk_api = vk_session.api()

print(vk_api.session.wall.post(message='Hello world!', version=5.21))
