import pygame.font

class Scoreboard:
  """现实的分信息"""

  def __init__(self, ai_game):
    """初始化"""
    self.screen = ai_game.screen
    self.screen_rect = self.screen.get_rect()
    self.settings = ai_game.settings
    self.stats = ai_game.stats

    # 显示得分信息时使用的字体设置
    self.text_color = (30, 30, 30)
    self.font = pygame.font.SysFont(None, 48)
    # 准备初始得分图像
    self.prep_score()
  
  def prep_score(self):
    """将得分转换为一幅渲染的图像"""
    score_str = str(self.stats.score)
    self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
    