
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
    wiki_index = wiki_result.index(max(wiki_result))
    google_index = google_search_result.index(max(google_search_result))

    
    print("WIKI FOUND: " + str(question_options['options'][wiki_index]) + "\t Frequency of Option: " + str(wiki_result[wiki_index]))
    print("GOOGLE FOUND: " + str(question_options['options'][google_index]) +"\t Number of Results: " + str(google_search_result[google_index]))

if __name__== '__main__':
    main()