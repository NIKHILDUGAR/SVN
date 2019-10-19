'''
Check evil chars in URL
:param url: suspicious URL
:return: result of check and the evil chars
'''
flag=0
url="www.facebook.com"
bad_chars = ['\u0430', '\u03F2', '\u0435', '\u043E', '\u0440', '\u0455', '\u0501', '\u051B', '\u051D']
result = [bad_chars[i] for i in range(len(bad_chars)) if bad_chars[i] in url]
if result:
    flag+=1
print (flag)