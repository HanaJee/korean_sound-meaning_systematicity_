import pandas as pd
import textdistance as txt
import os
from scipy.spatial.distance import euclidean

os.chdir(r'C:\Users\pc\OneDrive - University of Edinburgh\0. PhD_Psyhology\0. Experiment\0. The 3rd Year\1. Experiment & Data\0. Korean_Sound_Meaning\2. ReConducted_more samples')

ㅂ	=	[	0,	0,	1,	0,	0,	0,	0,	1,	0,	0,	0,	1,	0,	0,	0,	0	]
ㅃ	=	[	0,	0,	1,	0,	0,	0,	0,	1,	0,	0,	1,	0,	0,	0,	0,	0	]
ㄷ	=	[	0,	0,	0,	0,	0,	1,	0,	1,	0,	0,	0,	1,	0,	0,	0,	0	]
ㄸ	=	[	0,	0,	0,	0,	0,	1,	0,	1,	0,	0,	1,	0,	0,	0,	0,	0	]
ㄱ	=	[	0,	1,	0,	0,	0,	0,	0,	1,	0,	0,	0,	1,	0,	0,	0,	0	]
ㄲ	=	[	0,	1,	0,	0,	0,	0,	0,	1,	0,	0,	1,	0,	0,	0,	0,	0	]
ㅅ	=	[	0,	0,	0,	1,	0,	0,	0,	0,	0,	1,	0,	1,	0,	0,	0,	0	]
ㅊ	=	[	1,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	1,	0,	0,	0	]
ㅎ	=	[	0,	0,	0,	0,	0,	0,	1,	0,	0,	1,	0,	0,	0,	0,	0,	0	]
ㅁ	=	[	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0	]
ㄴ	=	[	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0	]
ㅇ	=	[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0	]
ng	=	[	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0	]
ㄹ	=	[	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0	]
ㅍ	=	[	0,	0,	1,	0,	0,	0,	0,	1,	0,	0,	0,	0,	1,	0,	0,	0	]
ㅌ	=	[	0,	0,	0,	0,	0,	1,	0,	1,	0,	0,	0,	0,	1,	0,	0,	0	]
ㅋ	=	[	0,	1,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0,	1,	0,	0,	0	]
ㅆ	=	[	0,	0,	0,	1,	0,	0,	0,	0,	0,	1,	1,	0,	0,	0,	0,	0	]
ㅈ	=	[	1,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	1,	0,	0,	0,	0	]
ㅉ	=	[	1,	0,	0,	0,	0,	0,	0,	0,	1,	0,	1,	0,	0,	0,	0,	0	]
emp	=	[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0	]

ㅏ	=	[	0,	1,	0,	0,	0,	1,	0,	1,	0,	0,	0,	0,	]
ㅔ	=	[	1,	0,	0,	0,	1,	0,	0,	1,	0,	0,	0,	0,	]
ㅣ	=	[	1,	0,	0,	1,	0,	0,	0,	1,	0,	0,	0,	0,	]
ㅗ	=	[	0,	0,	1,	0,	1,	0,	1,	0,	0,	0,	0,	0,	]
ㅜ	=	[	0,	0,	1,	1,	0,	0,	1,	0,	0,	0,	0,	0,	]
ㅑ	=	[	0,	1,	0,	0,	0,	1,	0,	1,	1,	0,	0,	1,	]
ㅒ	=	[	1,	0,	0,	0,	0,	1,	0,	1,	1,	0,	0,	1,	]
ㅖ	=	[	1,	0,	0,	0,	1,	0,	0,	1,	1,	0,	0,	1,	]
ㅛ	=	[	0,	0,	1,	0,	1,	0,	1,	0,	1,	0,	0,	1,	]
ㅠ	=	[	0,	0,	1,	1,	0,	0,	1,	0,	1,	0,	0,	1,	]
ㅘ	=	[	0,	1,	0,	0,	0,	1,	0,	1,	1,	0,	1,	0,	]
ㅟ	=	[	1,	0,	0,	1,	0,	0,	1,	0,	0,	0,	0,	0,	]
ㅞ	=	[	1,	0,	0,	0,	1,	0,	0,	1,	1,	0,	1,	0,	]
ㅓ	=	[	0,	0,	1,	0,	1,	0,	0,	1,	0,	0,	0,	0,	]
ㅐ	=	[	1,	0,	0,	0,	0,	1,	0,	1,	0,	0,	0,	0,	]
ㅕ	=	[	0,	0,	1,	0,	1,	0,	0,	1,	1,	0,	0,	1,	]
ㅚ	=	[	1,	0,	0,	0,	1,	0,	1,	0,	0,	0,	0,	0,	]
ㅙ	=	[	1,	0,	0,	0,	0,	1,	0,	1,	1,	0,	1,	0,	]
ㅝ	=	[	0,	0,	1,	0,	1,	0,	0,	1,	1,	0,	1,	0,	]
ㅡ	=	[	0,	0,	1,	1,	0,	0,	0,	1,	0,	0,	0,	0,	]
ㅢ	=	[	1,	0,	0,	1,	0,	0,	0,	1,	1,	1,	0,	0,	]



#def dist(a,b):
#    return edit_distance(a,b)
#
#def euclid(x,y):   
#    return np.sqrt(np.sum((x-y)**2))

#####################################3
f = pd.read_excel('Phono4.xlsx')
Cho1 = f['Cho'].tolist()
Jung1 = f['Jun'].tolist()
Jong1= f['Fin'].tolist()
Cho2 = f['Cho2'].tolist()
Jung2 = f['Jun2'].tolist()
Jong2 = f['Fin2'].tolist()

Edit_d = []
Euclid_d = []
Cosine_d = []
Jaccard_d = []
 
i=0
while True:
    w1 = eval(Jong1[i])
    w2 = eval(Jong2[i])
    
    leven = txt.levenshtein(w1,w2)
    euclid = euclidean(w1,w2)
    cosine = txt.cosine(w1,w2)
    jaccard = txt.jaccard(w1,w2)
        
    Edit_d.append(leven)
    Euclid_d.append(euclid)
    Cosine_d.append(cosine)
    Jaccard_d.append(jaccard)
    
    i += 1
    if i == len(Jong1):
        break  
        
f['Edit3'] = Edit_d
f['Euclid3'] = Euclid_d
f['Cosine3'] = Cosine_d
f['Jaccard3'] = Jaccard_d


f.to_excel('Phono_Final.xlsx', engine = 'xlsxwriter')

