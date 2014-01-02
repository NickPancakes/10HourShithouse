#!/bin/bash -e

rsync -Pavz update.sh scrape/smash_n_grab.py videos.json index.html js shithouse.tv:/var/www/shithouse/10Hours/
