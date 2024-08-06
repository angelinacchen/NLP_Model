import spacy
from spacy.training.example import Example
from spacy.scorer import Scorer

# Load the trained model
nlp = spacy.load('/Users/angelinachen/Downloads/NER_Output_Multi')



test_data = [("yeah i am ",{"entities":[(0,9,"rep")]}),
("Anyone landing at 1:30? ",{"entities":[(18,22,"time")]}),
("This message was deleted ",{"entities":[(0,24,"spam")]}),
("Anyone landing around 5:30 today? ",{"entities":[(27,32,"date"),(22,26,"time")]}),
("Anyone landing at 12am tonight and going to Clairmont? ",{"entities":[(44,53,"dest"),(23,30,"date"),(18,22,"time")]}),
("Anybody at the airport rn? ",{"entities":[(23,25,"time"),(15,22,"origin")]}),
("I ammm ",{"entities":[(0,6,"rep")]}),
("Anyone at the airport rn? ",{"entities":[(22,24,"time"),(14,21,"origin")]}),
("Anyone going back to Oxford at 6:30PM tomorrow? ",{"entities":[(21,27,"dest"),(31,37,"time"),(38,46,"date")]}),
("anyone landing at around 4:30? ",{"entities":[(25,29,"time")]}),
("anyone landing at 5:15pm today ",{"entities":[(18,24,"time"),(25,30,"date")]}),
("Anyone landing at 9pm going to main? ",{"entities":[(31,35,"dest"),(18,21,"time")]}),
("This message was deleted ",{"entities":[(0,24,"spam")]}),
("anyone land ~8pm going to main? ",{"entities":[(13,16,"time"),(26,30,"dest")]}),
("Anyone at the airport rn? ",{"entities":[(14,21,"origin"),(22,24,"time")]}),
("Anyone landing @9:30pm tonight going to Clairmont? ",{"entities":[(16,22,"time"),(40,49,"dest")]})
]

scorer = Scorer()
examples = []
for text, annots in test_data:
    predicted=nlp(text)
    example=Example.from_dict(predicted, annots)
    examples.append(example)
scorer.score(examples)

print(scorer.score(examples))
