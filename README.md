# superDash

this is a Django project holding the code to my online Dashboard.

## Description

It holds useful links to me, and offers some utils. 
(Utils in this project are small scripts that can crawl to the internet and save usefull info in a structured way)
It's private playground to test the Django framework and help my day to day life.

## Get it working

If you want to try it out you should set up a new database in the settings.py and migrate.
The crawlers for my university won't be working since a script containing my account details is not a part of this project.

## Production

Should you want to deploy this on a server you can simply use `docker-compose up -d` a Dockerfile and a docker-compose.yaml are ready to roll everything out on port 8888
