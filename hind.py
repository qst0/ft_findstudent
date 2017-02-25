import os
import sys
import requests

import simplejson as json

debug = False;

if len(sys.argv) > 1:
	with open(sys.argv[1]) as f:
		names = f.readlines()
	if len(sys.argv) > 2 and sys.argv[2] == "debug":
		debug = True;
else:
	print "Usage: python hind.c <login names file>"
	sys.exit()

args = [
	'grant_type=client_credentials',
	'client_id=' + os.environ["FT42_UID"],
	'client_secret=' + os.environ["FT42_SECRET"],
	]

status = requests.post("https://api.intra.42.fr/oauth/token?%s" % ("&".join(args)))
response = status.json()

if status.status_code == 200:
	print "Connected to the 42 API"
else:
	print "You are not connecting to the 42 API please check README.md"

if debug:
	print "Token: " + response['access_token']

args = [
'access_token=%s' % (response['access_token']),
'token_type=bearer',
'filter[active]=true'
	]

for name in names:	
	status = requests.get("https://api.intra.42.fr/v2/users/" + name.strip() + "/locations?%s" % ("&".join(args)))
	response = status.json()
	if len(response) > 0:
		if debug:
			print str(json.dumps(response, indent=4, sort_keys=True))
		print name.strip() + " is at computer " + response[0]['host']
	else:
		if status.status_code == 200:
			print name.strip() + " is not showing up on a computer, ask around!"
		else:
			print name.strip() + " is not a student login on the 42 API"
