from html.parser import HTMLParser
from urllib import parse


class CLinkFind(HTMLParser):
    def __init__(self, sBaseUrl, sPageUrl):

        super().__init__()
        self.m_Page = sPageUrl
        self.m_Base = sBaseUrl
        self.m_Link = set()

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for sType, sContent in attrs:
                if sType == 'href':
                    sUrl = parse.urljoin(self.m_Base, sContent)
                    self.m_Link.add(sUrl)

    # def FindLink(self):
    #     pass

    def ResultLink(self):
        return self.m_Link

#TODO: finish contextFinder
class CContextFind(HTMLParser):
    def __init__(self, sBaseUrl, sPageUrl):

        super().__init__()
        self.m_Page = sPageUrl
        self.m_Base = sBaseUrl
        self.m_Content = ""

    # def handle_starttag(self, tag, attrs):
    #     print("tag is", tag)
    #     print("attrs is", attrs)
    #     # if tag == "a":
    #     #     for sType, sContent in attrs:
    #     #         if sType == 'href':
    #     #             sUrl = parse.urljoin(self.m_Base, sContent)
    #     #             self.m_Link.add(sUrl)
    #
    # def Result(self):
    #     return self.m_Content