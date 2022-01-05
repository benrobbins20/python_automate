#!python3
import requests
import os
#response object
ro = requests.get(r'https://automatetheboringstuff.com/files/rj.txt')
#status code
sc = ro.status_code
#print(sc)
text = ro.text
#print(len(text))

###################
badro = requests.get(r'https://automatetheboringstuff.com/files/mj.txt') #does not exists, so return 404
#fouroh = badro.raise_for_status()
#print(fouroh)
print(badro.status_code) #404
###################
#saved text
os.chdir(r'c:/Users/benro/OneDrive/Documents/Python_automate')
st = open('rj_txt.txt','wb')
#for chunk in ro.iter_content(100000):
    #st.write(chunk)







