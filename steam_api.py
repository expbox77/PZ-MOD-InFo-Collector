import requests
import json
from script.utils import ext_id
from script.db import *

def collect_workshop_id(collection_id):
    COLLECTION_API_HOST = 'https://api.steampowered.com/ISteamRemoteStorage/GetCollectionDetails/v1/'
    # url = API_HOST + path
    # headers = {'Content-Type': 'application/x-www-form-urlencoded', 'charset': 'UTF-8', 'Accept': '*/*'}
    body = {
        "collectioncount":"1",
        "publishedfileids[0]":collection_id
    }
    try:
        response = requests.post(COLLECTION_API_HOST, data=body)
        jsonObject = json.loads(response.text)
        jsonArray = jsonObject.get('response').get('collectiondetails')[0].get('children')
    except Exception as ex:
        print(ex)
    
    workshop_ids = []
    for _ in jsonArray:
        workshop_ids.append(_.get('publishedfileid'))

    return workshop_ids
  
def collect_workshop_contents(workshop_ids, db_name):
    WORKSHOP_API_HOST = 'https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/'

    for _ in workshop_ids:
        body = {
            "itemcount":"1",
            "publishedfileids[0]":_
        }
        try:
            response = requests.post(WORKSHOP_API_HOST, data=body)
            jsonObject = json.loads(response.text.replace('\'', '\'\''))
            json_title = jsonObject.get('response').get('publishedfiledetails')[0].get('title')
            json_description = jsonObject.get('response').get('publishedfiledetails')[0].get('description')
            json_time_updated = jsonObject.get('response').get('publishedfiledetails')[0].get('time_updated')
            print(_)
            insert_db(db_name, _, json_title, json_description, json_time_updated)
        except Exception as ex:
            print(ex)
            break

if __name__ == "__main__":
    # 호출 예시
    url = 'https://steamcommunity.com/sharedfiles/filedetails/?id=2854214800'
    db_name = 'zb'
    connect_db(db_name)
    make_db(db_name)
    collect_workshop_contents(collect_workshop_id(ext_id(url)), db_name)
    # print(description_list)
    # print(uptime_list)
