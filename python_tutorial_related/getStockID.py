# !/usr/local/bin/python3
# File:    getStockID.py
# Author:  JuicyITer <mengoreo@163.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# Copyright 2005 Duke University

# History:
## =====================
# 2018-10-26 17:33 JuicyITer <mengoreo@163.com> created.
## =====================


import urllib.request
import re

stock_url = 'http://quote.eastmoney.com/stocklist.html'

def urlToList(url):
    allCodeList = []
    html = urllib.request.urlopen(url).read()
    html = html.decode('gbk')

    s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">'

    pat = re.compile(s)
    code = pat.findall(html)
    for item in code:
        if(item[0] == '6' or item[0] == '3'\
           or item[0] == '0'):
           allCodeList.append(item)

    return allCodeList


if __name__ == '__main__':
    allCodeList = urlToList(stock_url)
    print(allCodeList)
