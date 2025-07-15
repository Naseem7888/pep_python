def disp():
  """
  program 1: No parameters in the outer function
  """
  def show(message):
    return message
  
  result = show("show Function") + " disp Function"
  return result

print(disp())
