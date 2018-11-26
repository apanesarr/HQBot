
import screen
import localocr
from wiki import Wiki
from google_search import GoogleSearch
def main():
    screen.shot()
    question_options = localocr.getText()
    wiki_search = Wiki(question_options['question'], question_options['options'])
    wiki_result = wiki_search.getResults()
    google_search = GoogleSearch()
    google_search_result = google_search.getResult(question_options['question'], question_options['options'])
    
    
if __name__== '__main__':
    main()