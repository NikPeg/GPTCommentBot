import vk
import config
import constants


api = vk.API(access_token=config.ACCESS_TOKEN)
print(api.users.get(user_ids=1, v=constants.VK_VERSION))
