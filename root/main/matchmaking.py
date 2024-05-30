import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "AIzaSyDmLQuUp2Rxi0_5U6EtExfERczih72he_c"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')

def get_keywords(input_text) :
	response = model.generate_content(f"list out all the important keywords from the given text and return them in a comma seperated form : {input_text}")

	list_of_keywords = response.text.split(',')
	return list_of_keywords