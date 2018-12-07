import json
import pprint
from googleapiclient.discovery import build

class GoogleSearch:
    SEARCH_API_KEY = None
    SEARCH_ENGINE_ID = None
    def __init__(self):
        with open('config.json') as json_data_file:
            data = json.load(json_data_file)
        self.SEARCH_API_KEY = data["GOOGLE"]["CUSTOM_SEARCH_API_KEY"]
        self.SEARCH_ENGINE_ID = data["GOOGLE"]["CUSTOM_SEARCH_ENGINE_ID"]

    def getResult(self,question,options):
        results = []
        for option in options:
            if (option.startswith('"')):
                query = question + " " + option
            else:
                query = question + ' "' + option + '"'
            results.append(self.search(query))
        return results
    
    def search(self,query):
        service = build("customsearch", "v1", developerKey=self.SEARCH_API_KEY)
        res = service.cse().list(
            q=query,
            cx=self.SEARCH_ENGINE_ID,
        ).execute()
        return res['searchInformation']['totalResults']
