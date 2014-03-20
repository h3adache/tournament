import random
from math import sqrt

num_teams = 16 # change this to 4 to play Final Four and Championship

win_rates = {};

def add_win_rate(rank1, wins) :
	for rank2, rate in enumerate(wins) :
		rank2 += 1
		win_rates[(rank1 * 100) + rank2] = rate
		win_rates[(rank2 * 100) + rank1] = 100 - rate

def play(rank1, rank2) :
	game = (rank1 * 100) + rank2;
	return rank1 if win_rates[game] > (random.random() * 100) else rank2

competitors = range(1,num_teams+1)

# historical win rates from 2013
add_win_rate(1, [50,54.5,59.4,67.2,82.6,66.7,100,81.1,89.9,100,40,100,100,0,0,100])
add_win_rate(2, [45.5,50,61,44.4,20,70.6,74.4,57.1,50,59.6,91.7,100,0,0,94,0])
add_win_rate(3, [40.6,39,50,62.5,50,54.3,66.7,100,100,69.2,72.1,0,0,85.3,100,0])
add_win_rate(4, [32.8,55.6,37.5,50,55.4,33.3,66.7,25,66.7,100,0,63.6,78.4,0,0,0])
add_win_rate(5, [17.4,80,50,44.6,50,100,0,25,33,100,0,67.6,78.6,0,0,0])
add_win_rate(6, [33.3,29.4,45.7,66.7,0,0,57.1,25,0,60,66.9,0,0,85.7,0,0])
add_win_rate(7, [0,25.6,33.3,33.3,0,42.9,0,0,0,60,0,0,0,100,66.7,0])
add_win_rate(8, [18.9,42.9,0,75,75,75,100,0,51.4,0,100,0,100,0,0,0])

for round in range(int(sqrt(num_teams))):
	survivors = []
	print "round",(round+1),"-- remaining competitors", competitors
	
	while len(competitors) > 1 :
		rank1 = competitors[0]
		rank2 = competitors[-1]		
		winner = play(rank1, rank2)

		competitors.remove(rank1)
		competitors.remove(rank2)
		
		print "playing", rank1, "vs", rank2, "-- winner", winner
		survivors.append(winner)
	
	competitors = survivors


