import requests


class WebClient(object):
    # 网页下载

    @classmethod
    def get_string(cls,url):
        # 下载字符串
        return requests.get(url).text

    @classmethod
    def get_bytes(cls,url):
        # 下载二进制
        res=requests.get(url)
        stream=res.content
        return stream

    @classmethod
    def save_string(cls,url,filename):
        html=cls.get_string(url)
        f=open(filename,'w+',encoding='utf-8')
        f.write(html)
        f.close()

    @classmethod
    def save_bytes(cls,url,filename):
        #保存二进制
        stream=cls.get_bytes(url)
        f=open(filename,'wb')
        f.write(stream)
        f.close()
