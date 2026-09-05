from pyscript import display, document

def addition():
    document.getElementById('result').innerHTML = ""

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    sum = first_number + second_number

    display(f'The sum of {first_number} and {second_number} equals to {sum}.', target='result')


def subtraction():
    document.getElementById('result').innerHTML = ""

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    difference = first_number - second_number

    display(f'The difference of {first_number} and {second_number} equals to {difference}.', target='result')


def multiplication():
    document.getElementById('result').innerHTML = ""

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    product = first_number * second_number

    display(f'The product of {first_number} and {second_number} equals to {product}.', target='result')


def exponentiation():
    document.getElementById('result').innerHTML = ""

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    power = first_number ** second_number

    display(f'The power of {first_number} when raised to {second_number} is equal to {power}.', target='result')


def division():
    document.getElementById('result').innerHTML = ""

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    quotient = first_number / second_number

    display(f'The quotient of {first_number} when divided by {second_number} is equal to {quotient}.', target='result')


def floor_division():
    document.getElementById('result').innerHTML = ""

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    quotient_from_floor_division = first_number // second_number

    display(f'The quotient of {first_number} when divided by {second_number} is equal to {quotient_from_floor_division}.', target='result')


def get_remainder():
    document.getElementById('result').innerHTML = ""

    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)

    modulo = first_number % second_number

    display(f'The remainder of {first_number} when divided by {second_number} is equal to {modulo}.', target='result')