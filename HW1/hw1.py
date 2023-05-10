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
dice1={}
dice2={}
for i in range(1,7):
    if i in dice1:
        dice1[i]=dice1[i]+1
    else:
        dice1[i]=1
    if i in dice2:
        dice2[i]=dice2[i]+1
    else:
        dice2[i]=1

for key in dice1:
    if key in dice2:
        NA=NA+dice1[key]*dice2[key]
PA=NA/SampleSpace

PB=(len(dice1)*len(dice2)-NA)/SampleSpace #NB can be calculate total number of possibilities -possible outcomes for Event A as they were mutually exclusive



print("Probability of getting same number ",PA)
print("Probability of getting different number ",PB)


