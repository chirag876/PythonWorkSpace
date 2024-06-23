# -*- coding: utf-8 -*-

##########################
# AUTHOR : AMAN SINGHAL
##########################

#built-in modules
import random

# third-party modules
import json
import torch
import configparser

# our modules
from .model import NeuralNet
from .nltk_utils import bag_of_words, tokenize
from .api_adapter import ApiAdapter

config = configparser.ConfigParser()
config.read("config.cfg")

class Bot:

    # initializing all variables in this function
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        # loading intents.json
        with open(config['PATH']['INTENTS'], 'r') as f:
            self.intents = json.load(f)
        #loading events.json
        with open(config['PATH']['EVENT_TRIGGER'], 'r') as f2:
            self.events = json.load(f2)

        self.FILE = config["PATH"]["DATA"]
        self.data = torch.load(self.FILE) # loading training model
        self.input_size = self.data['input_size'] # getting input size from data
        self.hidden_size = self.data['hidden_size'] # getting hidden size from data
        self.output_size = self.data['output_size'] # getting output size from data
        self.all_words = self.data['all_words'] # getting all words from data
        self.tags = self.data['tags'] # getting tags from data
        self.model_state = self.data['model_state'] # getting model_state from data
        # Putting all values from training model into neural network
        self.model = NeuralNet(self.input_size, self.hidden_size, self.output_size).to(self.device) 
        self.model.load_state_dict(self.model_state)
        # it is a kind of switch for some specific layers/parts of the model that behave differently during training and inference (evaluating) time. 
        self.model.eval()

        self.bot_name = "Alice" # variable to store bot name
        self.last_tag = ""  # variable store last tag. Default value will be none
        self.api_params = [] # an empty list to store API parameters entered by user
        self.event_key = "" # variable to store last event occured
        self.welcome = "welcome"

    # This function gets the tag name for a particular message 
    def __get_tag(self, message):
        # tokenizing the message
        self.tokenize_sentence = tokenize(message)
        # creating bag of words
        self.x = bag_of_words(self.tokenize_sentence, self.all_words)
        self.x = self.x.reshape(1, self.x.shape[0]) 
        # creating the input data to pass into neural network
        self.x = torch.from_numpy(self.x)
        # getting the output after passing the input data into neural network model
        self.output = self.model(self.x)
        # predecting the tag which have maximum value in output. it will return a dict of predictions
        _, self.predicted = torch.max(self.output, dim=1)
        # getting tag name from predicted dict
        self.tag = self.tags[self.predicted.item()]
        # The softmax activation function is a common way to encode categorical targets in many machine learning algorithms. Tensor rescaling the inputs so that the elements of the n-dimensional output Tensor lie in the range [0,1] and sum to 1.
        self.probs = torch.softmax(self.output, dim=1)
        # getting the probability value
        self.prob = self.probs[0][self.predicted.item()]
        # checking if probability value is under defined value to return the tag name
        if self.prob.item() > 0.95:
            return self.tag


    # This function identify if current tag is dependent on last tag or not. If there is no dependent it will return none
    def __check_tag_dependency(self, tag):
        for intent in self.intents["intents"]:
            if tag == intent['tag']:
                if intent['dependent']:
                    if self.last_tag in intent['dependent']:
                        return True
                    else:
                        return False
                else:
                    return None

    # This function calls the API                                                                                        
    def __get_event(self, tag):
        api_object = ApiAdapter(self.api_params)
        return api_object.call_api(tag)

    # get a response for a particular tag       
    def __get_tag_response(self, tag):
        for intent in self.intents["intents"]:
            if tag == intent["tag"]:
                return [random.choice(intent['responses']), intent['buttons']]

    # get the response for a message
    def __get_response(self, message):
        self.tag = self.__get_tag(message)
        for intent in self.intents["intents"]:
            if self.tag == intent["tag"]:
                self.api_params = []
                self.buttons = intent["buttons"]
                self.response = {
                "response": [],
                "buttons": []
                }
                # checking the tag dependency
                if self.__check_tag_dependency(self.tag):
                    self.last_tag = self.tag
                    if self.last_tag in self.events.keys():
                        self.event_key = self.last_tag 
                    self.response['response'].append(random.choice(intent['responses']))
                    self.response['buttons'].append(self.buttons)
                    return self.response
                elif self.__check_tag_dependency(self.tag) ==  None:
                    self.last_tag = self.tag
                    if self.last_tag in self.events.keys():
                        self.event_key = self.last_tag 
                    self.response['response'].append(random.choice(intent['responses']))
                    self.response['buttons'].append(self.buttons)
                    return self.response
                else:
                    self.response['response'].append("Sorry, I do not understand. Please choose from below")
                    self.event_key = self.welcome
                    self.response['buttons'].append(self.buttons)
                    return self.response
            # If no tags found means user have entered some value and storing that value in api parameters 
            elif self.tag == None and message != "":
                self.response = {
                "response": [],
                "buttons": []
                }
                self.api_params.append(message)
                # checking if last tag is part of events
                if self.last_tag in self.events.keys():
                    for element in self.events[self.last_tag]:
                        if  element in self.tags:
                            self.last_tag = element
                            tag_res = self.__get_tag_response(element)
                            self.response['response'].append(tag_res[0])
                            self.response['buttons'].append(tag_res[1])
                        elif element not in self.tags:
                            self.api_result = self.__get_event(element)
                            self.api_params = []
                            self.response['response'].append(self.api_result)
                            self.response['buttons'].append([])
                    return self.response
                else:
                    del self.api_params[-1]
                    self.response['response'].append("Sorry, I do not understand. Please choose from below")
                    self.event_key = self.welcome
                    self.buttons = intent["buttons"]
                    self.response['buttons'].append(self.buttons)
                    return self.response
            elif self.tag == None and message == "":
                self.response['response'].append("Sorry, I do not understand. Please choose from below")
                self.event_key = self.welcome
                self.buttons = intent["buttons"]
                self.response['buttons'].append(self.buttons)
                return self.response

    
    # this is the main function which runs the bot when we run main.py file. 
    def run(self, message):
        response = self.__get_response(message)
        print(response["response"][0])
        #print(self.event_key)
        print(self.last_tag)
        if response["response"][0] == "continue":
            return self.__get_response(self.event_key)
        else:
            return response