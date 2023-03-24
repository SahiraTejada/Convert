from flask import Blueprint, render_template, request, redirect, url_for
views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html")


@views.route('/convert', methods=['POST', 'GET'])
def calculate_decimal():
    bmi = ''
    if request.method == 'POST' and 'convert' in request.form:
        a = request.form.get('convert')
        table = {'0': 0, '1': 1, '2': 2, '3': 3,
                '4': 4, '5': 5, '6': 6, '7': 7,
                '8': 8, '9': 9, 'A': 10, 'B': 11,
                'C': 12, 'D': 13, 'E': 14, 'F': 15}

        hexadecimal = a.strip().upper()
        res = 0

# computing max power value
        size = len(hexadecimal) - 1

        for num in hexadecimal:
            res = res + table[num]*16**size
            size = size - 1
        bmi= res
    return render_template('Convert.html', bmi=bmi)


@views.route("/back")
def back():
    return redirect(url_for("views.home"))

"""
@views.route('/ascii', methods=['POST', 'GET'])
def calculate():
    bmi = ''
    if request.method == 'POST' and 'ascii' in request.form:
        string = request.form.get('ascii')
        a = string.replace(" ", "")
        length = len(a)
        num = 0
        for i in range(length):

            # Append the current digit
            num = num * 10 + (ord(string[i]) -
                              ord('0'))

        # If num is within the required range
            if (num >= 32 and num <= 122):
                bmi = chr(num)
                num = 0
    return render_template('ASCII.html', bmi=bmi)
"""

@views.route('/character', methods=['POST', 'GET'])
def calculate_character():
    bmi = ''
    if request.method == 'POST' and 'character' in request.form:
        a = request.form.get('character')
        bmi = ''.join(str(ord(c)) for c in a)
    return render_template('Character.html', bmi=bmi)


@views.route('/ascii', methods=['POST', 'GET'])
def calculate():
    bmi = ''
    if request.method == 'POST' and 'ascii' in request.form:
        string = request.form.get('ascii')
        length = len(string)
        num = 0
        for i in range(length):

            # Append the current digit
            num = num * 10 + (ord(string[i]) -
                              ord('0'))

        # If num is within the required range
            if (num >= 32 and num <= 122):
                bmi = chr(num)
                num = 0
    return render_template('ASCII.html', bmi=bmi)

