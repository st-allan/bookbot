def counter_words(all_words):
    
     list = all_words.split()
     counter = len(list)
     return counter

def character_counter(all_characters):
     lower_case = all_characters.lower()
     characters_dictionary = {}
     for i in lower_case:
          if i in characters_dictionary:
               characters_dictionary[i] +=1
          else:
               characters_dictionary[i] = 1
     return characters_dictionary

def sorted_list_of_dictionaries(characters_dictionary):
     list_of_dictionaries = []
     for char, count in characters_dictionary.items():
          if char.isalpha():
               list_of_dictionaries.append({"char": char, "num": count})
     list_of_dictionaries.sort(key=lambda item:item["num"], reverse=True)
     return list_of_dictionaries
