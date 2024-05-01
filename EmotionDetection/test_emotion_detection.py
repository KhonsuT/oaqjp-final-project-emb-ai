import unittest
from emotion_detection import emotion_detector
class testEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        tests = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear")
        ]
        for test in tests:
            self.assertEqual(emotion_detector(test[0])['dominant_emotion'],test[1])

unittest.main()