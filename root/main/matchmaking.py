import requests

API_URL = "https://api-inference.huggingface.co/models/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Can you please let us know more details about your ",
})

print(output)
