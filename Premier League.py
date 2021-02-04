

PremierLeagueName=['Man City', 'Man United', 'Leicester City', 'Liverpool', 'West Ham', 'Everton', 'Tottenham', 'Chelsea', 'Aston Villa', 'Arsenal', 'Leeds United', 'Southampton', 'Crystal Palace', 'Wolves', 'Brighton', 'Newcastle', 'Burnley', 'Fulham', 'West Brom', 'Sheffield United']
PremierLeaguePoints=[47,44,42,40,38,36,33,33,32,31,29,29,29,26,24,22,22,14,12,11]
PremierLeagueRank=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print('What Premier League team occupies the ranking you will input?')
x = int(input('Ranking: '))
ibis = int(int(x)-1)

print('The team that is of ranking '+ str(x)+ ' is '+PremierLeagueName[ibis]+' and they have ' + str(PremierLeaguePoints[int(ibis)])+ ' points.')
    
def new_list(z):
    new = []
    for item in range(len(z)):
        if PremierLeagueRank[item] < int(x):
            new.append(PremierLeagueName[item])
    return new if int(x) > 1 else print('Already top team! ') 

print('Do you want to know, in the top 5, who is above '+PremierLeagueName[int(x-1)]+' ? Reply with YES or NO.')
answer = input('Enter YES or NO: ')
if answer =='YES':
        print(new_list(PremierLeagueName))
elif x == int(1):
    print('Man City is the top team of the Premier League! No one above it. ')
elif answer == 'NO':
        print('Alright!')
else:
    print('Please enter YES or NO. ')

