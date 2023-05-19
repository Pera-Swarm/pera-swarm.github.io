# pip install pyyaml requests

import yaml
import os
import requests 
import json 

def get_projects():
    dir_path = "../projects/pages"
    return os.listdir(dir_path)

def read_frontmatter(path):
    with open(path, "r") as file:
        data = file.read()
    
    structure = data.split("---")
    return yaml.safe_load(structure[1])

project_index = list(map(lambda x: "../projects/pages/"+x ,get_projects()))

team = {}
supervisors = {}
projects = []

for p in project_index:
    d = read_frontmatter(p)
    print('\n>> ', d['title'], )

    api_url = d['api_url']

    if api_url != "#":
        response = requests.get(api_url + "index.json")

        if response.status_code == 200:
            data = json.loads(response.text)
            proj_team = data['team']
            proj_supervisors = data['supervisors']

            print('\t', 'Team:', len(proj_team), ' Supervisors:', len(proj_supervisors))

            # Merge the team details with teams dictionary 
            team.update({k: v for k, v in proj_team.items() if k not in team})
            supervisors.update({k: v for k, v in proj_supervisors.items() if k not in supervisors})
            projects.append(data)
        else:
            print("\t Invalid project API URL: {0}".format(api_url))

# Sort details 
team_sorted = {k: v for k, v in sorted(team.items())}
supervisors_sorted = {k: v for k, v in sorted(supervisors.items(), key=lambda kv: supervisors[kv[0]]['name'])}

# Write the details 
filename = "../_data/team.json"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, 'w') as f:
    f.write(json.dumps(team_sorted, indent = 4))

filename = "../_data/supervisors.json"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, 'w') as f:
    f.write(json.dumps(supervisors_sorted, indent = 4))

filename = "../_data/projects.json"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, 'w') as f:
    f.write(json.dumps(projects, indent = 4))