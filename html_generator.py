class Generator(object):
	"""docstring for Generator"""
	def __init__(self):
		self.dataCol = []

	def collect_data(self, data):
		if data is None:
			return
		self.dataCol.append(data)

	def output(self):
		fout = open("output.html", "w")
		fout.write("<html><meta charset=\"utf-8\">")
		fout.write("<body>")
		fout.write("<table>")
		for data in self.dataCol:
			fout.write("<tr>")
			fout.write("<td>%s</td>" % data["url"])
			fout.write("<td>%s</td>" % data["title"].encode("utf-8"))
			fout.write("<td>%s</td>" % data["summary"].encode("utf-8"))
			fout.write("</tr>")
		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")
		fout.close()
		#if html file fail to encode
		font1 = open('output.txt', 'w')
		font1.write('# 1000 pices of Baidu Baike\n')
		for data in self.dataCol:
			font1.write("# %s\n" % data['title'].encode('utf-8'))
			font1.write("**[%s](%s)**\n" % (data['url'],data['url']))
			font1.write(">%s\n" % data['summary'].encode('utf-8'))
			font1.write("* * *\n")
		font1.close()


		