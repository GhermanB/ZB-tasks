from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class SimilarityModel:

    def __init__(self):
        self.model = SentenceTransformer('DeepPavlov/rubert-base-cased-sentence')

    def similarity(self, texts):
        sentences = texts
        sentence_embeddings = self.model.encode(sentences)
        similarity = cosine_similarity(
            [sentence_embeddings[0]],
            sentence_embeddings[1:])
        return similarity.item(0)