#Question:: 


# Two dice are thrown at the same time. Find the probability of getting
# (i) same number on both dice.
# (ii) different numbers on both dice.


#Solution:::
#each dice has total of 6 choices when rolled
PA=0 #probability of getting same number on the both dice


PB=0 #Probability of getting different number on the both the dice

NA=0 #number of possiblities for getting same number
NB=0 #number of posiibilities for getting different number

SampleSpace=6**2 # Total possibilites for two dice when they are rolled simultaneously

for firstDice in range(1,7):
    for secondDice in range (1,7):

        if firstDice==secondDice:
            NA=NA+1
        else:
            NB=NB+1

PA=NA/SampleSpace
PB=NB/SampleSpace

print("Probability of getting same number ",PA)
print("Probability of getting different number ",PB)

