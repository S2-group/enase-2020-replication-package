# Get SonarQube issues from SonarCloud API for list of repositories

import requests
import json
import math
import pandas
import time
import random

colnames = ['key', 'url', 'is_on_github', 'bugs', 'classes', 'code_smells', 'comment_lines', 
'comment_lines_density', 'confirmed_issues', 'directories', 'duplicated_blocks', 'duplicated_lines', 
'duplicated_lines_density', 'false_positive_issues', 'files', 'functions', 'lines', 'ncloc', 
'ncloc_language_distribution', 'open_issues', 'reliability_rating', 'reliability_remediation_effort', 
'reopened_issues', 'security_rating', 'sqale_debt_ratio', 'sqale_index', 'sqale_rating', 'violations', 
'vulnerabilities']

# import SonarCloud metadata in dataframe
metadata = pandas.read_csv('total_repo_metadata.csv', names=colnames)
project_key_list = metadata.key.tolist()

# Remove header
project_key_list.pop(0)

all_issues = []
discarded_repos = []


def get_issues(projectKey):
    page_size = 500

    url = 'https://sonarcloud.io/api/issues/search?'

    # Get first page to calculate total number.
    query = {'ps': page_size, 'p': 1, 'asc': 'true', 'componentKeys': projectKey}
    r = requests.get(url, params=query)

    # trottle slightly just to be nice
    time.sleep(random.random() * 2)

    issues_dict = r.json()

    # Total number of issues per project
    total_issues = issues_dict['paging']['total'] 

    # Total number of pages of the project issues
    total_pages = math.ceil(total_issues/page_size)
        
        return None

    else:

        # Iterate over all pages of the projet issue (excluding the first one)
        for p in range (2,total_pages+1):

            query = {'ps': page_size, 'p': p, 'asc': 'true', 'componentKeys': projectKey}
            r = requests.get(url, params=query)
            issues_new = r.json()
            
            # Merge new page results with the old one(s)
            issues_dict['issues'] = (issues_dict['issues'] + issues_new['issues'])

            # trottle slightly just to be nice on the SonarCloud servers
            time.sleep(1)

        del issues_dict['p']
        del issues_dict['ps']
        del issues_dict['paging']
        del issues_dict['components']
        del issues_dict['facets']

        issues_dict['projectKey'] = projectKey

        return issues_dict

current_project = 1

# overrite old dataset file if exsisting, and open json list with "["
with open('issues.json', 'w') as dataset:
   dataset.write('[')

for project in project_key_list:

    print("Current project: ", current_project, "(", project,")")

    # all_issues.append(get_issues(project))

    current_project_issues = get_issues(project)

    if current_project_issues != None:
        with open('issues.json', 'a') as dataset:
            if current_project != 1:
                dataset.write(",")
            dataset.write(json.dumps(current_project_issues))

    current_project += 1

# Close json list with "]"
with open('issues.json', 'a') as dataset:
    dataset.write(']')

with open('issues.json') as json_file:  
    data = json.load(json_file)

    for p in data:
        
        count = 0

        for issue in p['issues']:
            count += 1
        
        print ('Project:', p['projectKey'], '| Issues:', count)