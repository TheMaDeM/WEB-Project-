from random import randint

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

TOKEN = 'vk1.a.DupwHvzUuC1YTKm4PX8CdugIs0kMisyd1Gxp85lcH3fWsZuMyDlrcMxYwjFUR7ph' \
        'BulzRwba9FX_BqGPQ14a6bd64NJkeolCIdmHMgnHijHiE5OHDVZ_qiEmClxTyf_CxADW70' \
        '_sPHeOruVkF0IfZWTRhGBvui7Ohfv-x9WK86NwffIfYlFx_1tjVOxtp268ECMFdrW2NkOKrlwe_FQPMA'

ID = '220203199'


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, '220203199')

    replies = []

    for event in longpoll.listen():
        print(event.type)

        if event.type == VkBotEventType.MESSAGE_NEW:
            vk = vk_session.get_api()
            if event.object.message['text'] != '':
                replies.append(event.object.message['text'])
            print(event.object.message)
            if event.object.message['peer_id'] == event.object.message['from_id']:
                peer_id = event.object.message['from_id']
            else:
                peer_id = 2000000000 + event.chat_id
            chance = randint(0, 1)
            print(peer_id)
            if chance == 1 and len(replies) > 0:
                reply_id = randint(0, len(replies) - 1)
                vk.messages.send(peer_id=peer_id,
                                 message=replies[reply_id],
                                 random_id=randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_EDIT:
            vk = vk_session.get_api()
            chance = randint(0, 4)
            if chance == 1:
                vk.messages.send(peer_id=event.obj.from_id,
                                 message='Опа, а че мы там меняем?',
                                 random_id=randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_TYPING_STATE:
            vk = vk_session.get_api()
            print(event.object.message)
            chance = randint(0, 4)
            if chance == 1:
                vk.messages.send(peer_id=event.obj.from_id,
                                 message='Опа, а че мы там пишем?',
                                 random_id=randint(0, 2 ** 64))

        if event.type == VkBotEventType.GROUP_JOIN:
            vk = vk_session.get_api()
            vk.messages.send(peer_id=event.obj.user_id,
                             message='Добро пожаловать в сообщество!',
                             random_id=randint(0, 2 ** 64))

        if event.type == VkBotEventType.GROUP_LEAVE:
            vk = vk_session.get_api()
            vk.messages.send(peer_id=event.obj.user_id,
                             message='До свидания',
                             random_id=randint(0, 2 ** 64))

        if event.type == VkBotEventType.MESSAGE_ALLOW:
            vk = vk_session.get_api()
            vk.messages.send(peer_id=event.obj.user_id,
                             message='Ну го поболтаем че',
                             random_id=randint(0, 2 ** 64))


if __name__ == '__main__':
    main()