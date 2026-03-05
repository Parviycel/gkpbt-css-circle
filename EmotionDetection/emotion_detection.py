import requests
import json

def emotion_detector(text_to_analyze):
    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = { "raw_document": { "text": text_to_analyze } }
    response = json.loads(requests.post(URL, headers=headers, json=body).text)["emotionPredictions"]
    dominant_emotion = "anger"
    dominant_emotion_score = response[0]['emotion']['anger']
    disgust = response[0]['emotion']['disgust']
    if dominant_emotion_score < disgust:
        dominant_emotion_score = disgust
        dominant_emotion = "disgust"
    fear = response[0]['emotion']['fear']
    if dominant_emotion_score < fear:
        dominant_emotion_score = fear
        dominant_emotion = "fear"
    joy = response[0]['emotion']['joy']
    if dominant_emotion_score < joy:
        dominant_emotion_score = joy
        dominant_emotion = "joy"
    sadness = response[0]['emotion']['sadness']
    if dominant_emotion_score < sadness:
        dominant_emotion_score = sadness
        dominant_emotion = "sadness"
    return {
        "anger": response[0]['emotion']['anger'],
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion,
    }
