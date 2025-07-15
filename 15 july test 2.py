def disp(greeting_part):
  """
  program 2: Using a parameter in the inner function
  """
  def show(message):
    return message
  
  result = show(greeting_part) + " disp Function"
  return result

print(disp("show Function"))
