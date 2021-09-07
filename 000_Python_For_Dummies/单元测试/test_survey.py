import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
  def setUp(self):
    question = "What language did you first learn to speak?"
    self.my_survey = AnonymousSurvey(question)
    self.respones = ['English', 'Spanish', 'Mandarin']
      
  def test_store_single_response(self):
    self.my_survey.store_response(self.respones[0])
    self.assertIn(self.respones[0], self.my_survey.responses)
  
  def test_store_three_responses(self):
    for response in self.respones:
      self.my_survey.store_response(response)
    for response in self.respones:
      self.assertIn(response, self.my_survey.responses)
      
if __name__ == '__main__':
  unittest.main()