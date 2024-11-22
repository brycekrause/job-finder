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

print("Please wait...", end='')
for r in url_array:
    print(".", end='')
    response = requests.get(r).json()
    responses.append(response)


while True:
    print(f'responses[] has {len(responses)} elements')
    index = int(input('What index? (1-6) '))
    print(responses[index-1])
