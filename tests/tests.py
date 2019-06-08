import os
import unittest

from ultimate_discord_smash_bot import characters
from ultimate_discord_smash_bot import message_functions as mf

"""Only testing what is worth testing, this is separate from trying to dismock the bot"""

class _Msg:

	def __init__(self, content):
		self.content = content

class TestMessageFunctions(unittest.TestCase):

	def test_display_matchup(self):
		matchup_message = _Msg('matchup sonic little mac')
		self.assertEqual(
			mf._display_matchup(matchup_message),
			'https://ssbworld.com/matchup/little-mac-vs-sonic'
		)

	def test_display_data(self):
		data_message = _Msg('!data sonic')
		self.assertEqual(
			mf._display_data(data_message),
			"https://ultimateframedata.com/sonic.php"
		)

if __name__ == '__main__':
	unittest.main()

