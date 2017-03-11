st=[]
for _ in range(int(raw_input())):
	name = raw_input()
	score = float(raw_input())
	st.append([name,score])
    
#scorelist = [score for each in st for score in each[1:]]
second_lowest = sorted(set([score for each in st for score in each[1:]]))[1]
losers = [each[0] for each in st if each[1]==second_lowest]

for each in sorted(losers): #prinitng names alphabetically
	print each

