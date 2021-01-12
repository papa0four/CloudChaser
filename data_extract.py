import os
from typing import IO, List, Union
import json

def list_files(dir: IO, ext: str) -> IO:
    return (f for f in os.listdir(dir) if f.endswith('.' + ext))

def extract_data(file: IO) -> Union[str, str]:
    mess = ['\n', '\t', ' ']
    provider = ''
    ranges = []
    with open(file, "r") as file_ptr:
        line = file_ptr.readlines()
        for i in line:
            for junk in mess:
                if junk in i:
                    i = i.replace(junk, ',')
            i = i.split(',')
            i = list(filter(None, i))
            i.pop(0)
            provider = ' '.join(i[3:5])
            ips = ' '.join(i[0:3])
            ranges.append(ips)
    ranges.sort()
    return(provider, ranges)

def convert_to_json(file: IO, key: str, val: List):
    data_set = { key: val }
    json_dump = json.dumps(data_set)
    file = file + ".json"
    cwd = os.getcwd()
    path = cwd + "/" + file
    with open(path, "w") as file_ptr:
        file_ptr.write(json_dump)

if __name__ == "__main__":
    cwd = os.getcwd()
    files = list_files(cwd, "txt")
    for f in files:
        key, val = extract_data(f)
        f = f[:-4]
        print(f)
        convert_to_json(f, key, val)