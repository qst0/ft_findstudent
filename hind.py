import os
import sys
import requests

import simplejson as json

if len(sys.argv) > 1:
	with open(sys.argv[1]) as f:
		names = f.readlines()
else:
	print "Usage: python hind.c <login names file>"
	sys.exit()

args = [
	'grant_type=client_credentials',
	'client_id=' + os.environ["FT42_UID"],
	'client_secret=' + os.environ["FT42_SECRET"],
	]

response = requests.post("https://api.intra.42.fr/oauth/token?%s" % ("&".join(args)))

jsondata = response.json()

print jsondata['access_token']

args = [
'access_token=%s' % (jsondata['access_token']),
'token_type=bearer',
'filter[active]=true'
	]

for name in names:	
	response = requests.get("https://api.intra.42.fr/v2/users/" + name.strip() + "/locations?%s" % ("&".join(args)))
	response = response.json()
	if len(response) > 0:
		#print str(json.dumps(response, indent=4, sort_keys=True))
		print name.strip() + " is at computer " + response[0]['host']
	else:
		print "They ain't here, ask around. Someone has to have seen them."
