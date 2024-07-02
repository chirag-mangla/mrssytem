import pickle
import pandas as pd
import streamlit as st

movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
st.title("Movie Recommender System")
option = st.selectbox('How would you like to be contacted?', movies['title'].values)

similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances =similarity[index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda  x:x[1])[1:6]
    recommended_movie = []
    recommended_movie_posters = []
    for i in movies_list:
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie

if st.button('Show Recommendation'):
    recommendation=recommend(option)
    for i in recommendation:
        st.write(i)
