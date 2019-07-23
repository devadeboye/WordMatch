import re
import nltk
import json
from nltk.corpus import words
# download word database
#nltk.download('words') #uncomment the preceeding code to download dict of english words

class FindMatch:
    """
    The FindMatch class accepts a string and looks into the
    english dictionary to look for word that relates to it and
    also give the percentage closeness.

    The result of the search is written to a json file.

    PARAMETER
    The constructor for the class takes in a single parameter
    pat, which is the string whose related words we want to 
    find.

    METHOD
    start() - This kick start the search and coordinate every
    necessary activities.
    """

    def __init__(self, pat):
        """
        Constructor for the FindMatch class.

        PARAMETER
        pat - word to use as pattern for the regular expression
        """
        # carries related words
        self.__related_wd = dict()
        # collection of english words
        self.__eng_dict = words.words()
        # pattern
        self.pat = pat

    
    def __find_p(self, wd):
        """
        looks for a pattern in a word

        PARAMETER
        wd - word to be compared with our regex pattern
        """
        # create pattern
        pat_regex = re.compile(r'(\D*){}(\D*)'.format(self.pat))
        k = pat_regex.search(wd)

        # if there is a match
        if k:
            # calculate the %age of our pattern in wd
            p = round(((len(self.pat)/len(wd))*100), 2)
            self.__related_wd[wd] = '{}%'.format(p)

    
    def __search_dict(self):
        """
        searchs an english dictionary for matching words
        """
        # find pattern in english dict
        for cont in self.__eng_dict:
            self.__find_p(cont)


    def __write_json(self):
        """
        writes the json object to file
        """
        # open a file
        with open('rel_words.json', 'w') as outfile:
            # if no math in the english dict
            if len(self.__related_wd) == 0:
                raise Exception('Nothing to write to file!')
            else:
                # write json to file
                json.dump(self.__related_wd, outfile)

    @property
    def staart(self):
        """
        kick start the search operation
        """
        try:
            self.__search_dict()
            self.__write_json()
            print('done!')
            print('{} match found and written to file.'\
                .format(len(self.__related_wd)))
        except:
            print('No Match found!')












#-----------------------------------------------
if __name__ == "__main__":
    # search for words matching this value
    FindMatch('cake').staart