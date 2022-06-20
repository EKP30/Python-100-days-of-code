logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
keep_running = "n"
while keep_running == "n":
  print(logo)
  num1 = float(input("What's the first number?: "))
  for operation in operations:
    print(operation)
  operation_choice = input("Pick an operation from the lines above: ")
  num2 = float(input("What's the second number?: "))
  
  operation_function = operations[operation_choice]
  answer = operation_function(num1, num2)
  print(f"The answer is: {answer}")
  keep_running = input(f"Would you like to keep calculating with {answer}, or start a new calculation? \n Type 'y' or 'n'. ").lower()
  while keep_running == "y":
    for operation in operations:
      print(operation)
    operation_choice = input("Pick an operation from the lines above: ")
    num2 = float(input("What's the second number?: "))
    
    operation_function = operations[operation_choice]
    answer = operation_function(answer, num2)
    print(f"The answer is: {answer}")
    keep_running = input(f"Would you like to keep calculating with {answer}, or start a new calculation? \n Type 'y' or 'n'. ").lower()