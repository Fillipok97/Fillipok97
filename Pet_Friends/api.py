import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru'

    def get_api_key(self, email: str, password: str) -> json :
        '''Метод делает запрос к API сервера и возвращает статус-код запроса и результат в формате JSON с уникальным ключем пользователя, найденного по указанным email и паролю'''

        headers = {
            'email': email,
            'password': password
        }

        res = requests.get(self.base_url + '/api/key', headers=headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def get_list_of_pets(self, auth_key: json, filter: str='') -> json:
        '''Метод, используя уникальный ключ, отправляет запрос на API сервера и вовращает статус-код ответа и список всех животных по указанному фильтру в формате JSON'''

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + '/api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text

        return status, result


    def add_new_pet(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo: str) -> json:
        '''Метод отправляет на сервер данные о добавляемом питомце и возвращает статус-код запроса и результат в формате JSON с данными добавленного питомца'''

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
        }

        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}
        res = requests.post(self.base_url + '/api/pets', headers=headers, data=data, files=file)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result


    def delete_pet(self, auth_key: json, pet_id: str) -> json:
        '''Метод отправляет на сервер запрос на удаление питомца по указанному ID и возвращает статус-код запроса и результат в формате JSON с текстом уведомления о успешном удалении.'''

        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + '/api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def update_pet_info(self, auth_key: json, pet_id: str, name: str, animal_type: str, age: int) -> json:
        '''Метод отправляет запрос на сервер о обновлении данных питомца по указанному ID и возвращает статус-код запроса и результат в формате JSON с обновлённыи данными питомца'''

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }

        res = requests.put(self.base_url + '/api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result



# Ниже добавлены два метода, реализованные в соответствии с заданием 24.7.2


    def add_new_pet_without_photo(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
        '''Метод отправляет на сервер данные о добавляемом питомце без добавления фото и возвращает статус-код запроса и результат в формате JSON с данными добавленного питомца'''

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }

        res = requests.post(self.base_url + '/api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


    def add_photo_to_created_pet(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
        '''Метод отправляет запрос на сервер о добавлении фото в данные питомца по указанному ID и возвращает статус-код запроса и результат в формате JSON с обновлённыи данными питомца'''

        data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + '/api/pets/set_photo/' + pet_id, data=data, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result