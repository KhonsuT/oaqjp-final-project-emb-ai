'''
Emotion detectio module
'''
import requests
import json
def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    content = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, headers=Headers, json=content,timeout=10)
    response_json = json.loads(response.text)
    emotions = response_json['emotionPredictions'][0]['emotion']
    dominant_emotion_score = -1
    dominant_emotion = ""
    for emotion in emotions:
        if emotions[emotion] > dominant_emotion_score:
            dominant_emotion_score = emotions[emotion]
            dominant_emotion = emotion
    emotions['dominant_emotion'] = dominant_emotion
    return emotions