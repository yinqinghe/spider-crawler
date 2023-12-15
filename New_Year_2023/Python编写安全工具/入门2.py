import os
class Domain:
    def __init__(self,domain,port,protocol):
        self.domain=domain
        self.port=port
        self.protocol=protocol

    def URL(self):
        if self.protocol =='https':
            URL='https://'+self.domain+':'+self.port+'/'
        if self.protocol =='http':
            URL='http://'+self.domain+':'+self.port+'/'
            return URL

    def lookup(self):
        os.system("host "+self.domain)

domain=Domain('google.com','443','https')

dir(domain)

domain.URL()
domain.lookup()