# omdb-api

Small program in Pyton that queries this publicly available API to get Rotten Tomatoes rating for a specific movie:
http://www.omdbapi.com/

Part 1 – Dockerfile
Builds a docker image that will contain the script
- It's based on Alpine Linux
- The script is in Python language
- To build the image:

> docker build -t omdb-api .

- To run the container (example):

> docker run -e "MOVIE='Star Wars'" omdb-api:latest

Part 2 - Python script
- To run the script (example):

> python src/do_get_rating.py "Star Wars"

> python src/do_get_rating.py -h
