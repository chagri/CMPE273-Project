import time
import os
from slackclient import SlackClient
import spacy
nlp = spacy.load('en')

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
BOT_ID = os.environ.get("BOT_ID")
AT_BOT = "<@" + BOT_ID + ">"

def handle_command(command, channel):
    response = process_command(command)
    response = dependecyParse(command)
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)

def parse_slack_output(slack_rtm_output):
    output_msgs =slack_rtm_output
    if output_msgs and len(output_msgs) > 0:
        for output in output_msgs:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None

#find dependency between words
def dependecyParse(command):
    #command = "when is the final exam for CMPE273 spring 2017?"
    parsedEx = nlp(command.decode('utf-8'))
    print "---dependency tree----"
    for token in parsedEx:    
        print(token.orth_.encode('utf-8'), token.dep_.encode('utf-8'), token.head.orth_.encode('utf-8'), [t.orth_.encode('utf-8') for t in token.lefts], [t.orth_.encode('utf-8') for t in token.rights])
        #print(token.orth_, token.dep_, token.head.orth_, [t.orth_ for t in token.lefts], [t.orth_ for t in token.rights])
    response = "Sure...write some more code then I can do that!"
    return response

#method to find nouns, verbs ..
def process_command(command):
    #command = "who is the professor for CMPE273 for spring 2017?"
    tokens = nlp(command.decode('utf-8'))
    verbArr =[]
    nounArr = []
    numArr =[]
    entityArr =[]
    AdverbArr = []
    #filter out nouns
    for np in tokens.noun_chunks:
        nounArr.append(np)
        #filter out entities
        for ent in tokens.ents:
            entityArr.append(ent)
            #filter out verbs, numbers and adverbs
            for token in tokens:
                #print token,token.pos_
                if "VERB" in token.pos_:
                    verbArr.append(token)
                elif "NUM" in token.pos_:
                    numArr.append(token)
                elif "ADV" in token.pos_:
                    AdverbArr.append(token)
    print "---nouns----"
    print nounArr
    print "---verbs----"
    print verbArr
    print "--Adverbs---"
    print AdverbArr
    response = "Sure...write some more code then I can do that!"
    #else:
        #response = "I am CMPE bot. How can I help you? Use the *" + EXAMPLE_COMMAND + \
                      #"* command while asking questions."
    return response

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print "StarterBot connected and running!"
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print "Connection failed. Invalid Slack token or bot ID?"