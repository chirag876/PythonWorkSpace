## Installation

### Create an environment
Whatever you prefer (e.g. `conda` or `venv`)
```console
mkdir myproject
$ cd myproject
$ python3 -m venv venv
```

### Activate it
Mac / Linux:
```console
. venv/bin/activate
```
Windows:
```console
venv\Scripts\activate
.\env_chatbot\Scripts\activate
```
### Install PyTorch and dependencies
```
$ pip install -r requirements.txt
```

If you get an error during the first run, you also need to install `nltk.tokenize.punkt`:
Run this once in your terminal:
 ```console
$ python
>>> import nltk
>>> nltk.download('punkt')
```

## Model Training Steps
Run
```console
python train.py
```
This will dump `data.pth` file.

## Customize your dialogues
Have a look at [intents.json](intents.json). You can customize it according to your own use case. Just define a new `tag`, possible `patterns`, possible `responses`, dependency of dialgoues `dependent` and responsive buttons `buttons` for the chat bot. You have to re-run the training whenever this file is modified.
```console
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": [
        "Hi",
        "Hey",
        "How are you",
        "Is anyone there?",
        "Hello",
        "Good day"
      ],
      "responses": [
        "Hey :-)",
        "Hello, thanks for visiting",
        "Hi there, what can I do for you?",
        "Hi there, how can I help?"
      ],
      "dependent: [],
      "buttons": ["Yes", "No"]
    },
    ...
  ]
}
```

### Run ChatBot Service
```console
cd ChatBot_server
python service.py
```

## Output
###### Let's Chat! Type 'quit' to exit
###### Alice: Hello Aman, I am Alice, your Virtual Insurance Assistant
###### You: ping
###### Alice: pong
