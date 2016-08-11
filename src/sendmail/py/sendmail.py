import web
def sendmail(to_mail=r"511547297@qq.com"):
    try:
        web.config.smtp_server = 'smtp.163.com'
        web.config.smtp_port = 25
        web.config.smtp_username = 'lhq0631@163.com'
        web.config.smtp_password = 'ivu@1001621'
        web.config.smtp_starttls = True
        send_from = r'lhq0631@163.com'
        subject = 'Reset password'
        message = '''reset password:
                     http://localhost:8080/resetpassword'''
        web.sendmail(send_from, to_mail, subject, message)
    except Exception, e:
        print e
        return -1
    
sendmail()
print "Done"