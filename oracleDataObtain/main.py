import threading
import queue
import spider
import domain
import file_manager

PROJECT_NAME = 'crime data'
HOMEPAGE = 'https://tieba.baidu.com/index.html'
DOMAIN_NAME = domain.GetDomainName(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
DATA_QUANTITY = 2
NUMBER_OF_THREADS = 6
threadQueue = queue.Queue()
iTotalCrawlLink = 0

def CreateWorker():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=Work)
        t.daemon = True
        t.start()

def Work():
    while True:
        sUrl = threadQueue.get()
        spider.CSpider.CrawlPage(threading.current_thread().name, sUrl)
        threadQueue.task_done()

def CreateJob():
    for link in file_manager.File2Set(QUEUE_FILE):
        threadQueue.put(link)
    threadQueue.join()
    Crawl()

def Crawl():
    linkSet = file_manager.File2Set(QUEUE_FILE)
    if len(linkSet) > 0:
        CreateJob()
    # global iTotalCrawlLink
    # iTotalCrawlLink += 1
    # if len(linkSet) > 0 and iTotalCrawlLink < DATA_QUANTITY:
    #     CreateJob()


spider.CSpider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
CreateWorker()
Crawl()