varOne = "hutt"
try:
  print(varOne)
  try: #try does the program
    varOne = 1
  except: #except is a failure message
    print("Something went wrong when printing")
  else: #else is a success story
    print('You are oddly competent!')
  finally: #finally will happen regardless of anything
    print('Finally Executed')
except:
  print("Something went wrong with everything")