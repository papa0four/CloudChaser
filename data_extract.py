import os
from typing import IO, List, Union, Dict
import json
import socket

PROVIDERS = [ 
    'Alibaba.com Llc', 'Amazon', 'Azure', 'Baidu Inc', 'Digital Ocean', 'Google Cloud', 
    'Kamatera, Inc', 'Linode', 'M247 Ltd', 'M247 Ltd New York Infrastructure',
    'M247 Europe Srl', 'M247 Ltd Rome Network', 'M247 Los Angeles', 'M247',
    'M247 Europe', 'M247 Ltd Paris Infrastructure', 'M247 Ltd Oslo Infrastructure',
    'Oracle', 'Rackspace Hosting', 'Salesforce', 'Tencent Cloud Computing (Beijing) Co. Ltd',
    'Verizon Communications', 'Vultr Holdings LLC'
    ]

data = {}

def is_ipaddr(address: str) -> bool:
    try:
        socket.inet_aton(address)
        return True
    except socket.error:
        return False

def list_files(dir: IO, ext: str) -> IO:
    return (f for f in os.listdir(dir) if f.endswith('.' + ext))

def get_provider(file: IO) -> str:
    provider = ''
    ip_list = []
    with open(file, "r") as file_ptr:
        lines = file_ptr.readlines()
        characters = ['\n', '\t', ' ']
        for line in lines:
            for char in characters:
                if char in line:
                    line = line.replace(char, ',')
            line = list(filter(None, line.split(',')))
            line = ' '.join(line)
            for company in PROVIDERS:
                
    print(data)


# # def extract_data(file: IO) -> Union[Dict, Dict]:
# #     mess = ['\n', '\t', ' ']
# #     provider = ""
# #     ip_ranges = {}
# #     ip_list = []
# #     ip_ranges['ip_ranges'] = []
# #     with open(file, "r") as file_ptr:
# #         line = file_ptr.readlines()
# #         for i in line:
# #             try:
# #                 for junk in mess:
# #                     if junk in i:
# #                         i = i.replace(junk, ',')
# #                 i = i.split(',')
# #                 i = list(filter(None, i))
# #                 i.pop(0)
# #                 provider = ' '.join(i[3:5])
# #                 ips = ' '.join(i[0:3])
# #                 ip_list.append(ips)
# #                 ip_list.sort()
# #                 ip_ranges['ip_ranges'] = ip_list
# #             except (ValueError, IndexError):
# #                 continue
# #     return(provider, ip_ranges)

# # def convert_to_json(file: IO, key: Dict, val: Dict):
# #     data_set = { key: { key: val } }
# #     json_dump = json.dumps(data_set, sort_keys=True, indent=4)
# #     file = file + ".json"
# #     cwd = os.getcwd()
# #     path = cwd + "/" + file
# #     with open(path, "w") as file_ptr:
# #         file_ptr.write(json_dump)

if __name__ == "__main__":
    cwd = os.getcwd()
    files = list_files(cwd, "txt")
    for f in files:
        get_provider(f)