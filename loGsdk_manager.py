import pygame
import numpy as np
import threading
import time

fps = 100
class PixelWindow:
    def __init__(self, width, height, scale=10, title="Pixel Window", fps=100):
        pygame.init()
        self.width = width
        self.height = height
        self.scale = scale
        self.fps = fps

        self.screen = pygame.display.set_mode((width*scale, height*scale))
        pygame.display.set_caption(title)

        self.surface = pygame.Surface((width, height))
        self.clock = pygame.time.Clock()

        # черно-белая матрица (0=черный, 1=белый)
        self.matrix = np.zeros((height, width), dtype=np.uint8)
        self.running = True
        self._lock = threading.Lock()

        # поток без daemon
        self.thread = threading.Thread(target=self.loop, daemon=False)
        self.thread.start()

    def update_display(self):
      """Метод для вызова в ГЛАВНОМ потоке"""
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              self.running = False
      with self._lock:
          rgb_matrix = np.stack([self.matrix.T * 255] * 3, axis=-1)
          pygame.surfarray.blit_array(self.surface, rgb_matrix)
      scaled = pygame.transform.scale(
          self.surface,
          (self.width * self.scale, self.height * self.scale)
      )
      self.screen.blit(scaled, (0, 0))
      pygame.display.flip()
   

    def set_pixel(self, x, y, value):
        """
        Установить один пиксель
        value: 0 или 1
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            with self._lock:
                self.matrix[y, x] = 1 if value else 0
        else:
            raise ValueError("Координаты за пределами матрицы")

    def fill(self, value):
        """Залить весь экран 0 или 1"""
        with self._lock:
            self.matrix[:, :] = 1 if value else 0

    def loop(self):
       print("run: loop")      
       while self.running:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   print("run: exit")
                   self.running = False
                   # self.close()      
           self.update_display()  # обновляем экран каждый кадр
           self.clock.tick(self.fps)      
       pygame.quit()

    def close(self):
        """Закрыть окно корректно"""
        self.running = False
        self.thread.join()