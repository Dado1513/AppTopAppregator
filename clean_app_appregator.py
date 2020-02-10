import os
import sys
import json


def main():
    if len(sys.argv) == 2:
        name_file = sys.argv[1]
        with open(name_file) as json_file:
            data = json.load(json_file)
        with open("apps.txt","w") as w:
            for x in data:
                w.write("{}\n".format(x))

if __name__ == "__main__":
    main()