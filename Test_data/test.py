
new_file_path = 'llama_mygovneo.csv'
new_data = pd.read_csv(new_file_path)

print(new_data.head())

def evaluate_similarity(actual, predicted):
    """
    Basic evaluation function to check if the predicted answer contains key elements of the actual answer.
    This is a very simplistic approach and might not fully capture the semantic similarity.
    """

    actual_lower = actual.lower()
    predicted_lower = predicted.lower()
    actual_words = set(actual_lower.split())
    match_count = sum(word in predicted_lower for word in actual_words)
    return 1 if match_count / len(actual_words) > 0.5 else 0

data['Score_compact'] = data.apply(lambda row: evaluate_similarity(row['Actual answer'], row['Predicted_Answer_compact']), axis=1)
data['Score_refine'] = data.apply(lambda row: evaluate_similarity(row['Actual answer'], row['Predicted_Answer_refine']), axis=1)
data['Score_summary'] = data.apply(lambda row: evaluate_similarity(row['Actual answer'], row['Predicted_Answer_tree_summary']), axis=1)

average_scores = {
    'Average_Score_compact': data['Score_compact'].mean(),
    'Average_Score_refine': data['Score_refine'].mean(),
    'Average_Score_summary': data['Score_summary'].mean()
}

average_scores, data.tail()



