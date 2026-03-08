def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    top_k = recommended[:k]
    
    count_intersection = 0
    for i in relevant: 
        if i in top_k: 
            count_intersection += 1
    
    precision = count_intersection/k

    recall = count_intersection/len(relevant)

    return [precision, recall]