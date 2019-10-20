from flask import Flask,request
import os
import Main

app = Flask(__name__)

inputs=""

@app.route("/",methods=["GET","POST"])
def adder_page():
    if request.method == "POST":
        inputs=str(request.form["URL"])
        if request.form["action"] == "Submit":
            result = Main.getr(inputs)
            inputs=""
            return '''
                <html>
                    <body background="https://engineering.nyu.edu/sites/default/files/styles/content_header_1024_1_5x/public/2018-03/program-cybersecurity-risk-strategy.jpg?h=e1d1bc8a&itok=6ebHHz_7">
                        <p class=”breakAfter”>
            
            <center>
            <font font size =5 color="yellow" ><b>{result}</b></font>
            </center>
        </p>
         <p class=”breakAfter2”>
           
            <center>
            <font font size =5 color="yellow" ><b><a href = "/">Click here to check again</a></b></font>
            </center>
                    </body>
                </html>
            '''.format(result=result)
        
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
        <form method="post" action=".">
        <div class="fieldwrapper">
            <center>
            <input id="field_location" class="field r2" placeholder="Enter URL" id="Postcode" name="URL" type="text" value="">
            <input type="submit" id="findbutton" name="action" value="Submit" />
            
            </center>
        </div>


    </body>
    </div>
    </div>

    </html>
         '''
	
if __name__ == '__main__':  
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)   
