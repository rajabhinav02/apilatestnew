import requests
from configuration.configuration import *
from configuration.Resources import *
from configuration.payload import *
import json

class AddBook:

    abookurl = getconfig()['API']['endpoint']+ Resource.addresource
    gquery = "select * from Books"

    def add(self):
        #gquery = "select * from Books"

        res = requests.post(self.abookurl, json = bookpayload(self.gquery))
        res_json = res.json()
        print(res_json)
        assert res.status_code ==200 and "success" in res_json["Msg"]


    def update(self):
        row = rungquery(self.gquery)
        uquery = "update Books set aisle = %s where BookName = %s"
        data = (int(row[2])+1, row[0])
        runUquery(uquery, data)