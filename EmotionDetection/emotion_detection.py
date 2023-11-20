"""This module analyzes the emotion of a given input"""


import requests
import json

def emotion_detector(text_to_analyse):
    """This function analyzes the emotion of the given text"""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = response.json()
    if response.status_code == 200:
        pre = formatted_response['emotionPredictions'][0]['emotion']

        anger_score = pre['anger']
        disgust_score = pre['disgust']
        fear_score = pre['fear']
        joy_score = pre['joy']
        sadness_score = pre['sadness']

        top = max(pre, key=lambda key: pre[key])
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None

        top = None

    ret = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': top
        }

    return ret
