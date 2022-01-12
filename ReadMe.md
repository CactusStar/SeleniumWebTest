# Structure introduce for this framework
1. To run multiple test cases and generate report, Unittest framework adopt and also HTMLTestRunner adopt
2. Assets is used for store configuration and data for each page
3. framework is used for store Base.py(some common behavior in web page) and BaseBrowser.py(used for webdriver and open/quit browser)
4. logs is used for generate log
5. Objects is used for element collection, seperated by pages
6. Scripts is used for store test case scripts, seperated by pages
7. Test Report is used for store test report
8. Utilities is used for store page object which means this is seperated by pages and each page behaviors will be stored in this folder

# HTMLTestRunner update to support python 3
1. Line 101 ==> StringIO --> io: update related call
2. Line 676 ==> if not rmap.has_key(cls): --> if not cls in rmap:
3. Line 800 ==> uo = o.decode('latin-1') --> uo = e
4. Line 806 ==> ue = e.decode('latin-1') --> ue = e
5. Line 664 ==> print >> sys.stderr, '\nTime Elapsed: %s' %(self.stopTime-self.startTime) --> print (sys.stderr, '\nTimeElapsed: %s' % (self.stopTime-self.startTime))
