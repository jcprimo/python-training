# Summarize API
import os 
import requests
from smmryapi import SmmryAPI
import textwrap
from datetime import datetime

SMMRY_API_KEY=""
smmry = SmmryAPI(SMMRY_API_KEY)
global_url="https://api.smmry.com"
api_url = "&SM_API_KEY=" + SMMRY_API_KEY
target_url = "http://www.bbc.com/news/business-43298897"
coronavirus_url = "https://www.gatesnotes.com/Health/What-you-need-to-know-about-the-COVID-19-vaccine"
corona_china_url = "https://www.cnn.com/2020/04/30/business/lessons-from-china-business-coronavirus-intl-hnk/index.html"
migala_url = "https://migala.mx/1000-mascaras-regaladas-el-dia-de-muertos-o-por-que-odio-a-las-catrinas-panda/"
soldedad_url = "http://www.hacer.org/pdf/Paz00.pdf"
nature_url="https://www.nature.com/articles/d41586-020-00502-w"
hokkaido_url="https://www.bbc.com/news/world-asia-52305055?fbclid=IwAR3-kxNm0TGbv60waGDOkky17ELnmJwi1WS4WlB9_Vd3ZvvFcTUYjF9y9ak"

def save_to_file(s):
	title = s.sm_api_title
	if not title:
		title = "El papiro de: " + get_datetime()
	#body = format_text(s.sm_api_content)
	requests_left = s.sm_api_limitation
	total_reduction = s.sm_api_content_reduced
	file = open(title, "w")
	file.write(title+"\n")
	file.write("Total Reduction = " + str(total_reduction)+"\n")
	file.write("Total requests left = " + requests_left+"\n")
	write_body(s.sm_api_content, file)


def write_body(content, file):
	file.write("\n-------Start of Body Content-------\n")
	textos = content.split('\n')
	for line in textos:
		file.write(textwrap.fill(line, width=80))
		file.write('\n\n')
	file.write("-------End of Body Content-------")


def format_text(text):
	result = ""
	textos = text.split('\n')
	for line in textos:
		formatted = textwrap.fill(line, width=80)
		print(formatted)
		result += formatted
	return result


def print_attributes(s):
	attributes = (
		s.sm_domain,  # The domain name of the URL
		s.sm_api_title,  # The article's titled
		s.sm_url,  # URL of the article
		s.sm_api_content_reduced,  # Percent by which reduced
		s.sm_length,  # Number of sentences
		s.sm_requests_remaining,  # Number of queries left
		s.sm_api_keyword_array  # Keywords
	)

	result = """

	SMMRY reduced %s article "%s" from url
	[%s] by %s to %s sentences.

	You have %s requests remaining today.

	Top keywords are: %s.'
	"""
	print(result % attributes)


def get_datetime():
	# datetime object containing current date and time
	now = datetime.now()
	print("now =", now)

	# dd/mm/YY H:M:S
	dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
	print("date and time =", dt_string)
	return dt_string


def main():
	s = smmry.summarize(hokkaido_url, sm_length=15, sm_keyword_count=15, SM_WITH_BREAK='\n')
	save_to_file(s)
	print_attributes(s)
	title = s.sm_api_title
	body = s.sm_api_content
	requests_left = s.sm_api_limitation
	total_reduction = s.sm_api_content_reduced


if __name__ == "__main__":
	main()
