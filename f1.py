from flask import Flask
from Trial1 import check_EVIL
app = Flask(__name__)

@app.route("/")
def adder_page():
	return '''
		
<html>
<body background="https://engineering.nyu.edu/sites/default/files/styles/content_header_1024_1_5x/public/2018-03/program-cybersecurity-risk-strategy.jpg?h=e1d1bc8a&itok=6ebHHz_7">
  <div class="container">
    <div class="centered">
      <head>
        <b><font font size=24 color="white"><center>Phishing Website Checker</center></font></b></head>
      <p class=”breakAfter”>
        <style>p.breakAfter{margin: 100px; padding: 100px;}</style>
        <center>
          <font font size =5 color="yellow" ><b><style>font{margin: 100px; padding: 100px;}</style>Enter The URL Which You Want To Check For Phishing</b></font>
        </center>
      </p>
      <div class="fieldwrapper">
        <center>
          <input id="field_location" class="field r2" placeholder="Enter URL" id="Postcode" name="URL" type="text" value=""><input type="submit" id="findbutton" value="Submit" />
        </center>
      </div>
</body>
</div>
</div>

</html>


		'''
if __name__ == '__main__':  
	app.run(debug = True)     
