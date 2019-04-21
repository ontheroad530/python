#!/usr/bin/env python3

import pygame

class Background():
	def __init__(self, screen):
		self.screen = screen
		self.screen_rect = screen.get_rect()		

		self.image = pygame.transform.scale(
			pygame.image.load('images/bg.jpeg'), 
			(self.screen_rect.width, self.screen_rect.height))
		self.rect = self.image.get_rect()
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
