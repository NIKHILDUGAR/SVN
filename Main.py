from sklearn.externals import joblib
import CheckList
classifier = joblib.load('/root/Hackcbs/SVN/Model/logisticReg_final.pkl')
def getr(url):
    checkprediction = CheckList.main(url)
    x = classifier.predict(checkprediction)
    flag=0
    if x == 1:
        '''
        Check evil chars in URL
        :param url: suspicious URL
        :return: result of check and the evil chars
        '''
        flag+=1
        bad_chars = ['\u0430', '\u03F2', '\u0435', '\u043E', '\u0440', '\u0455', '\u0501', '\u051B', '\u051D']
        result = [bad_chars[i] for i in range(len(bad_chars)) if bad_chars[i] in url]
        if result:
            flag+=1
    if flag==1:
        msg="Not Phishing"
        return msg
    else:
        msg="Phishing"
        return msg
