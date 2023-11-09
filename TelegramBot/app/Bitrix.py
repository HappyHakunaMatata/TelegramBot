from bitrix24 import *
import logging

class Bitrix:
    def __init__(self, api):
        self.api = api
        self.bx24 =  Bitrix24(self.api)
    
    async def Bitrix(self, users):
        try:
            #members =  await GetAllMembers()
            #users = members["phones"]
            #if len(users) == 0:
            #    return
            id = self.bx24.callMethod('crm.duplicate.findbycomm', entity_type="CONTACT", values=users, type = "PHONE") #Получить id пользователей по номерам из тг
            if (len(id)== 0):
                return
            deal_list = self.bx24.callMethod('crm.deal.list', filter={'STAGE_ID':'C8:NEW'}, select = ['CONTACT_ID']) #Получить id проживающих
            deals = set(map(lambda x: int(x["CONTACT_ID"]), deal_list)) #Множество id проживающих
            contact_id = set(map(lambda x: x, id['CONTACT'])) #Множество id пользователей тг
            expired = list(contact_id - deals) #Список тех кто уже не проживает
            clients = self.bx24.callMethod('crm.contact.list', filter={'ID':expired}, select = ['ID', 'PHONE']) #Получить список выехавших
            clients_phones = list(map(lambda x: int(x["PHONE"][0]["VALUE"]), clients)) #Получить список номеров выехавших
            #for i in members["users"]: #Кикаем
            #    if (i.phone in clients_phones):
            #        await bot.kick_chat_member(public_chat_id, i.id) #Кик по id
            #await DeleteRemovedUsers() #Отчищаем список удаленных
        except BitrixError as e:
            logging.error(f"Произошла ошибка: {e}")
        except Exception as e:
            logging.error(f"Произошла ошибка: {e}")
