from bs4 import BeautifulSoup

class Bs(object):
    @classmethod
    def select(cls,input1,a_select):
        soup=BeautifulSoup(input1,'html.parser')
        return soup.select(a_select)

    @classmethod
    def find(cls,input1,a_select):
        soup=BeautifulSoup(input1,'html.parser')
        return soup.find(a_select)
