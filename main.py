# python_debian_project - Stephen Dawson
# Start Time: 1:00 PM April 02 2021 
# End Time: 10:00 PM April 02 2021
# See end of document for notes on process and imagined next steps.

import sys
import requests
import gzip
from collections import Counter

#Function to download and extract Debian Contents
def content_download(url, dest):
    r = requests.get(url)
    with open(dest, 'wb') as outfile:
        outfile.write(gzip.decompress(r.content))

#Function for separate the packages from the content file. 
def extract_packages(dest):
    packages = []
    with open(dest) as fp:
        for line in fp:
            #Take second column, put comma separated info on new lines, separate lines
            line = line.split()[1].replace(",", "\n").splitlines()
            for item in line:
                #separate package from section
                try:
                    item = item.split("/")[1]
                #factor in potential for unclean splits due to white space, etc. 
                except:
                    continue
                packages.append(item)
    return packages

#Function to extract most common packages and return # of instances which equates to file number. 
def count_packages(packages):
    count = Counter(packages)
    return count.most_common(10)

#Function to print results.
def print_packages(packages):
    print('The most popular packages are:')
    for count, item in enumerate(packages):
        print(f'{count + 1}: {item[0]}: {item[1]} Files')

def main():
    #Usage: python main.py arch is_micro(y/n) e.g. python main.py amd64 n
    #Architecture
    arch = sys.argv[1]
    #Micro or Standard size check
    is_micro = sys.argv[2]
    #base url
    url = "http://ftp.uk.debian.org/debian/dists/stable/main/Contents-"

    #Define whether downloading micro, or full sized contents. 
    if is_micro == "y":
        url = url + "udeb-" + arch + ".gz"
        filename = "Contents-udeb-" + arch
    else:
        url = url + arch + ".gz"
        filename = "Contents-" + arch
        
    #Destination for content data
    dest = 'content_files/' + filename + ".txt"

    content_download(url, dest)
    packages = extract_packages(dest)
    common_packages = count_packages(packages)
    print_packages(common_packages)

if __name__ == '__main__':
    main()

"""
Prototype Process:
 - Brute Force Solution
 - Attempt to verify correctness with manual testing and content reference.

Next Steps:
 - Refactor 
    - move out most code from main.py into modules
    - add error checking
    - implement better command line feedback and help
 - Implement Unit and Integration testing
 - Time code and optimize for time complexity
"""
