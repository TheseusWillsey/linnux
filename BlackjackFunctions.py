import random
import PIL
used=[]
hands=[]
Chips=[]
value=[1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10]
def draw(handNum):
	card=random.randint(1,52)
	if card not in used:
		used.append(card)
		hands[handNum].append(card)
	else:
		draw(handNum)
	return
def deal():
	x=0
	for y in hands:
		draw(x)
		draw(x)
		x=x+1
	return
def calcPoints(handNum):#caluclates the point value of the hand.
	Points=0
	Ace=False
	if ((1 in hands[handNum]) or (14 in hands[handNum])or (27 in hands[handNum]) or (40 in hands[handNum])):#if an ace is in the hand
		Ace=True
	for x in hands[handNum]:#total points in hand counting aces as 1
		Points=Points+value[x-1]
	if Ace and Points<=11:#Adjust If ace is worth 11
		Points=Points+10
	if Points>21:#Bust
		Points=-1
	if ((11 in hands[handNum]) or (50 in hands[handNum]))and (Points==21):#Check for BlackJack
		Points=22
	return Points
Num = raw_input("Enter the number of players")
#while Num<1 or Num>6:
	#Num = raw_input("Enter a reasonable the number of players")
Num=int(Num)
Num=Num+1 #insert dealer
while len(hands)< Num:
	hand=[]
	hands.append(hand)
deal()
print "Players hand's:"
for x in hands:
	print x[1]
#print "Player 1 has a score of:"
#print calcPoints(1)
y=1
while y<=Num-1:
	i=raw_input("Player"+str(y)+"'s turn Press Enter to Continue")
	z=0
	print "Your hand:"
	for q in hands[y]:
		print q
	while z==0:
		print "Point value:"
		print calcPoints(y)
		i=raw_input("Enter H to hit and S to stay")
		#while i!=('H'or 'S'or 's'or 'h'):
			#i=raw_input("Enter H to hit and S to stay")
		if i==('h'or 'H'):
			draw(y)
			print "Your hand:"
			for q in hands[y]:
				print q
			if calcPoints(y)==-1:
				print "BUST!"
				z=1
		else:
			z=1
			
	y=y+1
while (calcPoints(0)<17) and (calcPoints(0)!=-1):#Dealer calculations
	print "dealer hits"
	draw(0)
c=0
for x in hands:
	if x==hands[0]:
		print "Dealer's Hand"
	else:
		print "Player "+str(c)+"'s hand"
	print x
	print "Value:"
	if calcPoints(c) ==-1:
		print "Bust!"
	else:
		print calcPoints(c)
	c=c+1
y=0
winners=[0]
while y<=Num-1:
	if calcPoints(y)>calcPoints(winners[0]):
		winners=[y]
	elif calcPoints(y)==calcPoints(winners[0]):
		if winners[0]!=0:
			winners.append(y)
	y=y+1
if len(winners)==1:
	if winners[0]==0:
		print "Dealer Wins"
	else:
		print "Player "+str(winners[0])+" Wins!"
else:
	print "Tie game Between:"
	for w in winners:
		if w==0:
			print "Dealer"
		else:
			print "Player "+str(w)
	
