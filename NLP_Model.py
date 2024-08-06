from __future__ import unicode_literals, print_function
from spacy.training.example import Example

from thinc.api import compounding
from spacy.util import minibatch
import random
from pathlib import Path
import spacy
from tqdm import tqdm


text_file_path = '/Users/angelinachen/Downloads/trainingdatacopy.txt'
def load_train_data(file_path):
    with open(file_path, 'r') as file:
        train_data = eval(file.read())
    return train_data

TRAIN_DATA = load_train_data(text_file_path)


model = '/Users/angelinachen/Downloads/NER_Output'
output_dir= '/Users/angelinachen/Downloads/NER_Output'
n_iter=100

#load the model

nlp = spacy.load(model)
print("Loaded model '%s'" % model)


#set up the pipeline

if 'ner' not in nlp.pipe_names:
    nlp.add_pipe('ner', last=True)
    ner = nlp.get_pipe('ner')
else:
    ner = nlp.get_pipe('ner')

for _, annotations in TRAIN_DATA:
    for ent in annotations.get('entities'):
        ner.add_label(ent[2])



# Disable other pipelines during training
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
with nlp.disable_pipes(other_pipes):
    if model is None:
        optimizer = nlp.initialize()
    else:
        optimizer = nlp.resume_training()


    def make_iterable(schedule):
        step = 0
        while True:
            yield schedule(step)
            step += 1

    batch_sizes = compounding(4.0, 32.0, 1.001)
    batch_sizes_iterable = make_iterable(batch_sizes)

    # Training loop
    for itn in range(n_iter):
        random.shuffle(TRAIN_DATA)
        losses = {}


        batch_sizes = compounding(4.0, 32.0, 1.001)
        for batch in minibatch(TRAIN_DATA, size=batch_sizes_iterable):
            examples = []
            for text, annotations in batch:
                # Create Example objects
                doc = nlp.make_doc(text)
                examples.append(Example.from_dict(doc, annotations))

            # Update the model
            nlp.update(
                examples,
                drop=0.1,  # Dropout - make it smaller if you train longer
                losses=losses,
                sgd=optimizer  # Pass in the optimizer if resuming training or initializing
            )
        print(losses)

for text, _ in TRAIN_DATA:
    doc = nlp(text)
    print('Entities', [(ent.text, ent.label_) for ent in doc.ents])



for itn in range(n_iter):
    random.shuffle(TRAIN_DATA)
    losses = {}
    # Wrap TRAIN_DATA with tqdm for a progress bar
    for text, annotations in tqdm(TRAIN_DATA, leave=False):
        nlp.update(
            examples,  # Batch of annotations
            drop=0.5,  # Dropout - make it harder to memorise data
            sgd=optimizer,  # Callable to update weights
            losses=losses)
    print(losses)

if output_dir is not None:
    output_dir = Path(output_dir)
    if not output_dir.exists():
        output_dir.mkdir()
    nlp.to_disk(output_dir)
    print("Saved model to", output_dir)


# Example sentences to test the model's understanding
test_sentences = [
    "Anyone landing 5:30 today ",
    "Anyone going to the airport today? ",
    "Anyone going to the airport Monday afternoon ",
    "Is anyone going to the airport tmr morning ? ",
    "This message was deleted ",
    "i landed waited on an uber with someone else are u main or clairmont ? ",
    "Main ",
    "Same here ",
    "Just landed, anyone landing soon? ",
    "anyone landing 8:30 am ",
    "Is anyone in the airport rn "
]

# Process each sentence and print the entities recognized by the model
for sentence in test_sentences:
    doc = nlp(sentence)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    print(f"Sentence: '{sentence}'")
    if entities:
        print("Entities:", entities)
    else:
        print("No entities found.")
    print("")
