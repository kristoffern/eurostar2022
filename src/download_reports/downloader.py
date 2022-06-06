"""
	Tool used as an example showing how we can download reports from a webserver.
	Filestructure of the reports are as follows:

	http://www.northerntest.se/files/reports/
										[DATE]/
											[REPORT_NAME]s/
												[REPORT_NAME].json
		
	There are:

		- Daily reports generated Tuesday - Saturday
		- Weekly reports generated on Sundays
		- Monthly reports generated on the 1st of every month

	reports
		2022-04-01
			daily-reports
				daily-report.json
			monthly-reports
				monthly-report.json
		2022-04-02
			daily-reports
				daily-report.json
		2022-04-03
			weekly-reports
				weekly-report.json
		2022-04-04
		2022-04-05
			daily-reports
				daily-report.json
"""

import datetime
import os
import shutil
import subprocess
import zipfile

base_path = 'downloads'

if os.path.exists(base_path):
	shutil.rmtree(base_path)

os.mkdir(base_path)

d = datetime.date(2022,4,1)
td = datetime.timedelta(days=1)

for _ in range(0,10):
	os.mkdir(os.path.join(base_path, str(d)))

	if d.weekday() in [1,2,3,4,5]:
		report_name = 'daily-report'
	if d.weekday() == 6:
		report_name = 'weekly-report'
	if d.day == 1:
		report_name = 'monthly-report'


	p = subprocess.run(['wget',
						'--no-check-certificate',
						f'http://www.northerntest.se/files/reports/{d}/{report_name}s/{report_name}.json',
						f'--directory-prefix={os.path.join(base_path, str(d))}'])

	d = d + td

shutil.make_archive('downloaded_reports', 'zip', 'downloads')
