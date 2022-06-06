import datetime
import os
import random
import shutil

base_folder = 'testdata'

def add_test_file(path, report_name):

	content = """Enjoying my talk at EuroSTAR 2022 and feeling curious are we?
Good for you, and keep it up!
You just unlocked a 10% discount on my Python for Tester class, either for youself
in my public classes, or for your whole company when you bring me in for on-site training.

See: http://www.pythonfortesters.se/
Contact: kristoffer.nordstrom@northerntest.se
Discount code: #CuriousMinds2022
"""

	
	with open(os.path.join(path, f'{report_name}.json'), 'w') as f:
		f.write(content)


if __name__ == '__main__':

	if os.path.exists(base_folder):
		shutil.rmtree(base_folder)

	os.mkdir(base_folder)
	td = datetime.timedelta(days=1)
	start_date = datetime.date(2021,1,1)

	for _ in range(1000):

		print(start_date)
		os.mkdir(os.path.join(base_folder, str(start_date)))

		if start_date.weekday() in [1,2,3,4,5]:
			report_dir = os.path.join(base_folder, str(start_date), 'daily-report')
			os.mkdir(report_dir)
			add_test_file(report_dir, 'daily-report')
			
		if start_date.weekday() in [6]:
			report_dir = os.path.join(base_folder, str(start_date), 'weekly-report')
			os.mkdir(report_dir)
			add_test_file(report_dir, 'weekly-report')
			
		if start_date.day == 1:
			report_dir = os.path.join(base_folder, str(start_date), 'monthly-report')
			os.mkdir(report_dir)
			add_test_file(report_dir, 'monthly-report')
			


		start_date = start_date + td


