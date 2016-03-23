# -*- coding: utf-8 -*-
import urllib2
# import json
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# import requests
# import pdb

if __name__=="__main__":
    url='http://edu.ucas.ac.cn:8080/TRRP_SEP/WebService/PredictiveSearch.asmx/GetAllPredictionsWithCodeInfo?className=jzs010114&codeOrName='
    try:
        response=urllib2.urlopen(url+'中国科学院')
        cont=response.read()
        tree=etree.HTML(cont)
        for codeinfo in tree.getchildren()[0].getchildren()[0].getchildren():
            print codeinfo[2].text
        else:
            print "空"
        # pdb.set_trace()
        # print cont
    except Exception, e:
        pass