#!/usr/bin/env python3

import json

class GameStats(object):
	""" 跟踪游戏的统计信息 """
	def __init__(self, ai_settings):
		""" 初始化统计信息 """
		self.ai_settings = ai_settings
		self.reset_stats()

		# 游戏刚启动时处于活动状态
		self.game_active = False

		# 在任何情况下都不应重置最高得分
		self.load_stats()

	def load_stats(self):
		"""从文件中读取game stats"""
		try:
			with open(self.ai_settings.settings_file) as f:
				high_score = json.load(f)
				self.high_score = int(high_score)
		except FileNotFoundError:
			self.high_score = 0

	def store_stats(self):
		"""将game stats存储到文件中"""
		with open(self.ai_settings.settings_file, 'w') as f:
			json.dump(str(self.high_score), f)

	def reset_stats(self):
		""" 初始化在游戏运行期间可能变化的统计信息 """
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
