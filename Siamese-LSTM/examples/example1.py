import subprocess as sp
from lstm import *
sls=lstm("bestsem.p",load=True,training=True)
print "Pre training "
train=pickle.load(open("myTrain2.p",'rb'))
sls.train_lstm(train,150)
#Example
f=open("commands.csv")
line=f.read().splitlines()
sent={}
for x in line:
    c=x.split(",")
    sent[c[1].lower()]=c[0]
tmp = sp.call('clear',shell=True)
print "Model trained"
#print "Enter queries now "
#query=""
#while(query!="exit"):
#    query=raw_input()
#    rules={}
#    for key in sent.keys():
#        n=sls.predict_similarity(query,key)*4.0+1.0
#        rules[str(n)]=key
#    dis=sorted(rules.iterkeys(),reverse=True)
#    for i in range(0,5):
#        print dis[i]+","+rules[dis[i]]
#THEANO_FLAGS=floatX=float32
test=pickle.load(open("myTest.p",'rb'))
acc=0.0
fiveacc=0.0
for query in test:
    rules={}
    for key in sent.keys():
        n=sls.predict_similarity(query[1],key)*4.0+1.0
        rules[str(n)]=key
    dis=sorted(rules.iterkeys(),reverse=True)
    if(sent[rules[dis[0]]]==query[0]):
        acc=acc+1.0
        fiveacc=fiveacc+1.0
    else:
        for i in range(1,5):
            if(sent[rules[dis[i]]]==query[0]):
                fiveacc=fiveacc+1.0

x=acc/(len(test)*1.0)
y=fiveacc/(len(test)*1.0)
print "Accuracy = "+str(x)
print "Top 5 accuracy = "+str(y)











