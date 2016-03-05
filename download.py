import urllib2

def download_file(download_url, fname):
    response = urllib2.urlopen(download_url)
    file = open(fname + ".pdf", 'w')
    file.write(response.read())
    file.close()
    print("Completed")

with open("test.html") as f:
	for line in f:
		for i in range(8526814, 8526998):
			if(line.find(str(i)) != -1 and line.find("pdf") != -1):
				url = "https://canvas.instructure.com/courses/990374/modules/items/" + str(i)
				response = urllib2.urlopen(url)
				content = response.read()
				idx = content.find("download\"")
				fname = content[content.find("<h2>") + 4: content.find("</h2>")]
				print fname
				new_url = "https://canvas.instructure.com" + content[idx - 31:idx + 8]
				print new_url
				download_file(new_url, fname)