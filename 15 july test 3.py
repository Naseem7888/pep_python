def disp(main_message):
  """
  program 3: Passing a parameter through the outer function
  """
  def show():
    return main_message

  result = show() + " disp Function"
  return result

print(disp("show Function"))
