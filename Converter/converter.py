#! /usr/bin/env python
import argparse
import json
import os
import re
import sys
import yaml
import toml


def json_to_yaml():
    with open(args.file, 'r') as file:
        configuration = json.load(file)

    if (args.print_only == True):
        yaml_text = yaml.dump(configuration)
        print(yaml_text)
    else:
        lastFile = re.search(r'(\w+).',args.file)
        with open(f"{lastFile.group(1)}.yaml", 'w') as yaml_file:
            yaml.dump(configuration, yaml_file)
        with open(args.file, 'r') as yaml_file:
            print(yaml_file.read())


def yaml_to_json():
    with open(args.file, 'r') as file:
        configuration = yaml.safe_load(file)

    if (args.print_only == True):
        json_text = json.dumps(configuration)
        print(json_text)
    else:
        lastFile = re.search(r'(\w+).', args.file)
        with open(f"{lastFile.group(1)}.json", 'w') as json_file:
            output = json.dump(configuration, json_file, indent=2)
            #output = json.dumps(json.load(open(f"{lastFile.group(1)}.json")), indent=2)
            print(output)

        # with open(args.file, 'w') as json_file:
        #     json.dump(configuration, json_file)
        #     output = json.dumps(json.load(open('config.json')), indent=2)
        # print(output)

def json_to_toml():
    with open(args.file, 'r') as file:
        configuration = toml.load(file)

    if (args.print_only == True):
        toml_text = toml.dump(configuration)
        print(toml_text)
    else:
        lastFile = re.search(r'(\w+).',args.file)
        with open(f"{lastFile.group(1)}.toml", 'w') as toml_file:
            toml.dump(configuration, toml_file)
        with open(args.file, 'r') as toml_file:
            print(toml_file.read())

def toml_to_json():
    with open(args.file, 'r') as file:
        configuration = toml.safe_load(file)

    if (args.print_only == True):
        json_text = json.dumps(configuration)
        print(json_text)
    else:
        lastFile = re.search(r'(\w+).', args.file)
        with open(f"{lastFile.group(1)}.toml", 'w') as json_file:
            output = json.dump(configuration, json_file, indent=2)
            #output = json.dumps(json.load(open(f"{lastFile.group(1)}.json")), indent=2)
            print(output)

def yaml_to_toml():
    with open(args.file, 'r') as file:
        configuration = yaml.safe_load(file)

    if (args.print_only == True):
        toml_text = json.dumps(configuration)
        print(toml_text)
    else:
        lastFile = re.search(r'(\w+).', args.file)
        with open(f"{lastFile.group(1)}.toml", 'w') as toml_text:
            output = json.dump(configuration, toml_text, indent=2)
            #output = json.dumps(json.load(open(f"{lastFile.group(1)}.json")), indent=2)
            print(output)

def toml_to_yaml():
    with open(args.file, 'r') as file:
        configuration = toml.safe_load(file)

    if (args.print_only == True):
        yaml_text= json.dumps(configuration)
        print(yaml_text)
    else:
        lastFile = re.search(r'(\w+).', args.file)
        with open(f"{lastFile.group(1)}.yaml", 'w') as yaml_text:
            output = json.dump(configuration, yaml_text, indent=2)
            #output = json.dumps(json.load(open(f"{lastFile.group(1)}.json")), indent=2)
            print(output)

def selectFunction():
    matched = re.search(r'\.(\w+)', args.file)
    if ((matched.group(1) == 'yaml') and (args.out == 'json')):
        yaml_to_json()
    elif ((matched.group(1) == 'json') and (args.out == 'yaml')):
        json_to_yaml()
    elif ((matched.group(1) == 'json') and (args.out == 'toml')):
        json_to_toml()
    elif ((matched.group(1) == 'toml') and (args.out == 'json')):
        toml_to_json()
    elif ((matched.group(1) == 'yaml') and (args.out == 'toml')):
        yaml_to_toml()
    elif ((matched.group(1) == 'toml') and (args.out == 'yaml')):
        toml_to_yaml()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Converts between json, yaml, and toml file formats")
    parser.add_argument(
        "file",
        type=str,
        metavar="file",
        help="input file")
    parser.add_argument(
        "--out",
        type=str,
        choices=["json", "yaml", "toml"],

        help="the output file format"
    )
    parser.add_argument(
        "--in",
        type=str,
        choices=["json", "yaml", "toml"],
        dest="in",
        help="input file format. If not provided, the script tries to auto detect format from filename"
    )
    parser.add_argument(
        "--output-file", "-o",

        metavar="OUTPUT_FILE",
        help="the output filename. If not provided, the output file will have the same name as the input file",
        type=str
    )
    parser.add_argument(
        "--print-only", "-p",

        help="print converted file contents to console instead of writing to output file",
        action="store_true"
    )
    args = parser.parse_args()

    selectFunction()
