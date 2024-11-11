import pickle
from scripts.collaborative_personalized import recommend_collaborative_personalized
from scripts.content_based import recommend_content_based



def get_hybrid_recommendations(user_id, movie, outputs):
    
    content_based = recommend_content_based(movie,outputs) 
    collaborative_based = recommend_collaborative_personalized(user_id,outputs) 
    
    unique_movies = {}
    
    
    for item in content_based:
        unique_movies[item['title']] = item 
    
    # Add collaborative-based recommendations to the dictionary
    for item in collaborative_based:
        unique_movies[item['title']] = item 
    
    # Convert the dictionary values to a list
    hybrid_recommendations = list(unique_movies.values())
    
    
    return hybrid_recommendations[:outputs]