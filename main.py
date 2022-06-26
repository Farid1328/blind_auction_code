from replit import clear
import blindauction
print('Welcome to blind auction')
print(blindauction.logo)
blind = {}
while True:
  name = input('Enter Your name? ') 
  bid = int(input('Enter Your bid '))
  blind.update({name:bid})
  other = input('Is the any other bidders')
  if other == 'yes':
    
    continue
  else:
    x = 0
    for value in blind:
      if blind[value] > x:
        x = blind[value]
    print('the higts bid',x)
    break
       
        
  
    




