# -*- coding: utf-8 -*-
import math
import codecs

d={}
log = lambda x: float('-inf') if not x else math.log(x)
#prob = lambda x: d[x] if x in d else 0 if len(x)>1 else 1

def prob(x):
    if x in d:
        return d[x]
    elif len(x)>3:#每个汉字的长度为3,编码问题
        return 0
    else:
        return 1

def init(filename='people.dic'):
    d['_t_'] = 0.0
    with open(filename, 'r') as handle:
        for line in handle:
            word, freq = line.split('\t')[0:2]
            d['_t_'] += int(freq)+1#单词总频度
            try:
                d[word] = int(freq)+1#每个单词的频度，+1平滑
           #     print word, d[word], freq
            except:
                d[word] = int(freq)+1
 
def solve(s):
    l = len(s)
    p = [0 for i in range(l+1)]
    t = [0 for i in range(l)]
    for i in xrange(l-1, -1, -1):
        #for k in xrange(1, l-i+1):
       # if s[i:i+2].encode('utf-8') in d:
        #    print 'word is in dic'
        #else:
         #   print 'word not in dic'

#        print s[i:i+2],prob(s[i:i+2])
        p[i], t[i]  = max((log(prob(s[i:i+k].encode('utf-8'))/d['_t_'])+p[i+k], k)
                          for k in xrange(1, l-i+1))
       # print i,p[i], t[i], s[i:i+t[i]], s[0:1], len(s[0:1].encode('utf-')), log(prob(s[0:1].encode('utf-8'))/d['_t_']), p[1]#+p[1]
    while p[l]<l:
        yield s[p[l]:p[l]+t[p[l]]]
        p[l] += t[p[l]]
 
if __name__ == '__main__':
    init()
    with open('new_test','r') as handle:
        output_file = codecs.open('new_result','w','utf-8')
        for line in handle:
            s=line
            s = s.decode('utf-8')
            #print ' '.join(list(solve(s)))
            output_file.write(' '.join(list(solve(s))))