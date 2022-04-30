from flask import Blueprint, render_template, redirect, request
import os
import time
from urllib.parse import urlparse
import re




class ListDB:
    def __init__(self):
        ListDB.__init__(self)
        self.data = {}
        
    def add_new(self, user="", wishlist="", data={}, date=0):
        data['date'] = date # set the timemap (date created)
        self.data[user][wishlist].append(data)
        
    def load(self):
        self.data = {}
        
    def save(self):
        self.data = {}
        
DB = ListDB()


class Verify:
    def NewItem(data):
        for item in data:
            
            if not data[item]:
                return False, "{} field is empty.".format(item.title())
            
            if item == 'name':
                if len(data[item]) > 256:
                    return False, "{} field is too long (max 256 chars).".format(item.title())
            elif item == 'img':
                if not re.match(r"(https?|ftp)://" r"(\w+(\-\w+)*\.)?" r"((\w+(\-\w+)*)\.(\w+))" r"(\.\w+)*" r"([\w\-\._\~/]*)*(?<!\.)", data[item]):
                    return False, "Image URL field is not a valid Image URL."
            elif item == 'price':
                if not re.match(r'\d+(?:[.]\d{2})?$', data[item]):
                    return False, "Price field is not valid price."
                
        return True, "OK"
                
            





body = Blueprint('body', __name__, static_url_path="/web", static_folder="static/", template_folder="serve/")


@body.route("/")
def Index():
    return body.send_static_file("index.html")



## list templates

@body.route("/list/<name>")
def List(name):
    print(name)
    return render_template("list.html", data={"list":"main"})

@body.route("/list/<name>/submit", methods=["POST"])
def SubmitNew(name):
    try:
        user = "user1"
        data = request.json
        verified, message = Verify.NewItem(data)
        if verified:
            try:
                DB.add_new(user=user, wishlist=name, data=data, date=time.time())
            except Exception:
                return "Unknown Error. View log for more information.", 400
        else:
            return message, 400
    except Exception:
        return "Unknown Error. View log for more information.", 400
















