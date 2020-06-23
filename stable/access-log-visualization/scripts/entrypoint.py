#!/usr/bin/python
import argparse, os

def main():
	# Parse arguments
	parser = argparse.ArgumentParser(description='Visualize access.log file')
	parser.add_argument('-i', '--input', help='input access.log', required=True)
	parser.add_argument('-o', '--output', help='output directory')

	args = parser.parse_args()

	access_log_path = args.input
	output_path = args.output

	# Environment variable to be used in the Jupyter notebook
	os.environ['ACCESS_LOG_PATH'] = access_log_path

	visualize(output_path, access_log_path)


def visualize(output_path, access_log_path):
	bash_line = '/usr/local/bin/jupyter nbconvert --to html --ExecutePreprocessor.timeout=3600 \
		        --execute /home/appuser/access-log.ipynb --output '


	if output_path == None:
		if os.path.dirname(access_log_path) == "":
	        	bash_line = bash_line + '/home/appuser/output.html'
		else:
	        	bash_line = bash_line + os.path.dirname(access_log_path) + '/output.html'
	else:
		bash_line = bash_line + output_path + '/output.html'

	os.system(bash_line)


if __name__== "__main__":
	main()

