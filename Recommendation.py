def Popular(user):
  s=""+user+".txt"
  f = open(s, "r")

  a=f.read()

  l=a.split("\n")
  tc,ifa,asa,isa,cba,mta,ta,cc,ca,sa=0,0,0,0,0,0,0,0,0,0

  for i in l:
    a=i.split()
    s=""+a[0]+" "+a[1]
    if(s=="transaction count" ):
      tc+=1
    if(s=="transaction amount" ):
      ta+=1
    if(s=="cashback count" ):
      cc+=1
    if(s=="cashback amount" ):
      ca+=1
    if(s=="merchant transaction"):
      mta+=1
    if(s=="cardholder billing" ):
      cba+=1
    if(s=="issuer settlement" ):
      isa+=1
    if(s=="surcharge amount" ):
      sa+=1
    if(s=="acquirer settlement"):
      asa+=1
    if(s=="issuer fee"):
      ifa+=1
    

  tc,ta,sa,cc,ca,mta,ifa,cba,isa,asa=tc*5/len(l),ta*5/len(l),sa*5/len(l),cc*5/len(l),ca*5/len(l),mta*5/len(l),ifa*5/len(l),cba*5/len(l),isa*5/len(l),asa*5/len(l)


  ratings={"Transaction Count":tc,
           "Transaction Amount":ta,
           "Surcharge Amount":sa,
           "Cashback Count":cc,
           "Cashback Amount":ca,
           "Merchant Transaction Amount":mta,
           "Issuer Fee Amount":ifa,
           "Cardholder Billing Amount":cba,
           "Issuer Settlement Amount":isa,
           "Acquirer Settlement Amount":asa}

  
  
  sorted(ratings.items(), key=lambda x: x[1], reverse=True)
  print(list(ratings)[0])
  
  dictionary={"First_Popular":list(ratings)[0],
              "Second_Popular":list(ratings)[1],
              "Third_Popular":list(ratings)[2]
              }
  
  

  return dictionary
def RecommendNext(user,currmsg):

  s=""+user+".txt"
  f = open(s, "r")

  a=f.read()

  l=a.split("\n")
  tc,ifa,asa,isa,cba,mta,ta,cc,ca,sa=0,0,0,0,0,0,0,0,0,0

  for i in l:
    a=i.split()
    s=""+a[0]+" "+a[1]
    if(s=="transaction count" and currmsg!=tc):
      tc+=1
    if(s=="transaction amount" and currmsg!=ta):
      ta+=1
    if(s=="cashback count" and currmsg!=cc):
      cc+=1
    if(s=="cashback amount" and currmsg!=ca):
      ca+=1
    if(s=="merchant transaction" and currmsg!=mta):
      mta+=1
    if(s=="cardholder billing" and currmsg!=cba):
      cba+=1
    if(s=="issuer settlement" and currmsg!=isa):
      isa+=1
    if(s=="surcharge amount" and currmsg!=sa):
      sa+=1
    if(s=="acquirer settlement" and currmsg!=asa):
      asa+=1
    if(s=="issuer fee" and currmsg!=ifa):
      ifa+=1
    

  tc,ta,sa,cc,ca,mta,ifa,cba,isa,asa=tc*5/len(l),ta*5/len(l),sa*5/len(l),cc*5/len(l),ca*5/len(l),mta*5/len(l),ifa*5/len(l),cba*5/len(l),isa*5/len(l),asa*5/len(l)


  ratings={"Transaction Count":tc,
           "Transaction Amount":ta,
           "Surcharge Amount":sa,
           "Cashback Count":cc,
           "Cashback Amount":ca,
           "Merchant Transaction Amount":mta,
           "Issuer Fee Amount":ifa,
           "Cardholder Billing Amount":cba,
           "Issuer Settlement Amount":isa,
           "Acquirer Settlement Amount":asa}

  
  
  sorted(ratings.items(), key=lambda x: x[1], reverse=True)
  print(list(ratings)[0])
  
  dictionary={"First_Recommended":list(ratings)[0],
              "Second_Recommended":list(ratings)[1]
              }
  #print(dictionary)
  

  return dictionary

def write(user,msg):
  s=""+user+".txt"
  file=open(s,"a")
  writer=" \n"+msg
  file.write(writer)
  file.close()



RecommendNext("akash","cc")

Popular("akash")

write("akash","transaction amount alfa bank july 2020")