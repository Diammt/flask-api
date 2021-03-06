import requests
import argparse
import json


BASE = "http://127.0.0.1:5000/"


def parse_arguments():
    parser = argparse.ArgumentParser()
    # parser.add_argument("-e", "--extension", help="""Type of file to analyse. Is it a CSV or an XML?""")
    parser.add_argument("-t","--test", action="store_true")
  
    return parser.parse_args()

def parse_json(data):
    """
        Converted to indented json for better display
    """
    json_object = json.dumps(data, indent = 4)
    return json_object

def main():
    args = parse_arguments()

    if args.test:
        response = requests.get(BASE)
        #print(parse_json(response.json()))
    

if __name__ == '__main__':
    main()