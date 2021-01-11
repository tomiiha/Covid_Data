from requests import get
import pandas as pd
import datetime

# Standard get request
def get_data(url):
    try:
        response = get(endpoint, timeout=10)
    except:
        return print("Request failed")
    return response.json()

# What variables to be captured
variables = '{"date":"date","newCases":"newCasesByPublishDate","hospitalcases":"hospitalCases"}'

# Endpoint contains data to be requested
endpoint = (
        'https://api.coronavirus.data.gov.uk/v1/data?'
        'filters=areaType=nation;areaName=england&'
        'structure=' + variables)

# Pull data
data = get_data(endpoint)

# Convert to dataframe
df = pd.DataFrame.from_dict(data['data'], orient='columns')

# Empty list
file_urls = []

# Vaccination data file pull
def vax_capture(vax_source):
    import requests as reqs
    from bs4 import BeautifulSoup as bsoup
    vax_source = 'https://www.england.nhs.uk/statistics/statistical-work-areas/covid-19-vaccinations/'
    file_page = bsoup(reqs.get(vax_source).content, 'html.parser')
    file_capture = file_page.find_all('p')
    for x in file_capture:
        add = x.find_next('a').attrs['href']
        if add.endswith('.xlsx'):
            file_urls.append(add)
    return vax_parse(file_url[0])

print(file_urls)

# Parse latest file for data
def vax_parse(file_url):
    source_get = reqs.get(file_url).content
    # Capture data for handling - io used to not require local instance.
    data_set = pd.read_excel(io.StringIO(source_get.decode('utf-8')), thousands=',')
    return total_vax
    
vax_capture(vax_source)
