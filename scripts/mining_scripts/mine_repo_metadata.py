# Get SonarCloud API

import requests
import json
import math
import csv

page_size = 500
repo_number = 0
repo_row = []
spec_repo_list = []
repo_url = []
repo_key = []
bool_github = []


# load repositories from json generated from repo_getter.py
with open('repos.json') as json_data:
    repos_dict = json.load(json_data,)

url = 'https://sonarcloud.io/api/measures/component?'

j = 0
# merge this for loop with the next one so that the whole thing is done once per repo
for repo in repos_dict:
    repo_key = repo['key']

    query = {'componentKey': repo_key, 'metricKeys': 'duplicated_blocks,duplicated_lines,duplicated_lines_density,violations,false_positive_issues,open_issues,confirmed_issues,reopened_issues,code_smells,sqale_rating,sqale_index,sqale_debt_ratio,bugs,reliability_rating,reliability_remediation_effort,vulnerabilities,security_rating,classes,comment_lines,comment_lines_density,directories,files,lines,ncloc,ncloc_language_distribution,functions'}

    r = requests.get(url, params=query)
    repo_specs_new = r.json()

    spec_repo_list.append(repo_specs_new)

    j += 1

with open('repos_spec.json', 'w') as fout:
    json.dump(spec_repo_list, fout)


with open('repos_spec.json') as json_data:
    repos_dict = json.load(json_data,)

for repo in repos_dict:

    key = repo['component']['key']
    
    measurement_iterator = 0

    measurements_tuples = []

    for measure in repo['component']['measures']:
        metric = repo['component']['measures'][measurement_iterator]['metric']
        value = repo['component']['measures'][measurement_iterator]['value']
        
        # create array of tuples (metric, value)
        measurements_tuples.append((metric, value))

        measurement_iterator += 1 

    # sort metrics alphabetically
    measurements_tuples.sort()

    # write row of measurements for csv file
    repo_row.append([x[1] for x in measurements_tuples])

    repo_number += 1

with open('metadata_sonarcloud.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    
    for row_number in range(0, repo_number):
        writer.writerow(repo_row[row_number])

csvFile.close()

with open('repos.json') as json_data:

repo_number = 0
ok_repos = 0
not_ok_repos = 0
repo_row = []
i=0  
repos = json.load(json_data,)
    
    for row_number in range(0, repo_number):
        writer.writerow(repo_row[row_number])

csvFile.close()


    