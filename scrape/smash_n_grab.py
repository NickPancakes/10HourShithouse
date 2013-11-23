from bs4 import BeautifulSoup
from json import dumps
from time import sleep
import requests

output = 'raw_scraped.json'

def main():
    output_file = open(output, 'w')
    urls = []
    for i in range(1,2):
        r = requests.get('http://www.youtube.com/results?q=10+hours&page={}'.format(i))
        soup = BeautifulSoup(r.text)
        import ipdb; ipdb.set_trace()
        sleep(10)

    output_file.write(dumps(set(urls)))
    output_file.close()

if __name__ == '__main__':
    main()
