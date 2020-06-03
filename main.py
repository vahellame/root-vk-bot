# -*- coding: utf-8 -*-

import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

VK_TOKEN = "YOUR_VK_TOKEN"
vk = vk_api.VkApi(token=VK_TOKEN)
longpoll = VkLongPoll(vk)
VK_ID_ROOT = 576604927


def send_message(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": get_random_id()})


print("let it burn")
while True:
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    if event.user_id == VK_ID_ROOT:
                        if event.text == "out":
                            with open("out.txt", "r") as file:
                                logs = file.read()
                                if not logs:
                                    send_message(VK_ID_ROOT, "<empty>")
                                else:
                                    send_message(VK_ID_ROOT, logs)
                        elif event.text == "errors":
                            with open("errors.txt", "r") as file:
                                logs = file.read()
                                if not logs:
                                    send_message(VK_ID_ROOT, "<empty>")
                                else:
                                    send_message(VK_ID_ROOT, logs)
                        else:
                            os.system("{} > out.txt 2> errors.txt &".format(event.text))
    except:
        pass
