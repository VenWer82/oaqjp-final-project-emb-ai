''' Executing this module initiates the application of emotion detection to be executed over the 
    Flask channel and deployed on localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def render_index_page():
    ''' This function initiates the rendering of the main application
        over the flask channel'''
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detect():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotions, dominant emotion and its confidence 
        score for the provided text.'''
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    anger, disgust, fear, joy, sadness, dominant_emotion = result.values()
    return f'''For the given statement, the system response is 'anger': {anger},
               'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. 
               The dominant emotion is {dominant_emotion}.'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
