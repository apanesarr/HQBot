
import screen
import localocr
from wiki import Wiki
def main():
    screen.shot()
    question_options = localocr.getText()
    
    search = Wiki(question_options['question'], question_options['options'])
    result = search.getResults()
    print(result)
if __name__== '__main__':
    main()