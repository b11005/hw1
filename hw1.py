
def anagram(string):
  string=string.lower()
  string=string.strip()
  string=list(string)
  a=sorted(string)
  word=count(a)
  key=word.keys()
  value=word.values()
  num=len(value)
  f=open("/usr/share/dict/words")
  dic=f.read()
  f.close()
  line1=dic.split('\n')
  d={}
  for line in line1:
    line=line.lower()
    string=list(line)
    line2=sorted(string)
    line2="".join(line2)
    d[line]=line2
  d=sorted(d.items(), key=lambda x:len(x[1]), reverse=True)
  for i in d[10:20]:
    result=0
    nums=len(i[0])
    temp=count(i[1])
    for k,v in temp.items():
      if k not in key:
        break
      elif v>word[k]: 
        break
      else: 
        result+=1
    if result<=num:
       return i[0]


def count(word):
  d={}
  for i in range(len(word)):
    d[word[i]]=d.get(word[i],0)+1
  return d


strings="helloworld"
print anagram(strings)
