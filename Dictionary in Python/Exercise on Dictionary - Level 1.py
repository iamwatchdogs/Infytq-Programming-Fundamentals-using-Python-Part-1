# Problem Statement
# Represent a small bilingual (English-Swedish) glossary given below as a Python dictionary
#
# {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"} 
#
# and use it to translate your Christmas wishes from English into Swedish.
#
# That is, write a python function translate() that accepts the bilingual dictionary and a list of English words (your Christmas wish) 
# and returns a list of equivalent Swedish words. 

#lex_auth_012693774187716608134

def translate(bilingual_dict,english_words_list):
    #Write your logic here
    swedish_words_list = list()
    for i in english_words_list:
        swedish_words_list.append(bilingual_dict[i])

    return swedish_words_list


bilingual_dict= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
english_words_list=["merry","christmas"]
print("The bilingual dict is:",bilingual_dict)
print("The english words are:",english_words_list)

swedish_words_list=translate(bilingual_dict, english_words_list)
print("The equivalent swedish words are:",swedish_words_list)
