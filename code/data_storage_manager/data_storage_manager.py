from asyncore import write
import json
import pickle
from typing import List

class DataStorage:
    def save(userDict):
        list1: list = DataStorage.load()
        list2 = list1.copy()
        for v in list2.copy():
            valJson = json.loads(v)
            if (valJson['chat_identifier'] == userDict['chat_identifier']):
                list2.remove(v)

        list2.append(json.dumps(userDict, ensure_ascii = False))

        if list1 != list2:
            pickle.dump(list2, open("save.p", "wb"))

    def load():
        try:
            return pickle.load(open("save.p", "rb"))
        except (OSError, IOError) as e:
         return []
