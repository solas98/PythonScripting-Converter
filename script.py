#! /usr/bin/env python
import argparse
import json
import os
import re
import sys
# import pyyaml


def json_to_yaml():
        with open(args.file, 'r') as file:
                configuration = json.load(file)

        with open('config.yaml', 'w') as yaml_file:
                 yaml.dump(configuration, yaml_file)

        with open('config.yaml', 'r') as yaml_file:
                print(yaml_file.read())

def yaml_to_json():
        with open(args.file, 'r') as file:
         configuration = yaml.safe_load(file)

        with open('config.json', 'w') as json_file:
         json.dump(configuration, json_file)
    
        output = json.dumps(json.load(open('config.json')), indent=2)
        print(output)



        

if __name__ == '__main__':
        

        parser = argparse.ArgumentParser(description="Converts between json, yaml, and toml file formats")
        parser.add_argument(
        "file",
        type=str,
        metavar="file",
        help="input file" )
        parser.add_argument(
            "--out",
            type=str,
            choices=["json", "yaml","toml"],
            dest="out",
            help="the output file format"
            )
        parser.add_argument(
            "--in",
            type=str,
            choices=["json", "yaml","toml"],
            dest="in",
            help="input file format. If not provided, the script tries to auto detect format from filename"
            )
        parser.add_argument(
            "--output-file", "-o",
            type=str,
            dest="output-file",
            metavar="OUTPUT_FILE",
            help="the output filename. If not provided, the output file will have the same name as the input file"
            )
        parser.add_argument(
            "--print-only", "-p",
            type=str,
            dest="print-only",
            metavar='',
            help="print converted file contents to console instead of writing to output file"
            )    
        args = parser.parse_args()

        yaml_to_json()