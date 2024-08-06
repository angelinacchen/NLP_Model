import spacy
import pandas as pd


model = '/Users/angelinachen/Downloads/NER_Output'
nlp = spacy.load(model)

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
    "Is anyone in the airport rn ",
    "I’m landing at 5:19. Anyone at the airport now or in the next hour and would want to Uber?",
    "Just a PSA: sometimes it can be cheaper to call a second Uber if you don't mind waiting. Otherwise, it can use the airport price for the second stop which is usually way higher.",
    "Jesse Gui added Charles Ascone to the group.",
    "Shraddha Hariharan added Shreya Ramanathan to the group.",
    "Okay, then I’m fine with sharing a ride with you.",
    "No, but we can do two stops.",
    "Anyone landing around 6:45-7 and want to split an Uber or Lyft to Clairmont?",
    "Are you going to Clairmont campus?",
    "Does anyone wanna split an Uber soon? I'm headed to baggage claim now.",
    "If anyone lands or is in the airport around 4, DM me if you wanna split an Uber.",
    "Anyone landing at 1:30 on the 9th?",
    "Is anyone arriving around 3:40-4ish who wants to split an Uber?",
    "Kasandra Schroeder has joined the group.",
    "Sarah Broder has joined the group.",
    "Jared Kupersmith has left the group.",
    "I’m at the airport but going to Woodruff! And going to Clairmont campus?",
    "Anyone at the airport right now?",
    "Yousef Rajeh has joined the group.",
    "Anyone at the airport Friday around 2:30 and want to split an Uber? 🫣",
    "Anyone leaving for the airport around 5 am on Saturday, March 4, and want to split an Uber?",
    "Tiantian Li has left the group.",
    "Anyone have a flight around 9 am on Saturday, March 4?",
    "Is anyone leaving at 5:00 pm on Thursday, 3/2?",
    "Anyone leaving Saturday at 3:30 am to the airport?",
    "Anyone leaving at 11:30 am on Thursday, 3/2?",
    "Anyone for 11:30 am Saturday?",
    "Anyone landing @9:30pm Sunday night?",
    "Anyone landing around 2pm Sunday evening?",
    "Anyone landing around 9 am Sunday morning",
    "Anyone landing around 6:30 pm tomorrow (main campus)",
    "anyone landing around 3:30 today and want to uber back to main?",
    "Anyone landing around 3:50 pm tomorrow?",
    "Is anyone going to the airport at 6pm tomorrow"
]
entity_labels = ["date", "time", "dest", "origin", "spam", "rep", "rn"]

data_list = []

# Process each sentence and collect data in the list
for sentence in test_sentences:
    doc = nlp(sentence)
    entities_dict = {label: None for label in entity_labels}

    for entity in doc.ents:
        if entity.label_ in entities_dict:
            entities_dict[entity.label_] = entity.text

    # Add the sentence and entity values to the list
    row_data = [sentence] + list(entities_dict.values())
    data_list.append(row_data)

# Convert the list to a DataFrame
columns = ["Text"] + entity_labels
new_data_df = pd.DataFrame(data_list, columns=columns)

# Concatenate the new DataFrame to the original DataFrame (if it exists)
# If it doesn't exist, assign the new DataFrame to the original DataFrame
original_df = pd.concat([original_df, new_data_df], ignore_index=True) if 'original_df' in locals() else new_data_df

original_df = original_df.fillna("null")

# Export the DataFrame to an Excel file
output_excel_path = '/Users/angelinachen/Downloads/RIDEmoryNLP.xlsx'
original_df.to_excel(output_excel_path, index=False)

print(f"Data exported to {output_excel_path}")
