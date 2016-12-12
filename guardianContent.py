from theguardian import theguardian_content

def getContent(p):
	headers = {
		"show-fields" : "body",
		"page-size" : "200",
		"page" : str(p)
	}

	# create content
	content = theguardian_content.Content(api='2e433c1b-7fd1-46fc-be75-3f00732ca28c', **headers)

	# get all results of a page
	json_content = content.get_content_response()
	all_results = content.get_results(json_content)
	for result in all_results:
		print(result["fields"]["body"])

if __name__ == '__main__':
	p = 141
	for i in range(0, 10):
		getContent(p)
		p += 1
