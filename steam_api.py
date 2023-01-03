import requests
import json

# url에서 id 추출
def ext_id(workshop_url):
    for _ in reversed(workshop_url.split('/')):
        if 'id' in _:
            return _[4:]

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
  
def collect_workshop_contents(workshop_ids):
    WORKSHOP_API_HOST = 'https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/'
    description_list = []
    uptime_list = []

    for _ in workshop_ids:
        body = {
            "itemcount":"1",
            "publishedfileids[0]":_
        }
        try:
            response = requests.post(WORKSHOP_API_HOST, data=body)
            jsonObject = json.loads(response.text)
            description_list.append(jsonObject.get('response').get('publishedfiledetails')[0].get('description'))
            uptime_list.append(jsonObject.get('response').get('publishedfiledetails')[0].get('time_updated'))
        except Exception as ex:
            print(ex)
            break
    return description_list, uptime_list

if __name__ == "__main__":
    # 호출 예시
    url = 'https://steamcommunity.com/sharedfiles/filedetails/?id=2854214800'
    description_list, uptime_list = collect_workshop_contents(collect_workshop_id(ext_id(url)))
    print(description_list)
    print(uptime_list)
