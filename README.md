# Top Cancelled

## General Info
This website features three main pages: Home, Random, and About Us.

### Home:
The home tab features the most cancelled people on Twitter at any given time and what % cancelled (screwed) they are. You can navigate to each user's twitter profile by clicking their handles, and enjoy a sneak peek of their profile pic in a retro grid format. 

### Random:
The random page features totally random tweets, which we hope are as fun for you to pore over as they were for us. 

## Installation
Check out the requirements in the requirements.txt file, and make sure to use SpaCy and nltk to download the required tools.

## Technologies
Frontend:
- Bootstrap 5.3
- Flask 2.2

Backend:
- Python 3.10
- nltk - VADER
- SpaCy
- SQLite
- Twitter Developer API
- Web Scraping/Selenium
- crontab

Basically, this program uses a Twitter API and webscraping using Selenium to determine the most cancelled users at any given time! Data is stored using SQLite and sentiment analysis is performed on trending tweets to determine which users are most cancelled. Using SpaCy's Named Entity Recognition capabilities, we also made sure to weed out only people who are being cancelled using, as opposed to companies, etc. This data is then passed along to the frontend, which relies mainly on Flask. The frontend is also written with HTML, CSS, and the Bootstrap framework. We used crontab to update the database in the background.

Running on http://pod2-3.cs.purdue.edu:5000/random and 0 hours of sleep.
