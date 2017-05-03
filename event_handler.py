import time
import os
from slackclient import SlackClient
from file_reader import *
from nlp_parser import process_command,dependecyParse
import MySQLdb

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
BOT_ID = os.environ.get("BOT_ID")
AT_BOT = "<@" + BOT_ID + ">"
db = MySQLdb.connect("localhost","root","******","testdb" )
cursor = db.cursor()


def handle_command(command, channel):
    #call to nlp module
    response = process_command(command)
    dependecyParse(command)
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

#Generate query 
def generateQuery(leaf,head):
    data=None
    print leaf
    print head    
    print leaf
    cursor.execute("SELECT Week, Topics from testdb.CourseSchedule where Topics like ('%s%s');"%("%"+leaf+"%","%"+head+"%"))           
    data = cursor.fetchall()
    print "fetch completed",data,"data"  
    if data:      
        print "Output : %s " % data         
    return data

if __name__ == "__main__":
    print "Trying to connect"
    createDictionary()    
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
