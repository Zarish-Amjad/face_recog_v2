#!/usr/bin/python3

#from semantic_text_similarity.models import ClinicalBertSimilarity
import sys
sys.path.insert(0, '/var/www/html/api_orio/.local/lib/python3.8/site-packages')
#print(sys.path)
string1=str(sys.argv[1])
string2=str(sys.argv[2])
string3=str(sys.argv[3])
string4=str(sys.argv[4])

from semantic_text_similarity.models import WebBertSimilarity

web_model = WebBertSimilarity(device='cpu', batch_size=10) #defaults to GPU prediction

#clinical_model = ClinicalBertSimilarity(device='cuda', batch_size=10) #defaults to GPU prediction

res=web_model.predict([(string1,string2), (string3, string4)])
#print(string1)
#print(string2)
print(res[0])
print(res[1])