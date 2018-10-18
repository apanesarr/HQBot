import wikipedia
from fuzzywuzzy import fuzz

class Wiki:
    def __init__(self,question,options):
        self.question = question
        self.options = options
        self.result = [0,0,0]
        self.getContent(question)
    
    def getContent(self,question):
        search = wikipedia.search(question)
        if len(search) > 1:
            page = wikipedia.page(search[0])
            self.content = page.content
            self.contentArray = self.content.split(" ")
        else:
            print("No Results")

    def searchContent(self,content,search):
        i = 0
        for word in content:
            result = fuzz.token_set_ratio(search,word)
            if result > 99:
                i+=1
        return i

    def getResults(self):
        for i in range(len(self.options)):
            self.result[i] = self.searchContent(self.contentArray,self.options[i])
        return self.result