
def hackerNewsFunction(rating, time):

  hot = rating / (( time + 1000 )**1.02)

  return hot
