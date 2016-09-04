#ran out of time, but basically need to finish creating the dictionary so that it would hold multiple values and support the bi-directionality of the friendships
#EMPLOYEES
employees = {}       
infile = open('employees.csv')    

for line in infile:       
    line = line.strip()    
    num, first, department = line.split(',')     
    employees[int(num)] = { 'num':num, 'first':first, 'department':department }

#FRIENDSHIPS
friendships = {}       
infile = open('friendships.csv')    

for line in infile:       
    line = line.strip()    
    f1, f2 = line.split(',') 
    if int(f1) in friendships.keys():
      friendships[f1].append(f2)
    else:
      friendships[f1] = f2

#PRINTING
#would need to fix range for larger set of data, can't always assume a range
for index in range (1,7):    
#wrong, will print none for all 
  try:
    value = employees[index]
    try:
      value = friendships[index]
      #print employees[index]['num'] + ": " + friendships[index]['f2']
      print friendships[index]
    except KeyError:
      print employees[index]['num'] + ": None"
  except KeyError:
    pass
