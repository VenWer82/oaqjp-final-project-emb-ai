import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        res1 = emotion_detector('I am glad this happened')
        self.assertEqual(res1['dominant_emotion'], 'joy', 'Joy test failed')

        res2 = emotion_detector('I am really mad about this')
        self.assertEqual(res2['dominant_emotion'], 'anger', 'Anger test failed')

if __name__ == '__main__':
    unittest.main()