# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2022 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.

from os import environ

import heroku3

from userge import logging
from .sys_tools import secured_env, secured_str

_LOG = logging.getLogger(__name__)

# try to get this value using eval :)
TEST = secured_str("nice! report @UsergeSpam")

API_ID = environ.get("221017")
API_HASH = secured_env("3f0b55d67e0357d426afc5dc3c27145c")
BOT_TOKEN = secured_env("5654579119:AAGWmrRzecfC6KiYhAcaDU0DcwVAJN8OBms")
SESSION_STRING = secured_env("AgFbEf8AfSaKM6zJBtNNawwsIFTzjdzOmgiLm2RNHePDX9FvfFjquMMf4xc_s-N0ylEptNpl-qWdc7A1Zviao9XemOJS4oFfzDokFraFKNDGimrS_S2b3fiarstYE3PBaNM7KflZSXxrYZ097EZioUtziCNgGqud11BULNEJNDyA1c8qHERYM8Y5Aum7iYBSRVERSztXPI58F-t2o1H54Tp9zblRPajsMF42teH7rRxEmBl5o3fjmqk51HstP9Hss_MVzVeLXg3xdoaT_OrjN-gxlBoigTkmNY3qlx9L_ZRkp8ZKGKoyjF6C_yPZvtt81soCSMCYB_tyUQeFd9zuDC8L2ZNIJgAAAAFEQ2ixAA")
DB_URI = secured_env("mongodb+srv://hmoelwaseaf:ghZvWN9xDWkbjizg@cluster0.gqmhx8j.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = tuple(filter(lambda x: x, map(int, environ.get("OWNER_ID", "5440235697").split())))
LOG_CHANNEL_ID = int(environ.get("-1001861252300"))
AUTH_CHATS = (OWNER_ID[5440235697], LOG_CHANNEL_ID) if OWNER_ID else (LOG_CHANNEL_ID,)

CMD_TRIGGER = environ.get("CMD_TRIGGER")
SUDO_TRIGGER = environ.get("SUDO_TRIGGER")
PUBLIC_TRIGGER = '/'

WORKERS = int(environ.get("WORKERS"))
MAX_MESSAGE_LENGTH = 4096

FINISHED_PROGRESS_STR = environ.get("FINISHED_PROGRESS_STR")
UNFINISHED_PROGRESS_STR = environ.get("UNFINISHED_PROGRESS_STR")

HEROKU_API_KEY = secured_env("HEROKU_API_KEY")
HEROKU_APP_NAME = environ.get("HEROKU_APP_NAME")
HEROKU_APP = heroku3.from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME] \
    if HEROKU_API_KEY and HEROKU_APP_NAME else None

ASSERT_SINGLE_INSTANCE = environ.get("ASSERT_SINGLE_INSTANCE", '').lower() == "true"
IGNORE_VERIFIED_CHATS = True


class Dynamic:
    DOWN_PATH = environ.get("DOWN_PATH")

    MSG_DELETE_TIMEOUT = 120
    EDIT_SLEEP_TIMEOUT = 10

    USER_IS_PREFERRED = False
