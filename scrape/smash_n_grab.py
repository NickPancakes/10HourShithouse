from bs4 import BeautifulSoup
from json import dumps
from time import sleep
import requests

output = 'raw_scraped.json'

def main():
    output_file = open(output, 'w')
    intermediate_output_file = open('intermediate_{}'.format(output), 'a')
    urls = {}
    for i in range(1,40):
        print "Grabbing page {}.".format(i)
        r = requests.get('http://www.youtube.com/results?search_query="10+hours"&page={}'.format(i))
        soup = BeautifulSoup(r.text)
        hrefs = soup.select('#search-results h3.yt-lockup-title a.yt-uix-sessionlink')

        for a in hrefs:
            title = a.attrs.get('title', 'Unknown Title')
            raw = a.attrs['href']
            video_id = raw.split('=')[1] if 'watch' in raw else None

            video_time = soup.select("a[href=\"{}\"] span.video-time".format(raw))
            if len(video_time) >= 1:
                video_time = video_time[0].text

            urls[title] = { 'id': video_id, 'time': video_time }

        intermediate_output_file.write(dumps(urls))
        print "Retrieved page {}. Sleeping.".format(i)
        sleep(5)

    output_file.write(dumps(urls))
    intermediate_output_file.close()
    output_file.close()

if __name__ == '__main__':
    main()
