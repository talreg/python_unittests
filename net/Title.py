from net.StatusCheck import StatusCheck
class Title(object):
    """docstring for Ttile"""
    def __init__(self):
        super(Title, self).__init__()
    def get_url_title(self,url):
        s=StatusCheck()
        s.set_url(url)
        return s.get_title()
    def check_url(self,url):
        s=StatusCheck()
        return s.checkStatus()
