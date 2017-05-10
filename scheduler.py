import url_manager, html_downloader, html_parser, html_generator

class Spider(object):
	"""docstring for Spider"""
	def __init__(self):
		self.url = url_manager.UrlManager()
		self.downloader = html_downloader.Downloader()
		self.parser = html_parser.Parser()
		self.generator = html_generator.Generator()

	def craw(self, root_url):
		count = 1
		self.url.add_new_url(root_url)
		while self.url.has_new_url():
			try:	
				new_url = self.url.get_new_url()
				print "Craw %d: %s" %(count, new_url)
				html_content = self.downloader.download(new_url)
				new_url, new_data = self.parser.parse(new_url, html_content)
				self.url.add_new_urls(new_url)
				self.generator.collect_data(new_data)
				if count == 1000:
					break
				count += 1
			except Exception as e:
				print "Craw fail!"
				print e
		self.generator.output()

if __name__ == "__main__":
	root_url = "http://baike.baidu.com/item/Python"
	obj_spider = Spider()
	obj_spider.craw(root_url)