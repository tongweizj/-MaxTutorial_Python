# -*- coding: UTF-8 -*-

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
  """管理游戏资源和行为的类"""

  def __init__(self):
    """初始化游戏并创建游戏资源"""
    pygame.init()
    self.settings = Settings()
    self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    self.settings.screen_width = self.screen.get_rect().width
    self.settings.screen_height = self.screen.get_rect().height
    pygame.display.set_caption("Alien Invasion")
    
    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()
    self.aliens = pygame.sprite.Group()
    
    self._create_fleet()

  def run_game(self):
    """开始游戏的主循环"""
    while True:
      # 监视鼠标和键盘事件
      self._check_events()
      # 飞船实时更新
      self.ship.update()
      self.bullets.update()
      
      # 删除消失的子弹
      self._update_bullets()
      # 每次循环时都会重绘屏幕
      self._update_screen()



  def _check_events(self):  # _ 表示只在类内部使用的方法
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        self._check_keydown_events(event)
      elif event.type == pygame.KEYUP:
        self._check_keyup_events(event)                                               
      
  def _check_keydown_events(self, event):
    if event.key == pygame.K_RIGHT:
      # 向右移动飞船
      self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = True
    elif event.key == pygame.K_SPACE:
      self._fire_bullet()
    elif event.key == pygame.K_q:
      # q键 退出游戏
      sys.exit()
  
  def _check_keyup_events(self, event):
    if event.key == pygame.K_RIGHT:
      self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
      self.ship.moving_left = False

  def _fire_bullet(self):
    """创建一颗子弹，并切换到新屏幕"""
    if len(self.bullets) < self.settings.bullet_allowed:
      new_bullet = Bullet(self)
      self.bullets.add(new_bullet)

  def _update_bullets(self):
    for bullet in self.bullets.copy():
      if bullet.rect.bottom < 0:
        self.bullets.remove(bullet)
        # print(len(self.bullets))

  def _update_screen(self):
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()
    for bullet in self.bullets.sprites():
      bullet.draw_bullet()
    self.aliens.draw(self.screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()

  def _create_fleet(self):
    """创建外星人群"""
    alien = Alien(self)
    self.aliens .add(alien)

if __name__ == '__main__':
  # 创建游戏实例并运行游戏
  ai = AlienInvasion()
  ai.run_game()

