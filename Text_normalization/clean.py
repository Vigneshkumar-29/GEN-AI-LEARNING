import re
import string
import emoji

class Text_Normalization:
    def __init__(self,emoji=True,Punctuation=True):
        self.emoji=emoji
        self.punctuation=Punctuation

    def clean_data(self,text):

        # clean the emoji
        if self.emoji:
            text=re.sub(r'[^a-zA-Z0-9\s]','',text)
            text = emoji.replace_emoji(text,replace='') 

        # remove the punctuation
        if self.punctuation:
            str_p = string.punctuation
            str_p = str_p.replace('.','')
            text=re.sub(f'[{str_p}]','',text)

        
            return text

# object creation 
obj = Text_Normalization(emoji=True,Punctuation=True)

# text =  "Hello 😊! How are you? I'm learning GenAI 🚀."

with open("data.txt",'r',encoding='utf-8') as file:
    text = file.read()

result = obj.clean_data(text)



print(result)
            
        