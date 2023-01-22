import spacy

myList1 = ['Mahomes', 'Collinsworth', 'Jags', 'Trevor Lawrence', 'Chiefs', 'Jaguars', 'Chad Henne', 'Eubank', '#UFC283', 'McKinney', 'Agnew', 'Jacksonville', 'Andy Reid', 'Pacheco', 'Calvin Ridley']

myList = ['Giants', 'Eagles', 'Mahomes', 'Collinsworth', 'Daniel Jones', 'Jags', 'Chiefs', '#UFC283', 'McKinney', 'Bradberry', 'Nick Sirianni', '#TogetherBlue', 'Reddick', 'Kelce', 'Chad Henne'
, 'Go Birds', 'Jaylon Smith', '#Svengoolie', 'Evan Neal', 'Danny Dimes', 'Giant Killer', 'Agnew', '#TheWeddingVeil', 'Joe Davis', 'Shogun', 'Jacksonville', 'Andy Reid', 'Goedert', 'Taylor', 'Elon Musk']

myString = "., ".join(myList)

nlp = spacy.load("en_core_web_sm")
doc = nlp(myString)

count = 0
number = 0
print(len(doc.ents))
for ent in doc.ents:
    number += 1
    print(ent.text + "," + ent.label_)

    if (ent.label_ == "PERSON"):
        count += 1
    # print(ent.text, ent.start_char, ent.end_char, ent.label_)

print(count)
print(number)
print(count >= 1)

"""
count = 0
for x in range(len(myList)):
    doc = nlp(myList[x])
    print(doc.ents)
    for ent in doc.ents:
        print(ent.text + "," + ent.label_)

        if (ent.label_ == "PERSON"):
            count += 1
"""