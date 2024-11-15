from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def render_index_page():
    ''' This function initiates the rendering of the main application
    ''' 
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detect():
    text_to_analyze = request.args.get('textToAnalyze') 
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] == None:
        return 'Invalid text! Please try again!'
    anger, disgust, fear, joy, sadness, dominant_emotion = result.values()
    return f'''For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}
             and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}.'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)