import requests
import datetime
import sys
import pyimgur
import urllib2
import urllib
import json
import webbrowser
import demjson

now = datetime.datetime.now()

#imgur API
client_id = '553a684bfb74c46'
im = pyimgur.Imgur(client_id)
client_secret = 'a3c9db6724915332b454256493cbb0e854db1e5e'



# The project I based this project off of was based on some code by @gersteinj.
# My project is based off of The Python Alliance
#https://github.com/MC42/the-python-alliance/blob/master/thepythonalliance.py

initials = 'MW'
github = "https://github.com/Max5254/"
teamToHighlight = str("5254")

baseURL = 'http://www.thebluealliance.com/api/v2/'
header = {'X-TBA-App-Id': 'frc5254:thepythonalliance:beta'}


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class tba:
    def get_team(self):
        team = raw_input('Please enter a team:')
        myRequest = (baseURL + 'team/frc' + str(team))
        response = requests.get(myRequest, headers=header)
        jsonified = response.json()
        print(bcolors.HEADER + 'Team Information for FRC' + str(team) + bcolors.ENDC)
        if jsonified['location'] != None:
            if jsonified['nickname'] != None:
                print('Team Nickname: \t' + bcolors.OKGREEN + jsonified['nickname'] + bcolors.ENDC)
            if jsonified['name'] != None:
                print('Team Full Name: ' + bcolors.OKGREEN + jsonified['name'] + bcolors.ENDC)
            print('Team Number: \t' + bcolors.OKGREEN + str(jsonified['team_number']) + bcolors.ENDC)
            if jsonified['website'] != None:
                print('Website: \t' + bcolors.OKGREEN + jsonified['website'] + bcolors.ENDC)
            print('Rookie Year: \t' + bcolors.OKGREEN + str(jsonified['rookie_year']) + bcolors.ENDC)
            print('\t' + bcolors.OKBLUE + 'Location Data:' + bcolors.ENDC)
            if jsonified['locality'] != None:
                print('Locality: \t' + bcolors.OKGREEN + jsonified['locality'] + bcolors.ENDC)
            if jsonified['location'] != None:
                print('Location: \t' + bcolors.OKGREEN + jsonified['location'] + bcolors.ENDC)
            if jsonified['country_name'] != None:
                print('Country: \t' + bcolors.OKGREEN + jsonified['country_name'] + bcolors.ENDC)
        if (jsonified['location'] == None) and (jsonified['website'] == None):
            print('\nThere is no information avalible for Team ' + bcolors.HEADER + str(
                team) + bcolors.ENDC + '\nThis team has likely since been dissolved.')
        if (team == teamToHighlight):
            print(bcolors.WARNING + 'You\'re looking at your own team.  Or you\'re debugging...' + bcolors.ENDC)

    def get_team_name(self, team_no):

        myRequest = (baseURL + 'team/frc' + str(team_no))
        response = requests.get(myRequest, headers=header)
        jsonified = response.json()
        return jsonified['nickname']

    def get_team_event_key(self, team, year):
        myRequest = (baseURL + 'team/frc' + str(team) + '/' + str(year) + '/events')
        response = requests.get(myRequest, headers=header)
        jsonified = response.json()
        for x in range(0 , len(jsonified)):
            print (jsonified[x]['key'])
        #if jsonified['location'] != None:
        #    if jsonified['nickname'] != None:
        #      print('Team Nickname: \t' + bcolors.OKGREEN + jsonified['nickname'] + bcolors.ENDC)
        #if (jsonified['location'] == None) and (jsonified['website'] == None):
        #   print('\nThere is no information avalible for Team ')

    def get_team_event_matches(self, eventKey, team):
        myRequest = (baseURL + 'team/frc' + str(team) + '/event/' + str(eventKey) + '/matches')
        response = requests.get(myRequest, headers=header)
        jsonified = response.json()
        print  jsonified
        n = 2
        schedule = [[0 for i in range(2)] for i in range(len(jsonified))]
        teams = [[0 for i in range(5)] for i in range(len(jsonified))]
        print schedule
        #schedule.append([])
        #schedule.append([])
        for x in range(0 , len(jsonified)):
            schedule[x][0] = (str(jsonified[x]['comp_level']) +  str(jsonified[x]['match_number']))

            for y in range (0,3):
                blueTeams =  jsonified[x]['alliances']['blue']['teams'][y]
                blueTeams = blueTeams[3:]
                redTeams = jsonified[x]['alliances']['red']['teams'][y]
                redTeams = redTeams[3:]
                print blueTeams
                print redTeams
        print schedule


    def img(self):
        teamNumber = raw_input("please enter a team number: ")
        myRequest = (baseURL + 'team/frc' + str(teamNumber) + '/'+ str(now.year) + "/media")
        response = requests.get(myRequest, headers=header)
        jsonified = response.json()
        print(jsonified)
        key = ""
        if jsonified != None:
            type = jsonified[0]['type']
            if type == "imgur":
                key = jsonified[0]['foreign_key']
                print key
            image = im.get_image(key)
            print(image.link)
            imgURL = ("www." + str(type)  + ".com/" + str(key))
            message = ("""<html>
            <body>
            <h1>Team """ + str(teamNumber) +  """ 2016 Robot</h1>
            <img src=""" + str(image.link) + """>
            </body>
            </html>""")

            filename = 'RobotImage.html'
            f = open(filename, 'w')
            f.write(message)
            webbrowser.open_new_tab(filename)
            f.close()



print(
bcolors.OKBLUE + ' ________         ___       __  __               ___   _____  \n/_  __/ /  ___   / _ \__ __/ /_/ /  ___  ___    / _ | / / (_)__ ____  _______ \n / / / _ \/ -_) / ___/ // / __/ _ \/ _ \/ _ \  / __ |/ / / / _ `/ _ \/ __/ -_)\n/_/ /_//_/\__/ /_/   \_, /\__/_//_/\___/_//_/ /_/ |_/_/_/_/\_,_/_//_/\__/\__/ \n                    /___/  ' + bcolors.ENDC)

tba = tba()
#tba.img()
#tba.get_team_event_key(5254, 2016)
#print ''
tba.get_team_event_matches('2016iri' , '5254')


