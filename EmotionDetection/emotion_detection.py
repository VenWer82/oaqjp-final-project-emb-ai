import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json =  {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=input_json, headers=headers)
    if response.status_code == 400:
        anger = disgust = fear = joy = sadness = dom_emotion = None

    elif response.status_code == 200:    
        data = json.loads(response.text) 
        emotions_dict = data['emotionPredictions'][0]['emotion']
        dom_emotion, score = max(emotions_dict.items(), key= lambda x: x[1])
        anger, disgust, fear, joy, sadness = emotions_dict.values()

    return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': dom_emotion}
    