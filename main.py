from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/request_counter', methods=['GET', 'POST'])
def request_counter():
    counter[request.method] += 1
    print(counter)
    return redirect('/')


@app.route('/statistics')
def statistics():
    return render_template('statistics.html', counter=counter)


if __name__ == '__main__':
    counter = {'GET': 0, 'POST': 0, 'DELETE': 0, 'PUT': 0}
    app.run(debug=True)
