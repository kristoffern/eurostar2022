"""
	Demo code showing how to use GSpread and integrating with Goggle Sheets
	In order to use this create authentication for a service account or your 
	own account.
		
	# Service Account authentication:
	- https://docs.gspread.org/en/latest/oauth2.html#service-account

	# Personal account authentication
	- https://docs.gspread.org/en/latest/oauth2.html#for-end-users-using-oauth-client-id

	If you're using your own account for authentication, replace the line:
		
		gc = gspread.service_account()
	
	with the following line instead

		gc = gspread.oauth():
"""

import gspread
gc = gspread.service_account()

sh = gc.create("Example spreadsheet")
sh = gc.open("Example spreadsheet")
sh = gc.open_by_key("1SK4Z1oqv6AdNWjh7MC2WWo8fZPlnIzDG_lsgIFmB0H4")

EMAIL_TO_SHARE_WITH = 'kristoffer.nordstrom@northerntest.se'

sh.share(EMAIL_TO_SHARE_WITH, perm_type='user', role='writer')

worksheet = sh.add_worksheet(title="A worksheet", rows=100, cols=20)
worksheet.update('B1', 'Bingo!')
worksheet.update('A1:B2', [[1, 2], [3, 4]])

values_list = worksheet.row_values(1)
values_list = worksheet.col_values(1)
