# RIDEmory NLP Model 🚗🤖

This repository contains the NLP model component of the RIDEmory project. The NLP model is designed to extract and interpret ride information from GroupMe messages, providing users with seamless ride-sharing details.

> **Note:** The full RIDEmory project, which includes other features and components, can be found at this [link](https://github.com/project-emory/RIDEmory).

## Table of Contents

- [Overview](#overview)
- [NLP Model Features](#nlp-model-features)
- [Data Annotation Format](#data-annotation-format)
- [How to Run This Model](#how-to-run-this-model)
- [Example Responses](#example-responses)
- [License](#license)

## Overview

The NLP model in this repository is a core component of the RIDEmory system, tasked with extracting relevant entities and classifying message types from ride-related communications within GroupMe. The model supports seamless ride-sharing coordination among Emory students by accurately parsing messages to determine key details such as origin, destination, time, and date.

## NLP Model Features

- **Named Entity Recognition (NER):**  
  - Detects and classifies entities such as time, date, origin, and destination within text messages.
  - Recognizes additional categories like spam messages and immediate departures.
 
- **Message Classification:**  
  - Determines the type of message (e.g., ride request, offer, confirmation) to streamline information processing.

- **Integration with GroupMe:**  
  - Parses messages from GroupMe for accurate and up-to-date ride information extraction.
  - Provides real-time insights into ride-sharing opportunities.

## Data Annotation Format

The model uses annotated text data for training and evaluation, formatted as follows:

```python
("Anyone leaving main campus at 7:30pm on Friday?", {"entities": [[15, 26, "origin"], [27, 33, "time"], [37, 43, "date"]]})
```

## Supported Entities

- **Date:** Recognizes dates mentioned in messages.
- **Time:** Identifies specific times.
- **Destination (dest):** Detects the destination locations.
- **Origin:** Recognizes the starting point of a trip.
- **Spam Message (spam):** Flags irrelevant or spam messages.
- **Reply (rep):** Identifies replies within a conversation.
- **Immediate Departure (rn):** Detects messages about immediate departures.

## How to Run This Model

### Training Data:

- **File:** `Training_Data.txt`
- **Description:** This text file contains annotated text data used to train the model.

### Exporting Results:

- **File:** `Export_Test`
- **Description:** This file showcases the entities found in test messages and then exports the results to an Excel file.
- **Example:**

  ![Excel Document Example](https://github.com/user-attachments/assets/b579e131-84ec-4252-ac70-b693cef50a53)

### Testing Model Accuracy:

- **File:** `Accuracy_Test`
- **Description:** This file tests the accuracy of the model.
- **Accuracy:** 83%

### Model Training:

- **File:** `NLP_Model`
- **Description:** This file contains the NLP model that is continuously being trained when new training data is added to the `Training_Data.txt` file. The model is saved in the `NER_Output` folder.

### Steps to Run

1. Ensure you have Python and spaCy installed. You can install spaCy using pip:
   ```bash
   pip install spacy
   ```
2. Download and install the English language model:
  ```bash
   python -m spacy download en_core_web_sm
  ```

3. Train the model by executing the training script:
  ```bash
   python NLP_Model.py
```

4. Test the model by running the accuracy test script:
  ```bash
   python Accuracy_Test.py
```

5. View the results exported to an Excel file for detailed analysis.
   


## Example Responses

Here are some example sentences processed by the model, showcasing its ability to extract relevant information:

- **Input:** "Anyone landing 5:30 today"
  - **Entities Extracted:** `[(5:30, 'time'), (today, 'date')]`

- **Input:** "Anyone going to the airport Monday afternoon"
  - **Entities Extracted:** `[(airport, 'dest'), (Monday afternoon, 'time')]`

- **Input:** "i landed waited on an uber with someone else are u main or clairmont ?"
  - **Entities Extracted:** `[(main, 'origin'), (clairmont, 'dest')]`


## Miscellaneous

Made with ❤️ by the Project Pandas, ©️ Project Emory 2023 under the ⚖️ GNU GPL-3.0 license
