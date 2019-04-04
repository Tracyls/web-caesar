from flask import Flask, request
from caesar import rotate_string

app=Flask(__name__)

app.config ['DEBUG']=True

form="""       
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px; 
                }}

            textarea {{
                margin: 10px 0;
                width: 540 px;
                height: 120 px;
            }}

        </style>
    </head>
    
    <body>
        <form method='POST'>
        <label><b>Rotate by:<b/></label>
        <input type="text" name="rot" value="0"/><br/><br/>
        <textarea name="text" rows="10" cols="74">{0} </textarea><br/>
        <input type="submit" value="Submit Query"/><br/>
        </form>
    </body>
</html>
"""

@app.route ("/")
def index():
     return form.format('')

@app.route ("/", methods=['POST'])
def encrypt():
    rots= int(request.form['rot'])
    text=request.form ['text']
    return form.format(rotate_string(text,rots))


app.run()      