from urllib.request import urlopen
import find_part
import file_manager

class CSpider:


    m_ProjectName = ''
    m_BaseUrl = ''
    m_DomainName = ''
    m_QueueFile = ''
    m_CrawledFile = ''
    m_QueueSet = set()
    m_CrawledSet = set()
    def __init__(self, sProjectName, sBaseUrl, sDomainName):
        CSpider.m_ProjectName = sProjectName
        CSpider.m_BaseUrl = sBaseUrl
        CSpider.m_DomainName = sDomainName
        CSpider.m_QueueFile = sProjectName + "/queue.txt"
        CSpider.m_CrawledFile= sProjectName + "/crawled.txt"
        self.Boot()
        self.CrawlPage("first spider", CSpider.m_BaseUrl)

    @staticmethod
    def Boot():
        file_manager.CreateProject(CSpider.m_ProjectName)
        file_manager.CreateData(CSpider.m_ProjectName, CSpider.m_BaseUrl)
        CSpider.m_QueueSet = file_manager.File2Set(CSpider.m_QueueFile)
        CSpider.m_CrawledSet = file_manager.File2Set(CSpider.m_CrawledFile)

    @staticmethod
    def CrawlPage(sName, sUrl):
        if sUrl not in CSpider.m_CrawledSet:
            print(sName + "is crawling" + sUrl)
            print("need finished job:" + str(len(CSpider.m_QueueSet)) + "finished:" + str(len(CSpider.m_CrawledSet)))
            #CSpider.AddData(sUrl)
            CSpider.AddLink2Queue(CSpider.GatherLinks(sUrl))
            CSpider.m_CrawledSet.add(sUrl)
            CSpider.m_QueueSet.remove(sUrl)
            CSpider.UpdateFile()

    @staticmethod
    def GatherLinks(sUrl):
        sHtml = ''
        try:
            oResponse = urlopen(sUrl)
            if "text/html" in oResponse.getheader('Content-Type'):
                htmlByte = oResponse.read()
                sHtml = htmlByte.decode("utf-8")
                oFinder = find_part.CLinkFind(CSpider.m_BaseUrl, sUrl)
                oFinder.feed(sHtml)
        except:
            print("error")
            return set()

        return oFinder.ResultLink()

    @staticmethod
    def AddData(sUrl):
        try:
            oResponse = urlopen(sUrl)
            htmlByte = oResponse.read()
            sHtml = htmlByte.decode("utf-8")
            oFinder = find_part.CContextFind(CSpider.m_BaseUrl, sUrl)
            oFinder.feed(sHtml)
        except:
            print("error")
            return " "



    @staticmethod
    def AddLink2Queue(linkSet):
        for sUrl in linkSet:
            if sUrl in CSpider.m_QueueSet:
                continue
            if sUrl in CSpider.m_CrawledSet:
                continue
            #so we do not crawl anything outside the domain website
            if CSpider.m_DomainName not in sUrl:
                continue
            CSpider.m_QueueSet.add(sUrl)

    @staticmethod
    def UpdateFile():
        file_manager.Set2File(CSpider.m_QueueSet, CSpider.m_QueueFile)
        file_manager.Set2File(CSpider.m_CrawledSet, CSpider.m_CrawledFile)

