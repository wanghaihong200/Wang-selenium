#coding:utf-8
login_bussiness_url = "http://localhost:8081/business/login.html"


class LoginBussinessPage():
    #定位器，定位页面元素
    username_loc = ("name", "username")
    password_loc = ("name", "password")
    submit_loc = ("tag name", "button")
    base_url = login_bussiness_url

