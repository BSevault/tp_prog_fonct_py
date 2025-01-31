def get_float_input(prompt, non_null=False):
  while True:
    try:
      result = float(input(prompt))
      if non_null and result == 0:
        print("Null number")
      else:
        return result
    except ValueError:
      print("Not a number")

a = get_float_input("Enter number 1: ")
b = get_float_input("Enter non-null number 2: ", non_null=True)

print(f"{a} / {b} = {a/b:.6f}")