# from translator import Translator

# translator = Translator(from_langue = "french", to_langue = "english")
# french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

# new_dict ={}

# for i in french_words:
#     new_dict[translator.translate(i)] = i

# print(new_dict)


from translator import Translator

translator = Translator()

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

translation_words = {w: translator.translate(w, dest="en").text for w in french_words}
print(translation_words)