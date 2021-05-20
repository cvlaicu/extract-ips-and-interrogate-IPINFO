import ipinfo
import csv


def get_ip_list(doc):
    ip_list = []

    for row in doc:
        ip_list.append(row[0])
    return ip_list


def get_ipinfo_data(ips_list, token):
    # this list will store the dictionary for each IP
    ip_info = []
    # this list will store all IPs for which IPinfo does not provide any onfo
    no_info = []

    acc_token = token
    handler = ipinfo.getHandler(token)
    print("[+] Pulling data...")

    for ip in ips_list:
        ip_dictionary = {}

        try:
            details = handler.getDetails(str(ip))
            ip_dictionary['ip'] = ip
            ip_dictionary['hostname'] = details.hostname
            ip_dictionary['city'] = details.city
            ip_dictionary['region'] = details.region
            ip_dictionary['country'] = details.country
            ip_dictionary['location'] = details.loc
            ip_dictionary['organization'] = details.org
            ip_dictionary['postal'] = details.postal
            ip_dictionary['timezone'] = details.timezone
            ip_info.append(ip_dictionary)

        except AttributeError:
            no_info.append(ip)

    print("\n[+] Done!")

    return ip_info, no_info


def generate_csv(raw_ip_list, no_info):

    with open('ip_info.csv', 'w', newline='') as file:

        write = csv.writer(file)
        file_header = ['IP', 'Hostname', 'City', 'Region', 'Country', 'Location', 'Organization', 'Postal', 'Timezone']
        # here I am writing the header of the file
        write.writerow(file_header)

        # here I attribute to the values variable the dictionary values
        for dictionary in raw_ip_list:
            values = [dictionary['ip'], dictionary['hostname'], dictionary['city'], dictionary['region']
                      , dictionary['country'], dictionary['location'], dictionary['organization']
                      , dictionary['postal'], dictionary['timezone']]
            # here I am writing the values to the CSV file
            write.writerow(values)

        for ip in no_info:
            no_value_list = [ip, 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a']
            write.writerow(no_value_list)


def main(access_token):
    with open("ips.csv", 'r') as file:
        reader = csv.reader(file)

        ips = get_ip_list(reader)
        ip_info_list = get_ipinfo_data(ips, access_token)
        # get_ipinfo_data returns two lists: one list for which IPinfo found values, and another for which IPinfo
        # did not find any info. I am calling the two below, where [0] is the one with info and [1] is the one
        # with no info
        generate_csv(ip_info_list[0], ip_info_list[1])

