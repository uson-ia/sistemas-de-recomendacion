import numpy as np
import scipy.stats as st
from itertools import ifilter

def shared_items(db, person1, person2):
    return db[person1].viewkeys() & db[person2].viewkeys()

def critics_ratings(db, person1, person2):
    shared = shared_items(db, person1, person2)
    n = len(shared)
    scores1 = np.fromiter(map(lambda x: db[person1][x], shared), np.float_)
    scores2 = np.fromiter(map(lambda x: db[person2][x], shared), np.float_)
    return scores1, scores2, n

def euclidean_similarity(db, person1, person2):
    s1, s2, n = critics_ratings(db, person1, person2)
    return 1/(1+np.linalg.norm(s1-s2))

def pearson_similarity(db, person1, person2):
    s1, s2, n = critics_ratings(db, person1, person2)
    if n == 0: return 0
    return st.pearsonr(s1, s2)[0]

def recommend_critics(db, person, similarity):
    lst = [(similarity(db, person, other), other)
           for other in db if other != person]
    cleaned = ifilter(lambda p: p[0]==p[0], lst)
    return sorted(cleaned)[::-1]

def top_critics(db, person, similarity, n=30):
    return recommend_critics(db, person, similarity)[:n]

def get_recommendations(db, person, similarity=pearson_similarity, n=30, m=30):
    totals = {}
    similarity_sums = {}
    for simil, critic in iter(top_critics(db, person, similarity, n)):
        if simil <= 0: continue
        for movie in db[critic].iterkeys():
            if movie not in db[person]:
                totals.setdefault(movie, 0)
                totals[movie] += db[critic][movie]*simil
                similarity_sums.setdefault(movie, 0)
                similarity_sums[movie] += simil
    rankings = [(total/similarity_sums[movie], movie)
               for movie, total in totals.items()]
    return sorted(rankings)[::-1][:m]