#importing all libraries
import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests
#function to fetch poster of movie from the given movie_id
def fetchposter(movie_id):
    #uses API of TMDB after customising it with my own API key which I had generated
    responses = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=5f1c46fced5dd617378a868f449033d9&language=en-US')
    data = responses.json()               #converts it from jsoon format which it recieves the data
    #find image path from the net of tmdb
    return 'https://image.tmdb.org/t/p/w500' + data['poster_path']

#function to recommend movies
def recommend(movie,n=5):
    ind = newdf[newdf['title']==movie].index[0]         #will give the index of the inputed movie
# will first sort the similarity[ind] array in descending order and then give the indexes as list
    v = list(np.argsort(similarity[ind])[::-1][0:51])
#will sort the similarity[ind] array in descending order and then give the values as list
    c = list(np.sort(similarity[ind])[::-1][0:51])
#will create a dictionary matching the indexes with the corresponding values
    di = dict(zip(v,c))
#creates a dataframe M
    M = pd.DataFrame(list(di.items()), columns=['index', 'similarityvalue'])
    M['release_date'] = newdf.iloc[v,3]        #creates a column in dataframe M called releasedate
#we intend to create a parameter datesimilarity which is reciprocal of difference of each
#movies' release decade and the inputed movie's release decade as this will help us factor in
#which decade the movie was released in, as often many viewers like movies of 90s or some like
#movies of the 2000s, etc.
    def datesimilarity(x):
        if (x-M.iloc[0,2])==0:                 #we are handling 0 values here like this
            return 100
        else:
            return 1/(x-M.iloc[0,2])
    M['release_date'] = M['release_date'].apply(datesimilarity)
    M['netsimilarity'] = M['similarityvalue']**2 + 0.01*(M['release_date']**2)
#we are sorting according to the new parameter netsimilarity
    final = M.sort_values(by='netsimilarity', ascending=False)[1:n+1]
    fin = list(final['index'])
    recommended_movies = []
    recommended_movies_posters = []
    for i in fin:
        recommended_movies.append(newdf.iloc[i].title)
        # fetch poster from api
        recommended_movies_posters.append(fetchposter(newdf.iloc[i,0]))
    return recommended_movies, recommended_movies_posters

newdf = pd.DataFrame(pickle.load(open('movies.pkl', 'rb')))
st.title('Movie Recommender System')
similarity = pickle.load(open('similarity.pkl', 'rb'))
#to create a dropdown box of all movies available in database
selected_movie_name = st.selectbox(
    "Select movie from the given list of movies to be suggested similar movies",
    newdf['title'].values,
)

number = st.number_input("Type number of movies you want to recommend", value=5, min_value=1, max_value=50)
err = 0     #err variable will record the number of times it took to access API before success
if st.button("Recommend"):

    st.write("You selected:", selected_movie_name, 'and ', number, 'movies recommended.')
    while True:                   #will handle the error if server fails to connect to API
        try:                      #this codeblock makes the server reconnect without crashing
            names, posters = recommend(selected_movie_name, number)
            break
        except:
            err+=1
#the following code is the code to create columns of images and names of movies recommended
    col1, col2, col3, col4, col5 = st.columns(5, border= True)
    col1num = [i for i in range(number) if i%5==0]
    col2num = [i for i in range(number) if i%5==1]
    col3num = [i for i in range(number) if i%5==2]
    col4num = [i for i in range(number) if i%5==3]
    col5num = [i for i in range(number) if i%5==4]
    with col1:
        for j in col1num:
            st.write(names[j])
            st.image(posters[j])
    with col2:
        for j in col2num:
            st.write(names[j])
            st.image(posters[j])
    with col3:
        for j in col3num:
            st.write(names[j])
            st.image(posters[j])
    with col4:
        for j in col4num:
            st.write(names[j])
            st.image(posters[j])
    with col5:
        for j in col5num:
            st.write(names[j])
            st.image(posters[j])
    st.write('The server tried to connect ', err, 'times')
