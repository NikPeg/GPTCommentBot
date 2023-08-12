# GPTCommentBot
Бот для управления фейковыми аккаунтами, которые будут оставлять сгенерированные chatGPT комментарии под нужными постами.

# Настройка окружения
Установите python версии 3.10. Например, с помощью pyenv: https://github.com/pyenv/pyenv

Создайте виртуальное окружение: https://docs.python.org/3/library/venv.html
source venv/bin/activate
Перед каждой строкой командной строки должно появиться (venv)

Установите необходимые для работы бота пакеты:
pip install -r requirements.txt

Создайте файл config.py в основной папке проекта, рядом с main.py
Добавьте в этот файл access_token ВКонтакте в формате:
ACCESS_TOKEN = "ваш токен"

Про получение токена подробно рассказано в этом видео: https://www.youtube.com/watch?v=f8D6RYNEtlk
Повторю основные пункты из него.

Зайдите в раздел "Мои приложения" вконтакте: https://vk.com/apps?act=manage
И создайте новое приложение. Нажмите "редактировать" в списке приложений, выберете "настройки" в левом меню. Скопируйте ID приложения, например, 51727701.

В пункте "Состояние" выберете "Приложение включено и видно всем".
Создайте URL запроса токена, это описано в официальной документации: https://dev.vk.com/ru/api/access-token/implicit-flow-user
У меня получился такой запрос:
https://oauth.vk.com/authorize?client_id=51727701&state=123&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=offline,walls&response_type=token&v=5.21
В пункте scope должны быть перечислены нужные Вам доступы к аккаунту.

Отправьте запрос на получение токена (Enter) и авторизуйтесь через официальный интерфейс ВКонтакте. Скопируйте из адресной строки браузера всё, что идёт после "access_token=" до "&expires_in". Это и есть access_token.
