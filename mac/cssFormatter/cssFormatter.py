import sublime
import sublime_plugin
import urllib

class CssFormatterCommand(sublime_plugin.TextCommand):
	def run(self, edit):	
		txt  = ''	
		sels = self.view.sel()

		for sel in sels:
			txt += self.view.substr(sel)

		cssFormatterURL = "http://dev.ui.naver.com/tool/n-met/cssFormatter/formatted2.php"
		cssData = urllib.parse.urlencode({"org[]":txt, "from":"sublimetext"}).encode('UTF-8')
		url = urllib.request.Request(cssFormatterURL, cssData)
		url.add_header("Content-type", "application/x-www-form-urlencoded")
		ResponseData = urllib.request.urlopen(url).read().decode("utf8", 'ignore')

		for sel in sels:
			self.view.erase(edit, sel)
			
		for region in self.view.sel():
			self.view.insert(edit, region.end(), ResponseData.replace('\r\n', '\n'));