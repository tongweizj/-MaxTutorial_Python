import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
  """测试 name_function.py"""

  def test_first_last_name(self):
    formatted_name = get_formatted_name('janis', 'joplin')
    self.assertEqual(formatted_name, 'Janis Joplin') # assertEqual 断言

  def test_first_middle_last_name(self):
    formatted_name = get_formatted_name('janis', 'joplin', 'middle')
    self.assertEqual(formatted_name, 'Janis Middle Joplin') # assertEqual 断言

if __name__ == '__main__':
  unittest.main()
