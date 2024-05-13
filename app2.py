import pickle
import streamlit as st


def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1]
    )
    recommended_movie_names = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names


st.header("Movie Recommender System")

# load the dataset
movies = pickle.load(
    open("D:\my_projects\movie-recommendation-system\model\movies.pkl", "rb")
)

# load the similarity
similarity = pickle.load(
    open(
        "D:\my_projects\movie-recommendation-system\model\similaritys.pkl",
        "rb",
    )
)

movie_list = movies["title"].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button("Show Recommendation"):
    recommended_movie_names = recommend(selected_movie)
    st.text(recommended_movie_names[0])
    st.text(recommended_movie_names[1])
    st.text(recommended_movie_names[2])
    st.text(recommended_movie_names[3])
    st.text(recommended_movie_names[4])
