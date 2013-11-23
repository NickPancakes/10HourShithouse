from bs4 import BeautifulSoup
from json import dumps
from time import sleep
import requests

output = 'raw_scraped.json'

def main():
    output_file = open(output, 'w')
    intermediate_output_file = open('intermediate_{}'.format(output), 'a')
    urls = []
    for i in range(1,35):
        print "Grabbing page {}.".format(i)
        r = requests.get('http://www.youtube.com/results?q=10+hours&page={}'.format(i))
        soup = BeautifulSoup(r.text)
        hrefs = soup.select('#search-results h3.yt-lockup-title a.yt-uix-sessionlink')
        hrefs = [test.attrs['href'] for test in hrefs]
        ids = [raw.split('=')[1] for raw in hrefs if 'watch' in raw]

        map(urls.append, ids)
        intermediate_output_file.write(dumps(list(set(urls))))
        print "Retrieved page {}. Sleeping.".format(i)
        sleep(5)

    output_file.write(dumps(list(set(urls))))
    intermediate_output_file.close()
    output_file.close()

if __name__ == '__main__':
    main()
