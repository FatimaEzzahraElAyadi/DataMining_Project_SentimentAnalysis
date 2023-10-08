import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from datetime import datetime



def sentiment_score(review):

    model_name = 'nlptown/bert-base-multilingual-uncased-sentiment'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    tokens = tokenizer.encode(review, return_tensors='pt')
    result = model(tokens)
    rating = int(torch.argmax(result.logits))+1
    if rating <= 2:
        return -1
    elif rating == 3:
        return 0
    else:
        return 1


def transform(**kwargs):
    
    print("-------------------------transform-------------------------")
    extracted_data = kwargs['ti'].xcom_pull(task_ids='extract_task')
    df = pd.DataFrame(extracted_data)
    df = df.dropna(subset=['text'])

    df = df[:100].copy()

    columns_to_keep = ['title', 'city', 'address', 'phone', 'text']
    df = df[columns_to_keep]


    df['sentiment']=lambda x: sentiment_score(x[:512])




    df['totalScore'] = df['text'].apply(lambda x: df['sentiment'] if isinstance(x, str) else np.nan)
    df.dropna()
    df = df.drop('text', axis=1)


    return df.values.tolist()