""" This buffer is for notes you don't want to save, and for Lisp evaluation.
 If you want to create a file, visit that file with C-x C-f,
 then enter the text in that file's own buffer."""

def anagram(strings):
  strings=strings.lower()
  strings=list(strings)
  a=sorted(strings)
  b=len(strings)
  f=open("/usr/share/dict/words")
  dic=f.read()
  f.close()
  line1=dic.split('\n')
  d={}
  dic={}
  for line in line1[:5]:
    line=line.lower()
    name=list(line)
    line2=sorted(name)
    line2="".join(line2)
    d[line]=line2
    for i in range(len(line2)):
      dic.setdefault(line2[i],0)
      dic[line2[i]]+=1
  print d
  print dic

strings="Hello"  
print anagram(strings)
