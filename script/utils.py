from script.metadata import HEADER, WORKSHOP_URL

from bs4 import BeautifulSoup
from urllib import request
import time
import random
import os

# url에서 id 추출
def ext_id(workshop_url):
    for _ in reversed(workshop_url.split('/')):
        if 'id' in _:
            return _[4:]

# url을 통해서 html 읽어오기
def call_html(id):
    with request.urlopen(request.Request(url=WORKSHOP_URL+id, headers=HEADER)) as response:
        return BeautifulSoup(response.read(), 'lxml')

# 모음집 id를 사용하여 모음집에 있는 워크숍 id 불러오기
def collect_mod_id(collection_id):
    id_list = []

    # 모음집의 구독 목록 부분 불러오기
    for _ in call_html(collection_id).find_all('div', class_='workshopItem'):
        id_list.append(ext_id(_.find('a')['href']))

    return id_list

# 가져온 ID를 사용해서 정보 긁어오기
def collect_mod_contents(id_list, set_sleep=False):
    mod_dict = {'id':id_list, 'mod':[], 'map':[]}
    
    for id_num in mod_dict['id']:
        # URL을 통해서 html 읽어오기
        workshop_contents = call_html(id_num).find('div', class_='workshopItemDescription')
        
        for _ in workshop_contents.prettify().split('\n'):
            # MOD NAME
            if 'Workshop ID: ' in _:
                print('Workshop ID: {}'.format(_.split(': ')[1]))
            # MOD ID
            elif 'Mod ID: ' in _:
                print('Mod ID: {}'.format(_.split(': ')[1]))
                mod_dict['mod'].append(_.split(': ')[1])
            # MAP FOLDER
            elif 'Map Folder: ' in _:
                print('Map Folder: {}'.format(_.split(': ')[1]))
                mod_dict['map'].append(_.split(': ')[1])

        if set_sleep:
            time.sleep(random.uniform(1, 3))

        print('-' * 20)

    return mod_dict

def save_env(mod_dict, env_path='./'):
    if os.path.isfile(env_path+'.env'):
        print('.env 파일이 존재하여 삭제 후 재생성합니다.')
        os.remove(env_path+'.env')
    env_file = open(env_path+'.env', 'w')
    env_file.write('MOD_WORKSHOP_IDS=' + ';'.join(mod_dict['id']) + '\n')
    env_file.write('# 마지막에 Muldraugh, KY는 꼭 있어야합니다.\n')
    env_file.write('MOD_NAMES='+ ';'.join(mod_dict['mod']) + '\n')
    env_file.write('MAP_NAMES='+ ';'.join(mod_dict['map']) + ';Muldraugh, KY' + '\n')
    env_file.close()