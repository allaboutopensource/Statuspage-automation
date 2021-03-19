#!/usr/bin/python3
import requests
import json
import sys
import argparse
url = 'https://api.statuspage.io/v1/pages/<page-id>/incidents/'
parser = argparse.ArgumentParser()
parser.add_argument("Issue")
parser.add_argument("Component")
args = parser.parse_args()
if args.Component == 'AWS':
    component_id= "xxxxxxxxxxx"
elif args.Component == 'Azure':
    component_id="xxxxxxxxxxx"
elif args.Component == 'Openstack':
    component_id="xxxxxxxxx"
elif args.Component == 'Storage':
    component_id="xxxxxxxxxxxx"
else:
    print ("No component Found")
    exit()
# Set proper headers
headers = {
    'Authorization': 'OAuth <Auth code>',
}
#print (component_id)
values={
  "incident" : {
       "name": args.Issue,
       "impact_override": "critical",
       "status":"investigating",
       "body": "This is the auto email",
       "components": {
         component_id: "major_outage"
       },
       "component_ids": [
            component_id
       ]
  }
}


# Do the HTTP request
response = requests.post(url, headers=headers, json = values)
# Check for HTTP codes other than 201
if response.status_code != 201:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print (data)
