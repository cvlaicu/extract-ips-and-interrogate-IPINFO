import csvparse
import apicall
import os
import glob


def get_files_directory():
    # this function checks current working directory and then creates a path to all file extensions to the \FILES\
    # directory
    main_program_directory = os.getcwd()
    csv_files = glob.glob(main_program_directory + r"\FILES\*.csv")

    return csv_files


def check_files_existence():
    # here I am returning all CSV files from \FILES\ directory and running the parsers if any files found

    print("[+] Checking for CSV files...")
    csv_files_list = get_files_directory()

    if not csv_files_list:
        print("[-] No CSV files found! Checking next extension...")
    else:
        print("[+] CSV files found! Extracting info...")
    csvparse.main(csv_files_list)  # HERE I AM CALLING THE CSVPARSER


if __name__ == '__main__':

    access_token = "XXXXXXXXXXXXXXX" # REPLACE THE TOKEN WITH THE ONE YOU RECEIVE WHEN REGISTERING TO IPINFO
    check_files_existence()
    print("\n[+] Information extraction from files finished, proceeding with pulling data from IPinfo...")
    apicall.main(access_token)
