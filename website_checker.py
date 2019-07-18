import requests
import argparse

def url_status_code(url):
    try:
        r = requests.get(url)
        return str(r.status_code)
    except:
        return "Failed to establish a new connection"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url',
                         help='url to check status of',
                         required= True,
                         type= str)
    args = parser.parse_args()
    print(url_status_code(args.url))
