# -*- coding: utf-8 -*-
import sys
import re, string
import json

import connectiondb as conn


def login(username,password):

        query = "SELECT id,password FROM account WHERE username = '%s' LIMIT 1; " %(username)
        data = ""
        print (query)
        cursor = conn.run_query(query,data)

        flag1 = 0
        id = ""

        for (id_db, password_db) in cursor:
            if password == password_db:
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