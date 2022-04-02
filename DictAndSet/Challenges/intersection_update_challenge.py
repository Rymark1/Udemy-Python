text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

sentence_list = text.split()
preps_used = prepositions.intersection(sentence_list)
print(preps_used)
