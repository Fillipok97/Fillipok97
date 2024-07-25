from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    '''Проверяем, что запрос возвращает статус-код 200 и в содержимом ответа присутсвует уникальный идентификационный ключ'''

    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_list_of_pets_with_valid_key(filter=''):
    '''Проверяем, что запрос возвращает статус-код 200 и в содержимом ответа находится список животных по указанному фильтру'''

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер', age='4', pet_photo='images/cat1.jpg'):
    '''Проверяем что можно добавить питомца с корректными данными'''

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    '''Проверяем возможность удаления питомца'''

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    '''Проверяем возможность обновления информации о питомце'''

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")


#Ниже находятся тест-кейсы реализованные в соответствии с заданием 24.7.2


def test_add_new_pet_without_photo_and_with_valid_data(name='Матильда', animal_type='Собака', age='3'):
    '''Проверяем что можно добавить питомца без фото и с корректными данными'''

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_without_photo_and_with_invalid_data(name='', animal_type='', age=''):
    '''Проверяем что можно добавить питомца без фото с некорректными данными'''

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 400
    assert result['name'] != name
#Баг! Запрос с пустыми данными проходить не должен.

def test_add_photo_to_created_pet_with_valid_format(pet_photo='images/P1040103.jpg'):
    '''Проверяем возможность добавления фото питомца'''

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    pet_id = my_pets['pets'][0]['id']

    # Проверяем, есть ли уже фотография у питомца
    if my_pets['pets'][0]['pet_photo'] == "":
        status, result = pf.add_photo_to_created_pet(auth_key, pet_id, pet_photo)
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
        assert status == 200
        assert result['pet_photo'] == my_pets['pets'][0]['pet_photo']
    else:
        print("У питомца уже есть фото")


def test_add_photo_to_created_pet_with_invalid_format(pet_photo='images/IMG_5126.HEIC'):
    '''Проверяем возможность добавления фото питомца'''

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    pet_id = my_pets['pets'][0]['id']

    # Проверяем, есть ли уже фотография у питомца
    if my_pets['pets'][0]['pet_photo'] == "":
        status, result = pf.add_photo_to_created_pet(auth_key, pet_id, pet_photo)
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
        assert status == 415
        assert result['pet_photo'] != my_pets['pets'][0]['pet_photo']
    else:
        print("У питомца уже есть фото")

#Баг! В ответ на запрос приходит ошибка с кодом 500


def test_get_api_key_for_invalid_email_and_password(email='invalid_email', password='invalid_password'):
    '''Проверяем, что нельзя получить идентификационный ключ, введя неверные данные авторизации.'''

    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


def test_get_api_key_for_invalid_email(email='invalid_email', password=valid_password):
    '''Проверяем, что нельзя получить идентификационный ключ, введя неверный email, но верный пароль.'''

    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


def test_get_api_key_for_invalid_password(email=valid_email, password='invalid_password'):
    '''Проверяем, что нельзя получить идентификационный ключ, введя неверный пароль, но верный email.'''

    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


def test_get_list_of_pets_with_valid_key_without_filter():
    '''Проверяем, что запрос возвращает статус-код 200 и в содержимом ответа находится список животных'''

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key)
    assert status == 200
    assert len(result['pets']) > 0


def test_successful_delete_any_pet():
    '''Проверяем возможность удаления любого питомца'''

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, all_pets = pf.get_list_of_pets(auth_key)

    pet_id = all_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, all_pets = pf.get_list_of_pets(auth_key)
    assert status == 400
    assert pet_id in all_pets.values()

#Баг! Пользователь не должен иметь возможность удаления питомца из списка всех питомцев, но удаление проходит.


def test_successful_update_any_pet_info(name='Kal-el', animal_type='Koroed', age=15):
    '''Проверяем возможность обновления информации о питомце'''

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, all_pets = pf.get_list_of_pets(auth_key)

    if len(all_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, all_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 400
        assert result['name'] != name

#Баг! Пользователь не должен иметь возможность изменения питомца из списка всех питомцев, но изменение проходит.