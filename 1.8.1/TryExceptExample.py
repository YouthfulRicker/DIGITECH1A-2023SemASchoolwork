varOne = "hutt"
try:
  print(varOne)
  try:
    varOne = 1
  except:
    print("Something went wrong when printing")
  finally:
    print('Finally Executed')
except:
  print("Something went wrong with everything")