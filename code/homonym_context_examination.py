import re
import os

os.chdir(r'C:\Users\pc\OneDrive - University of Edinburgh\New folder\Coding\My_Code_Corpus\2. Nate_Pann_Corpus\Corpus_Nate_Pann')

f=open(r'final_corpus.txt','r',encoding='utf-8').read()
d = re.findall(r'((?:\S+\s+){0,3}\b금\b\s*(?:\S+\s+){0,3})',f)
print(d)



l=['편','폭','각','간','갑','강','건','곡','과','구','국','군','권','귤','급','남','뇌','답','댁','도','면','명','목','무','문','미','반','방','백','번','법','벽','병','복','본','부','북','분','사','산','삼','상','색','생','석','선','속','수','시','식','십','암','약','양','여','역','열','영','오','왕','외','욕','용','운','원','월','육','은','음','인','잔','장','적','전','점','정','조','종','죄','주','죽','즉','질','차','창','책','총','층','칠','탑','평','표','하','핵','향','현','형','호','화','회','후']

m=[]
for i in l:
    code=r'((?:\S+\s+){0,3}\b'+i+r'\b\s*(?:\S+\s+){0,3})'
    d=re.findall(code,f)
    m.append(d)
    
with open('homonyms2.txt', 'w', encoding='utf-8') as filehandle:
   for j in m:
        filehandle.write('%s\n' % j)   
    
    
f1=open(r'homonyms.txt','r',encoding='utf-8').read()
print(f1)
