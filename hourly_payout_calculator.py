print ('hello world')
name = input('what is your name?')
print ('hello '+ name)
print('hello',name)

hrs = input("Enter Hours: ")
rate = input("Enter Rate per hour: ")
payout = float(hrs) * float(rate)
print ('Payout would be ' + str(payout) + ' for ' + hrs + ' hours at a rate of ' + rate + ' per hour')