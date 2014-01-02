from bs4 import BeautifulSoup
from json import dumps, loads, load
from time import sleep
import requests, os

existing = 'videos.json'

def main():
    loaded = open(existing, 'r')
    urls = load(loaded) or {}
    old_len = len(urls.keys())
    print "Loaded {} existing videos.".format(len(urls.keys()))
    loaded.close()

    output_file = open(existing, 'w')
    intermediate_output_file = open('/tmp/intermediate_{}'.format(existing), 'w')

    for i in range(1,60):
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

            try:
                split_time = video_time.split(":")

                if len(split_time) >= 3 and int(split_time[0]) >= 9:
                    urls[title] = { 'id': video_id, 'time': video_time }
            except IndexError:
                print "Weird split."
                continue
            except AttributeError:
                print "List split?"
                continue

        intermediate_output_file.write(dumps(urls))
        print "Retrieved page {}. Sleeping.".format(i)
        sleep(2)

    output_file.write(dumps(urls))
    intermediate_output_file.close()
    os.remove(intermediate_output_file)
    output_file.close()
    diff = len(urls.keys()) - old_len
    print "Added {} new videos.".format(diff)

if __name__ == '__main__':
    main()
