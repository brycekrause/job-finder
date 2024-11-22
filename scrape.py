import json
import requests

general_url = 'https://jobdataapi.com/api/'

regions_url = general_url + 'jobregions'
cities_url = general_url + 'jobcities'
types_url = general_url + 'jobtypes'
jobs_url = general_url + 'jobs'
industries_url = general_url + 'industries'
companies_url = general_url + 'companies'

# put urls in an array for iteration later
url_array = [
    regions_url, 
    cities_url,
    types_url,
    jobs_url,
    industries_url,
    companies_url
    ]

responses = []

def getNext(url):
    response = requests.get(url).json()
    responses.append(response)

    # get every page
    try:
        getNext(response['next'])
    except:
        print('No value found for [next]')

for r in url_array:
    # make the request TODO: add exception handling
    response = requests.get(r).json()
    responses.append(response)

    # if there are multiple pages
    try:
        # TODO: find 'next' index. rate limited atm.
        getNext(response["next"])
        print(response['next'])
    except:
        print('No value found for [next]')

c = 0
for i in responses:
    filename = str(f"data{str(c)}.json")
    # write to a newly created file
    with open(filename, 'w') as file:
        json.dump(response, file, indent=4, separators=(',', ':'))
        c += 1 # changes the filename


while True:
    print(f'responses[] has {len(responses)} elements')
    index = int(input('What index? (1-6) '))
    print(responses[index-1])