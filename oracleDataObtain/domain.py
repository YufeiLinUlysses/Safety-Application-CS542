from urllib.parse import urlparse


def GetSubDomainName(sUrl):
    try:
        return urlparse(sUrl).netloc
    except:
        return ''

def GetDomainName(sUrl):
    try:
        tempRes = GetSubDomainName(sUrl).split('.')
        if len(tempRes) < 2:
            return ''
        return tempRes[-2] + '.' + tempRes[-1]
    except:
        return ''


