import json
import requests
import sys
import argparse

parser = argparse.ArgumentParser(description='Script that gets Rotten Tomatoes rating of a movie.')
parser.add_argument('movie', nargs='*', default='Star Wars', help='Movie to review, example \'Star Wars\'')
args = parser.parse_args()

api_key = 'be3f7f2f'
api_url_base = 'http://www.omdbapi.com/?'

if len(sys.argv) < 2:
  print('ERROR: Please pass a movie title as argument')
  exit()
else:
  movie = sys.argv[1]

def get_rating_from_api():
  api_url = '{0}apikey={1}&t={2}'.format(api_url_base,api_key,movie)

  response = requests.get(api_url)

  if response.status_code == 200:
    return json.loads(response.content.decode('utf-8'))
  else:
    return None

movie_data = get_rating_from_api()

if movie_data is not None:
  ratings = movie_data['Ratings']

  print("Rotten Tomatoes Rating for Movie '{0}': ".format(movie))

  for i in range(len(ratings)):
    if ratings[i]['Source'] == 'Rotten Tomatoes':
      print('{0}'.format(ratings[i]['Value']))

else:
  print('ERROR: Request Failed!')
