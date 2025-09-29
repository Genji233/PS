regular_price = 3.49
discout = 0.6
discounted_price = round(regular_price*(1-discout),2)
inventory = 50
k = True
while k == True :
    N = input('How many loaves of day old bread do you want? Please enter:')
    if N.isdigit() :
        number = int(N)
    else :
        print('Please enter an integer! Try again.')
        continue
    if number >50:
        print('Sorry,we only have',inventory,'loaves left.Please enter again.')
    elif number==0 :
        print('Goodbye.')
        exit(0)
    else :
        break
total_price =round(number*discounted_price,2)
print('Regular price is',regular_price,'£.\n'+
      'Discount rate is',discout*100,'%.\n'
      'Discounted price is',discounted_price,'£.\n'
      'You wanted',number,'of them.\n'+
      'Total price is',total_price,'£,thank you.'
      )
