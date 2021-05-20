import csv
import re


def eliminate_duplicates(ip_list):
    # this function eliminates IP duplicates
    return list(dict.fromkeys(ip_list))


def ip_sanitization(raw_ip):
    # this function is needed to sanitize IPs that have the format 192[.]49[.]33[.]12
    raw_ip = raw_ip.split("[.]")
    separator = '.'
    return separator.join(raw_ip)


def export_to_file(ip_list):
    # this function exports the data to "ips.csv" file
    with open("ips.csv", "a", newline='') as f:
        writer = csv.writer(f)
        for element in ip_list:
            writer.writerow([element])


def manipulate_document(csv_file):
    # this function performs the data manipulation of the CSV file
    ips = []

    # here I am reading each row from the CSV file.
    for row in csv_file:
        for element in row:

            b = re.findall(r"(?:\s|\A)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?=\s|\Z)", element)
            c = re.findall(r"(?:\s|\A)(\d{1,3}\[.]\d{1,3}\[.]\d{1,3}\[.]\d{1,3})(?=\s|\Z)", element)

            if not b:
                pass
            else:
                ips.extend(b)

            if not c:
                pass
            else:
                # Because REGEX returns a list with only one element, I need to take the element out of the list
                # so I attribute it to c (ip_sanitization does not support lists)
                c = c[0]
                c = ip_sanitization(c)
                ips.append(c)

    ips_list = eliminate_duplicates(ips)
    export_to_file(ips_list)


def main(files_list):
    for each_file in files_list:
        with open(each_file, 'r') as file:
            data = csv.reader(file)
            manipulate_document(data)
    print("[+] CSV information extraction done.")

