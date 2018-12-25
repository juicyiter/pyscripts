# File:    getStockContent.py
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
# 2018-10-26 21:20 JuicyITer <mengoreo@163.com> created.
## =====================


import urllib.request

import getStockID as getstocklist

urlToList = getstocklist.urlToList

stockCodeUrl = 'http://quote.eastmoney.com/stocklist.html'

start = '20180909'
end = '20181010'

allCodelist = urlToList(stockCodeUrl)

for code in allCodelist:
    print("Getting stock {}'s content...".format(code))

    if code[0] == '6':
        url = 'http://quotes.money.163.com/service/chddata.html?code=0' + code +\
            '&start=' + start + '&end=' + end + '&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'

    else:
        url = 'http://quotes.money.163.com/service/chddata.html?code=1' + code +\
            '&start=' + start + '&end=' + end + '&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'

    urllib.request.urlretrieve(url, '/Users/jit/Desktop/Pydir/stockData/' + code + '_' + end + '.csv')
