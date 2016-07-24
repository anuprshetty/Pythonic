import requests


def readFile(filename):
    with open(filename) as f:
        lines = f.readlines()
    urls = []
    for line in lines:
        urls.append(line.strip(' \t\n'))
    while '' in urls:
        urls.remove('')
    return urls


def urlsStatusChecker(urls):
    for url in urls:
        try:
            url_response = requests.get(url, verify=False)
            if url_response.status_code == 200:
                print('{} - OK'.format(url))
        except requests.exceptions.ConnectionError:
            print('{} - NOT OK'.format(url))     


if __name__ == '__main__':
    filename = 'URLs.txt'
    urls = readFile(filename)
    urlsStatusChecker(urls)
