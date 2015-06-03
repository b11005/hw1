""" This buffer is for notes you don't want to save, and for Lisp evaluation.
 If you want to create a file, visit that file with C-x C-f,
 then enter the text in that file's own buffer."""

def anagram(strings):
  strings=strings.lower()
  strings=list(strings)
  a=sorted(strings)
  word=count(a)
  f=open("/usr/share/dict/words")
  dic=f.read()
  f.close()
  line1=dic.split('\n')
  d={}
  print line1[5:10]
  for line in line1[5:10]:
    line=line.lower()
    name=list(line)
    line2=sorted(name)
    line2="".join(line2)
    d[line]=line2
  long=sorted(d.items(), key=lambda x:len(line[1]), reverse=True) 
  print long

def count(word):
  d={}
  for i in range(len(word)):
    d.setdefault(word[i],0)
    d[word[i]]+=1
  return d



strings="Hello"  
print anagram(strings)
