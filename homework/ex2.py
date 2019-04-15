from urllib.request import urlopen
from bs4 import BeautifulSoup
from pyexcel import *
from pyexcel_xls import *
from pyexcel_xlsx import *
from collections import OrderedDict
#1. Open Connection
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode('utf8')

#2. Find ROI (Region of Interest)
soup = BeautifulSoup(html_content, 'html.parser')
div = soup.find("div",attrs={'style':'overflow:hidden;width:100%;border-bottom:solid 1px #cecece;'})
table = div.table
tr_list = table.find_all('tr')
list_1=[]
for tr in tr_list:
    td_list = tr.find_all('td')
    category = td_list[0].string
    quy1 = td_list[1].string
    quy2 = td_list[2].string
    quy3 = td_list[3].string
    quy4 = td_list[4].string
    bang = OrderedDict({
        'Category': category,
        '1': quy1,
        '2': quy2,
        '3': quy3,
        '4': quy4,
    })
    list_1.append(bang)
save_as(records=list_1, dest_file_name="report.xls")
            

