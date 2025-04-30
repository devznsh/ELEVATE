from transformers import BertTokenizer, BertModel
import torch
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class BERTRecommender:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')
    
    def get_embedding(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.last_hidden_state.mean(dim=1)
    
    def recommend(self, user_input, careers_df, top_n=5):
        career_texts = careers_df['profession'] + " " + careers_df['keywords']
        user_embedding = self.get_embedding(user_input)
        career_embeddings = torch.stack([self.get_embedding(text) for text in career_texts])
        
        similarities = cosine_similarity(
            user_embedding,
            career_embeddings.squeeze(1)
        )[0]
        
        top_indices = np.argsort(similarities)[-top_n:][::-1]
        return careers_df.iloc[top_indices]

def get_recommendations(user_input, careers_df):
    recommender = BERTRecommender()
    return recommender.recommend(user_input, careers_df)