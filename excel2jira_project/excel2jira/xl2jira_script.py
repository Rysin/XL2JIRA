# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:55:01 2019

@author: sdesai
"""

import re


def main(issueID):
	"""
	
	"""
	string = issueID
	# matches all whitespace characters
	patternSpaces = '\s+'
	# empty string
	replaceComma = ','
	# Forming new string
	string_processed = re.sub(patternSpaces, replaceComma, string)
	final_string = f'key in({string_processed})'
	return final_string
