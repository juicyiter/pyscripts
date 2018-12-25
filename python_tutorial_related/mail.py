#! /usr/local/bin/python3
# File:    mail.py
# Author:  JuicyITer <contactme@juicyiter.com>
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
# 2018-10-28 12:10 JuicyITer <contactme@juicyiter.com> created.
## =====================


import yagmail

def sendmail(title, contents, fileslist):
    yag = yagmail.SMTP("juicyiter@qq.com", 'mxb1240523210', 'smtp.qq.com', 465)
    yag.send(['contactme@juicyiter.com'], title, contents, fileslist)


sendmail("test", "hello", ['visitor_system.py'])
