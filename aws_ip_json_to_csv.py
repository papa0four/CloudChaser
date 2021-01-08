"""
Data structure:
{
    "ip_range": "10.10.10.10/28",
    "provider": "MegaCloud",
    "region": "us-east-1",
    "country": "US",
    "city": "Atlanta",
}
"""

import json
import csv
import sys

HEADER = ["ip_range", "provider", "region", "country", "city"]


def process_aws(in_f, out_f):
    aws_regions = {
        "us-east-1": ["US", "Virginia"],
        "us-east-2": ["US", "Ohio"],
        "us-west-1": ["US", "California"],
        "us-west-2": ["US", "Oregon"],
        "af-south-1": ["SA", "Cape Town"],
        "ap-east-1": ["HK", "Hong Kong"],
        "ap-south-1": ["IN", "Mumbai"],
        "ap-south-2": ["IN", "Hyderabad"],
        "ap-northeast-3": ["JP", "Osaka"],
        "ap-northeast-2": ["KR", "Seoul"],
        "ap-southeast-1": ["SG", "Singapore"],
        "ap-southeast-2": ["AU", "Sydney"],
        "ap-southeast-3": ["ID", "Jakarta"],
        "ap-northeast-1": ["JP", "Tokyo"],
        "ca-central-1": ["CA", ""],
        "eu-central-1": ["DE", "Frankfurt"],
        "eu-west-1": ["IR", ""],
        "eu-west-2": ["GB", "London"],
        "eu-south-1": ["IT", "Milan"],
        "eu-west-3": ["FR", "Paris"],
        "eu-north-1": ["SE", "Stockholm"],
        "me-south-1": ["BH", ""],
        "me-central-1": ["", ""],  # This doesn't exist on the Internet... Iran?
        "sa-east-1": ["BR", "Sao Paulo"],
        "cn-northwest-1": ["CN", "Ningxia"],
        "cn-north-1": ["CN", "Beijing"],
        "us-gov-east-1": ["US", "GovCloud"],
        "us-gov-west-1": ["US", "GovCloud"],
        "GLOBAL": ["", "Global"],
    }
    with open(in_f) as f:
        data = json.load(f)
    csv_writer = csv.writer(out_f)
    prefixes = data["prefixes"]
    for prefix in prefixes:
        csv_writer.writerow(
            [
                prefix["ip_range"],
                "AWS",
                prefix["region"],
                aws_regions[prefix["region"]][0],
                aws_regions[prefix["region"]][1],
            ]
        )


def process_linode(in_f, out_f):
    with open(in_f) as f:
        csv_reader = csv.reader(f)
        csv_writer = csv.writer(out_f)
        for row in csv_reader:
            csv_writer.writerow([row[0], "Linode", row[2], row[1], row[3]])


def process_azure(in_f, out_f):
    with open(in_f) as f:
        data = json.load(f)
    csv_writer = csv.writer(out_f)
    values = data["values"]
    for value in values:
        props = value["properties"]
        region = props["region"]
        for addr in props["addressPrefixes"]:
            csv_writer.writerow([addr, "Azure", region, "", ""])


def process_gcp(in_f, out_f):
    with open(in_f) as f:
        data = json.load(f)
    csv_writer = csv.writer(out_f)
    prefixes = data["prefixes"]
    for prefix in prefixes:
        csv_writer.writerow(
            [
                prefix["ip_range"],
                "Google Cloud",
                prefix["region"],
                "",
                "",
            ]
        )


def process_oracle(in_f, out_f):
    with open(in_f) as f:
        data = json.load(f)
    csv_writer = csv.writer(out_f)
    regions = data["regions"]
    for r in regions:
        region = r["region"]
        for cidr in r["cidrs"]:
            csv_writer.writerow([cidr["cidr"], "Oracle", region, "", ""])


def process_digitalocean(in_f, out_f):
    with open(in_f) as f:
        csv_reader = csv.reader(f)
        csv_writer = csv.writer(out_f)
        for row in csv_reader:
            try:
                csv_writer.writerow([row[0], "DigitalOcean", row[2], row[1], row[3]])
            except:
                print(row)


if __name__ == "__main__":
    output_file = open("ip_ranges.csv", "w")
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(HEADER)
    process_aws("aws_ips.json", output_file)
    process_linode("linode_ips.csv", output_file)
    process_azure("azure_ips.json", output_file)
    process_gcp("gcp_ips.json", output_file)
    process_oracle("oracle_ips.json", output_file)
    process_digitalocean("digitalocean.csv", output_file)
