#!/bin/bash -e

rsync -Pavz videos.json index.html js shithouse.tv:/var/www/shithouse/10Hours/
