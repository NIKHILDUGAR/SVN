from sklearn.externals import joblib
import CheckList
classifier = joblib.load('Model\\logisticReg_final.pkl')
print ("enter url")
url=input()
checkprediction = CheckList.main(url)
x = classifier.predict(checkprediction)
if x == 1:
    print("\n \n This may not be a phishing website !!!!!\n \n ")
else:print("\n \n This may  be a phishing website !!!!!! \n \n ")