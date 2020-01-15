# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:55:01 2019

@author: sdesai
"""

import re


def main(issueID):
	"""
	CREW-156251
	CREW-156287
	CREW-156295
	CREW-154318
	"""
	string = issueID
	# matches all whitespace characters
	patternSpaces = '\s+'
	# empty string
	replaceComma = ','
	# Forming new string
	string_processed = re.sub(patternSpaces, replaceComma, string)
	if string_processed[-1] == ',':
		print('Comma Defect!!')
		string_processed = string_processed[:-2]
	else:
		print('String without comma defect!!')
		pass
	
	final_string = f'key in({string_processed})'
	return final_string

