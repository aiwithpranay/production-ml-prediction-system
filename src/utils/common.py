import yaml

def read_yaml(path):

    with open(path) as yaml_file:

        return yaml.safe_load(yaml_file)