import json
import os
#from all_media.links import INTENSO_STORAGE_CHAT_ID, all_media_dir

all_media_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'all_media')

def read_credentials(filename: str) -> dict:
    if os.path.getsize(os.path.join(all_media_dir, filename) == 0):
        print("was returned")
        return {}
    try:
        with open(file=os.path.join(all_media_dir, filename), mode="r") as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        return {}

# функция для передачи пары chat.username:chat.id в словарь для дальнейшей сериализаации в json
# необходима проверка что в json есть такой словарь, и если есть, что в нем уже имеется данная пара или нет
def add_credentials(current_dict, filename: str):
    library_dict = read_credentials(filename)
    print("get returned value")

    with open(file=os.path.join(all_media_dir, filename), mode="w") as f:
        if (len(library_dict) == 0):
            print("dict is empty")
            json.dump(current_dict, f)    
        else:
            print("dict does not empty")
            print(current_dict)
            print(library_dict)
            library_dict.update(current_dict)
            json.dump(library_dict, f)

#test_dict = {"robert0":"-1003215217346", "anastasiya":"12345"}
#add_credentials(test_dict, )
#print(read_credentials())
