import os

import yaml


def list_project_config():
    configs = []

    for root, dirs, files in os.walk("data/projects"):
        for file in files:
            if file == 'template.yml':
                continue
            if file.endswith(".yml"):
                configs.append(os.path.join(root, file))

    return configs


for config in list_project_config():
    with open(config, 'r') as c:
        project = yaml.safe_load(c)
        print(project['name'])
        print(project['priority'])
        print(project['tasks'][0])
