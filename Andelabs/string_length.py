def string_length(x):
  a = []
  if isinstance(x, str):
    a.append(len(x))
  else:
    for i in x:
      a.append(len(i))
  return a
    
