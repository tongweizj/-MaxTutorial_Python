class AnonymousSurvey:
  """收集匿名调查问卷的答案"""

  def __init__(self, question):
      """存储一个问题，并为存储答案做准备"""

      self.question = question
      self.responses = []

  def show_question(self):
    print(self.question)

  def store_response(self, new_respone):
    self.responses.append(new_respone)
  
  def show_results(self):
    print("Survey results:")
    for response in self.responses:
      print(f"- {response}")