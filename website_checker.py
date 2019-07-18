import requests

def url_status_code(url):
    try:
        r = requests.get(url)
        return str(r.status_code)
    except:
        return "Failed to establish a new connection"