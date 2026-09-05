'''importing the recommended module for the text normalization'''
import re
import string
import emoji
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


'''Creating an class for the Text_Normalization'''
class Text_Normalization:

    '''Creating an Instance and Instance variable '''
    def __init__(self,emoji=True,Punctuation=True,stop_words=True,lemma_words=True):
        self.emoji=emoji
        self.punctuation=Punctuation
        self.stop_words=stop_words
        self.lemma_words=lemma_words

    '''Creating an Method for cleaning an emoji and punctuation and stop words'''
    def clean_data(self,text):

        '''clean the emoji'''
        if self.emoji:
            text=re.sub(r'[^a-zA-Z0-9\s]','',text)
            text = emoji.replace_emoji(text,replace='') 

        '''remove the punctuation'''
        if self.punctuation:
            str_p = string.punctuation
            str_p = str_p.replace('.','')
            text=re.sub(f'[{str_p}]','',text)

        '''remove the stop_words'''
        if self.stop_words:
            words = text.split()
            stop_word = stopwords.words('english')

            '''
            Creating an empty list, checking each word against
            the stop-word list, storing the non-stop words,
            and joining them back into text.
            '''
            clean_word = []
            for word in words:
                if word not in stop_word:
                    clean_word.append(word)
            text=" ".join(clean_word)   


        '''here we apply the lemmatization for makeing the words into the original root form by the pos '''
        if self.lemma_words:
            words = text.split()
            lem = WordNetLemmatizer() 
            pos_tag_word = nltk.pos_tag(words)
            
            def find_postag(tag):

                if tag.startswith('N'):
                    return 'n'

                elif tag.startswith('V'):
                        return 'v'

                elif tag.startswith('J'):
                            return 'a'

                elif tag.startswith('R'):
                            return 'r'

                else:
                        return 'n'

        clean_word = []
        for word,tag in pos_tag_word:
            tagged_word = lem.lemmatize(word,pos=(find_postag(tag)))
            clean_word.append(tagged_word)
        text=" ".join(clean_word)


        ''' And we return the text '''
        return text


'''object creation for the Class '''
obj = Text_Normalization(emoji=True,Punctuation=True,stop_words=True,lemma_words=True)


'''text = [Open the file and read that and stored in the text variable for the clean_data method process]'''
with open("data.txt",'r',encoding='utf-8') as file:
    text = file.read()

'''we calling the clean data class by using an object and store in the variable result'''
result = obj.clean_data(text)


'''We store the clean text in the new file by using the result '''
with open('clean_words_after_lem','w',encoding='utf-8') as file:
    file.writelines(result)

            
        