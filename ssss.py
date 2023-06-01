import time

# getting current time by passing
# the number of seconds since ep
def showtime():
  c = time.localtime()
  curr = time.asctime(c)
  print(curr)
  print(type(curr))
  n = curr.split(" ")
  print(n[4])
  l=n[4].split(":")
  hour=l[0]
  minut=l[1]
  return hour,minut
  
