import requests
import json
import sys

#request to get similar movies
def get_movies_from_tastedive(movie):
    url_data = 'https://tastedive.com/api/similar'
    params_dict = {}
    params_dict['q'] = movie

    params_dict['type'] = 'movies'
    params_dict['k'] = 'your key'
    params_dict['limit'] = 5

    taste_resp = requests.get(url_data, params = params_dict)
    print(taste_resp.url)
    taste_data = json.loads(taste_resp.text)
    
    return taste_data


#movie
movie_input = input("Enter the movie: ")
movie_data = get_movies_from_tastedive(movie_input)


#making a list of the movies
def extract_movie_titles(movie):
    
    movie_titles = []
    try:
        for c in range(0,5):
            movie_titles.append(movie['Similar']['Results'][c]['Name'])
    
    except:
        print("Movie not found! Please make sure that you enter correctly.")
        return sys.exit()
       
    return movie_titles      

#list of movies
movie_list = extract_movie_titles(movie_data)

#getting the data of the movies
rating_list = []
key = "your key"
c = 0
for r in movie_list:
    url_data = f"http://www.omdbapi.com/?apikey={key}&"
    params_dict = {}
    params_dict['t'] = r
    params_dict['r'] = 'json'
    taste_resp = requests.get(url_data, params=params_dict)
    taste_data = json.loads(taste_resp.text)
    rating = taste_data['imdbRating']
    rating_list.append(movie_list[c] + " - Rating: " + rating)
    c+=1
     

for x in rating_list:
    print(x)




