def anagram(string):
  string=string.lower()
  string=string.translate(None," ")
  string=list(string)
  a=sorted(string)
  word=count(a)
  print word
  key=word.keys()
  value=word.values()
  num=len(value)
  f=open("/usr/share/dict/words")
  dic=f.read()
  f.close()
  line1=dic.split('\n')
  d={}
  for line in line1:
    if len(line)>16:
      del line
      continue
    str=line.lower()
    str=list(str)
    line2=sorted(str)
    line2="".join(line2)
    d[line]=line2
  d=sorted(d.items(), key=lambda x:len(x[1]), reverse=True)
  for i in d:
    result={}
    nums=len(i[0])
    temp=count(i[1])
    total=0
    for k,v in temp.items():
      if k not in key:
        result[k]=result.get(k,0)+1
        break
      elif v>word[k]:
        result[k]=result.get(k,0)+1
        break
      else: 
        result[k]=result.get(k,0)
    for f,g in result.items():
      if f not in key:
        total=-100
        break
      elif g==1:
        total=-10
        break
      else: total+=1
    if total<=nums and total>0:
      print count(i[0])
      return i[0]
      break



def count(word):
  d={}
  for i in range(len(word)):
    d[word[i]]=d.get(word[i],0)+1
  return d

def gen_ran_str(chars=None):
  import random
  import string
  if chars==None: 
    chars = string.lowercase
  return ''.join([random.choice(chars) for i in range(16)]) 
  
strings=gen_ran_str()
print strings
print anagram(strings)
