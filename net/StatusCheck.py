from urllib.request import urlopen
class StatusCheck(object):
    """docstring for StatusCheck"""
    def __init__(self):
        super(StatusCheck, self).__init__()
        self.url="www.google.com"

    def checkStatus(self):
        real_address=self.get_real_address(self.url)
        resp=urlopen(real_address)
        return resp.code

    def set_url(self,url):
        self.url=url

    def get_real_address(self,address):
        real_address="http://"+address
        try:
            index=self.url.index("http")
            if index==0:
                real_address=self.url
        except:
            pass
        return real_address

    def get_title(self):
        real_address=self.get_real_address(self.url)
        resp=urlopen(real_address)
        value=None
        data=str(resp.read(10000)).lower()
        try:
            index=data.index("<title>")
            index2=data.index("</title>")
            value=data[index+7:index2]
        except:
            value="error, can't get value."
        return value
