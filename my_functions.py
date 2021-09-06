def stream_proportions(df, rater, threshold, streaming_service):
    top_rated_count = df.loc[(df[streaming_service]==1) & 
                             (df[rater] >= threshold), 
                             streaming_service].count()
    lower_rated_count = df.loc[(df[streaming_service]==1) & 
                               (df[rater] < threshold), 
                               streaming_service].count()
    return top_rated_count, lower_rated_count