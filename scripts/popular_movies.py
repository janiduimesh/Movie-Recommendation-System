import pickle
import streamlit as st

# Popular movies
def getTopRatedMovies(n_outputs):
   
    with open('PKL_Files/popular_movies_df', 'rb') as file:
        popular_movies_df = pickle.load(file)

    # Get the top n rated movies
    top_movies = popular_movies_df.head(n_outputs)

    # Streamlit columns to display the movies
    col1, col2, col3 = st.columns(3)
    title_height = "70px"  

    for i, movie in top_movies.iterrows():
        title_div = f"<div style='height: {title_height}; display: flex; align-items: center;'>{movie['title']}</div>"
        if i % 3 == 0:
            with col1:
                st.write(title_div, unsafe_allow_html=True)
                st.image(movie['Poster URL'], width=200)
        elif i % 3 == 1:
            with col2:
                st.write(title_div, unsafe_allow_html=True)
                st.image(movie['Poster URL'], width=200)
        else:
            with col3:
                st.write(title_div, unsafe_allow_html=True)
                st.image(movie['Poster URL'], width=200)
