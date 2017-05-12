from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/request_counter', methods=['GET', 'POST', 'PUT', 'DELETE'])
def request_counter():
    counter[request.method] += 1
    content = ''
    for item in counter:
        content += item + ': ' + str(counter[item]) + '\n'
    with open('request_counts.txt', 'w') as file:
        file.write(content)
    return redirect('/')


@app.route('/statistics')
def statistics():
    return render_template('statistics.html', counter=counter)


if __name__ == '__main__':
    with open('request_counts.txt', 'r') as file:
        lines = file.readlines()
        counter = {}
        for item in lines:
            row = item.replace('\n', '').split(': ')
            counter[row[0]] = int(row[1])
    app.run(debug=True)
