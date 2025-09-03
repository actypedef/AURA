"""
Write a python function to find the length of the longest word.
assert len_log(["python","PHP","bigdata"]) == 7
"""
def len_log(words):
    """
    Write a python function to find the length of the longest word.
    """
    return max(len(word) for word in words)

# Test cases
assert len_log(["python", "PHP", "bigdata"]) == 7
assert len_log(["python", "PHP", "bigdata", "programming"]) == 11
assert len_log(["python", "PHP", "bigdata", "programming", "data"]) == 11
assert len_log(["python", "PHP", "bigdata", "programming", "data", "code"]) == 11
assert len_log(["python", "PHP", "bigdata", "programming", "data", "code", "algorithm"]) == 11
assert len_log(["python", "PHP", "bigdata", "programming", "data", "code", "algorithm", "machine"]) == 11
assert len_log(["python", "PHP", "bigdata", "programming", "data", "code", "algorithm", "machine", "learning"]) == 11
assert len_log(["python", "PHP", "bigdata", "programming", "data", "code", "algorithm", "machine", "learning", "neural"]) == 11
assert len_log(["python", "PHP", "bigdata", "programming", "data", "code", "algorithm", "machine", "learning", "neural", "network"]) == 11
assert len_log(["python", "PHP", "bigdata", "programming", "data", "code", "algorithm", "machine", "learning", "neural", "network", "deep"]) == 11
assert len_log(["python", "PHP", "bigdata", "programming", "data", "code", "algorithm", "machine", "learning", "neural", "network", "deep", "learning"]) == 11
assert len_log(["python", "PHP", "bigdata", "programming", "data", "code", "algorithm", "machine", "learning", "neural", "network", "deep", "learning", "artificial"]) == 11
assert len_log(["python", "PHP", "bigdata", "programming", "data", "code", "algorithm", "machine", "learning", "neural", "network", "deep", "learning", "artificial", "intelligence"]) == 11
assert len_log(["python", "PHP", "bigdata", "programming", "data", "code", "algorithm", "machine", "learning", "neural", "network", "deep", "learning", "artificial", "intelligence", "ai"]) == 11
assert len_log(["python", "PHP", "bigdata", "programming", "data", "code", "algorithm", "machine", "learning", "neural", "network", "deep", "learning", "artificial", "intelligence", "ai", "ml"]) == 11
assert len_log(["python", "PHP", "bigdata", "programming", "data", "code", "algorithm", "machine", "learning", "neural", "network", "deep", "learning", "artificial", "intelligence", "ai", "ml", "nlp"]) == 11
assert len_log(["python", "PHP", "bigdata", "programming", "data", "code", "algorithm", "machine", "learning", "neural", "network", "deep", "learning", "artificial", "intelligence", "ai", "ml", "nlp", "cv"]) == 11