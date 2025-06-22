from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_reward(query, result):
    emb_query = model.encode(query, convert_to_tensor=True)
    emb_result = model.encode(result, convert_to_tensor=True)
    score = util.pytorch_cos_sim(emb_query, emb_result).item()
    return score