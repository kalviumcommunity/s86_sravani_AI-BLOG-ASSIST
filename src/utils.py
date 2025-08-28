# src/utils.py
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def compute_cosine_similarity(vec1, vec2):
    """
    Compute cosine similarity between two vectors (numpy arrays)
    """
    vec1 = vec1.reshape(1, -1)
    vec2 = vec2.reshape(1, -1)
    return cosine_similarity(vec1, vec2)[0][0]


def find_most_similar_topic(user_embedding, topic_embeddings, topic_list):
    """
    Given user embedding, returns the topic with highest cosine similarity
    """
    best_score = -1
    best_topic = None
    for idx, emb in enumerate(topic_embeddings):
        score = compute_cosine_similarity(user_embedding, emb)
        if score > best_score:
            best_score = score
            best_topic = topic_list[idx]
    return best_topic, best_score
