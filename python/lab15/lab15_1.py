#
#

import urllib

def main():
    r = requests.get('http://www.ulster.ac.uk')

    print(r.status_code)
