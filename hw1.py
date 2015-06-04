def anagram(string):
  string=string.lower()
  string=string.strip()
  string=list(string)
  a=sorted(string)
  word=count(a)
  print word
  key=word.keys()
  value=word.values()
  f=open("/usr/share/dict/words")
  dic=f.read()
  f.close()
  line1=dic.split('\n')
  d={}
  result=[]
  for line in line1:
    line=line.lower()
    string=list(line)
    line2=sorted(string)
    line2="".join(line2)
    d[line]=line2
  d=sorted(d.items(), key=len, reverse=True)
  for i in d:
    temp=count(i[1])
    print temp
    for k,v in temp.items():
      if key==k and value>=v:
        return k

 





def count(word):
  d={}
  for i in range(len(word)):
    d[word[i]]=d.get(word[i],0)+1
  return d

def number(word):
  return len(word)

strings="Helloworld"
print anagram(strings)
