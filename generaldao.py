# -*- coding: utf-8 -*-
import sys
import re, string
import json

import connectiondb as conn


def login(username,password):

        query = "SELECT id,password FROM account WHERE username = '%s' LIMIT 1; " %(username)
        data = ""
        cursor = conn.run_query(query,data)

        flag1 = 0
        id = ""

        for (id_db, password_db) in cursor:
                password_bd = str(password_bd)
                password_bd = re.sub('[%s]' % re.escape(string.punctuation),"", password_bd).lower()
                if password == password_bd:
                        flag1 = 1
                        id = id_db
        if flag1 == 1:

                data = {'id': id ,'username': username}
                final = final = json.dumps(data,ensure_ascii=False).encode('utf8')
                return final
        else:

                data = {'id': '0' ,'username': '0'}
                final = final = json.dumps(data,ensure_ascii=False).encode('utf8')
                return final