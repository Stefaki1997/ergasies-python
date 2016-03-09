flag1 = 0 #gia th prwth fora poy paizei o prwtos
flag2 = 0 #gia th prwth fora poy paizei o deyteros
flag = 0 #otan ginei ena 1 tote exoume nikhth
flag4 = 0 #metrhths
turn = 1 #deixnei poios paizei

print "\n\t", a[0], "|", a[1], "|", a[2]
print "\t", "---------------------------"
print "\n\t", a[3], "|", a[4], "|", a[5]
print "\t", "---------------------------"
print "\n\t", a[6], "|", a[7], "|", a[8]

hand1=['SB1','SB2','MB1','MB2','LB1','LB2']
hand2=['SR1','SR2','MR1','MR2','LR1','LR2']

for i in range(8)
     array[i] = 0

while (flag == 0)
     if (turn%2 != 0 ) & (turn == 1)
	     print "The first player plays "
		 pawn = raw_input("Choose: Size S<M<L,Color B, Number 1,2")
		 while ( flag1 ==0 )
		     for i in range (5)
			     if ( hand1[i] == pawn )
				     hand1[i] = 0
					 flag1 = 1
		 x = raw_input ("Give a number from 0 to 8 to place the pawn")
		 array [x] = pawn
         turn = turn + 1
		 
	 if ( turn%2 == 0 ) & ( turn == 2 )
	     print "The second player plays"
		 pawn = raw_input ("Choose: Size S<M<L,Color R, Number 1,2")
		 while (flag2 == 0)
		     for i in range (5)
			     if ( hand2[i] == pawn )
                     hand2[i] = 0
					 flag2 = 1
         while ( flag4 == 0)		
		     x=raw_input ("Give a number from 0 to 8 to place the pawn")
		     if ( array[x] == 0 )
		         array[x] = pawn
				 flag4 = 1
		     else
		         for i in range (8)
			         S[i] = array[i]
			     for i in range (8)
			         if S[i] == array[x]
				         temp = S[i]
			     if temp[0] == pawn[0]
			        print "You cannot move to this place, pick another one because you have the same size"
			     if temp[0] == 'L'
			         print "You cannot move to this place, pick another one because there is a large pawn here"
			     if temp[0] == 'S' & pawn[0] == 'M'
			          print "Good move! you gobblet a smaller one!"
					  flag4 = 1
					  array[x] = pawn
			     if temp[0] == 'M' & pawn[0] == 'S'
			         print "You cannot move to this place, pick another one because there is a medium pawn here"
				 if temp[0] == 'M' & pawn[0] == 'L'
			          print "Good move! you gobblet a smaller one!"
			          flag4 = 1
					  array[x] = pawn
		 turn = turn +1		  
	
	if (turn%2 != 0 )
	     print "The first player plays "
		 l=raw_input ("Place new piece into the board or move a current piece from the board")
		 if l == 'place'
		     flag5 = 0
			 flag6 = 0
			 flag7 = 0
			 pawn = raw_input("Choose: Size S<M<L,Color B, Number 1,2")
		     while ( flag5 ==0 )
		         for i in range (5)
			         if ( hand[i] == pawn )
				         hand[i] = 0
					     flag5 = 1
		     while ( flag6 == 0)	
			     x = raw_input ("Give a number from 0 to 8 to place the pawn") 
		         if ( array[x] == 0 )
		             array[x] = pawn
				     flag6 = 1
		         else
		             for i in range (8)
			             S[i] = array[i]
			         for i in range (8)
			             if S[i] == array[x]
				             temp = S[i]
			         if temp[0] == pawn[0]
			              print "You cannot move to this place, pick another one because you have the same size"
			         if temp[0] == 'L'
			             print "You cannot move to this place, pick another one because there is a large pawn here"
			         if temp[0] == 'S' & pawn[0] == 'M'
			             print "Good move! you gobblet a smaller one!"
						 array[x] = pawn
					     flag6 = 1
			         if temp[0] == 'M' & pawn[0] == 'S'
			             print "You cannot move to this place, pick another one because there is a medium pawn here"
				     if temp[0] == 'M' & pawn[0] == 'L'
			             print "Good move! you gobblet a smaller one!"
						 array[x] = pawn
			             flag6 = 1
		     turn = turn +1	
         else
		     m=raw_input ("Enter which pawn exactly you wanna move")
			 while (flag 7 == 0)
			     for i in range (8)
		             if array[i] == m
					     array[i] = 0
						 flag7 = 1
				 if (flag == 0)
				     m=raw_input("There is no such pawn in the board, pick another one you want to move")
			 k=input("Pick a number on the board from 0 to 8 to place the pawn")
			 for i in range (8)
			    S[i] = array[i]
			 for i in range (8)
			     if S[i] == array[k]
				     temp = S[i]
			     if temp[0] == pawn[0]
			        print "You cannot move to this place, pick another one because you have the same size"
			    if temp[0] == 'L'
			        print "You cannot move to this place, pick another one because there is a large pawn here"
			    if temp[0] == 'S' & pawn[0] == 'M'
			         print "Good move! you gobblet a smaller one!"
					 array[k] = pawn
					 flag6 = 1
			    if temp[0] == 'M' & pawn[0] == 'S'
			        print "You cannot move to this place, pick another one because there is a medium pawn here"
				if temp[0] == 'M' & pawn[0] == 'L'
			         print "Good move! you gobblet a smaller one!"
				     array[k] = pawn
			         flag6 = 1
		     turn = turn +1	
	 if ( turn%2 == 0 )	
	     print "The second player plays"
		 l=raw_input ("Place new piece into the board or move a current piece from the board")
		 if l == 'place'
		     flag5 = 0
			 flag6 = 0
			 flag7 = 0
			 pawn = raw_input("Choose: Size S<M<L,Color R, Number 1,2")
		     while ( flag5 ==0 )
		         for i in range (5)
			         if ( hand[i] == pawn )
				         hand[i] = 0
					     flag5 = 1
		     while ( flag6 == 0)	
			     x = raw_input ("Give a number from 0 to 8 to place the pawn") 
		         if ( array[x] == 0 )
		             array[x] = pawn
				     flag6 = 1
		         else
		             for i in range (8)
			             S[i] = array[i]
			         for i in range (8)
			             if S[i] == array[x]
				             temp = S[i]
			         if temp[0] == pawn[0]
			              print "You cannot move to this place, pick another one because you have the same size"
			         if temp[0] == 'L'
			             print "You cannot move to this place, pick another one because there is a large pawn here"
			         if temp[0] == 'S' & pawn[0] == 'M'
			             print "Good move! you gobblet a smaller one!"
						 array[x] = pawn
					     flag6 = 1
			         if temp[0] == 'M' & pawn[0] == 'S'
			             print "You cannot move to this place, pick another one because there is a medium pawn here"
				     if temp[0] == 'M' & pawn[0] == 'L'
			             print "Good move! you gobblet a smaller one!"
						 array[x] = pawn
			             flag6 = 1
		     turn = turn +1	
         else
		     m=raw_input ("Enter which pawn exactly you wanna move")
			 while (flag 7 == 0)
			     for i in range (8)
		             if array[i] == m
					     array[i] = 0
						 flag7 = 1
				 if (flag == 0)
				     m=raw_input("There is no such pawn in the board, pick another one you want to move")
			 k=input("Pick a number on the board from 0 to 8 to place the pawn")
			 for i in range (8)
			    S[i] = array[i]
			 for i in range (8)
			     if S[i] == array[k]
				     temp = S[i]
			 if temp[0] == pawn[0]
			     print "You cannot move to this place, pick another one because you have the same size"
			 if temp[0] == 'L'
			    print "You cannot move to this place, pick another one because there is a large pawn here"
			 if temp[0] == 'S' & pawn[0] == 'M'
			    print "Good move! you gobblet a smaller one!"
			     array[k] = pawn
			     flag6 = 1
			 if temp[0] == 'M' & pawn[0] == 'S'
			    print "You cannot move to this place, pick another one because there is a medium pawn here"
		     if temp[0] == 'M' & pawn[0] == 'L'
			     print "Good move! you gobblet a smaller one!"
				 array[k] = pawn
			     flag6 = 1
		     turn = turn +1	
	 
	 for i in range (8)
	     S[i] = array[i]
	 for i in range (8)
	     temp = S[i]
		 K[i] = temp[1]
	 if K[0] == K[1] & K[1]== K[2] 
	     if K[0] == 'R'
		     print "Player 2 wins!"
			 flag = 1
		 elif K[0] == 'B'
		     print "Player 1 wins!"
			 flag = 1
	 if K[3] == K[3] & K[3]== K[5] 
	     if K[3] == 'R'
		     print "Player 2 wins!"
			 flag = 1
		 elif K[3] == 'B'
		     print "Player 1 wins!"
			 flag = 1 
	 if K[6] == K[7] & K[6]== K[8] 
	     if K[6] == 'R'
		     print "Player 2 wins!"
			 flag = 1
		 elif K[6] == 'B'
		     print "Player 1 wins!"	
             flag = 1			 
	 if K[0] == K[3] & K[0]== K[6] 
	     if K[0] == 'R'
		     print "Player 2 wins!"
			 flag = 1
		 elif K[0] == 'B'
		     print "Player 1 wins!"	
			 flag = 1
	 if K[1] == K[4] & K[1]== K[7] 
	     if K[1] == 'R'
		     print "Player 2 wins!"
			 flag = 1
		 elif K[1] == 'B'
		     print "Player 1 wins!"	
			 flag = 1 
	 if K[2] == K[5] & K[2]== K[8] 
	     if K[2] == 'R'
		     print "Player 2 wins!"
			 flag = 1
		 elif K[2] == 'B'
		     print "Player 1 wins!"	
			 flag = 1
	if K[0] == K[4] & K[0]== K[8] 
	     if K[0] == 'R'
		     print "Player 2 wins!"
			 flag = 1 
		 elif K[0] == 'B'
		     print "Player 1 wins!"	
			 flag = 1 
	 if K[2] == K[4] & K[2]== K[6] 
	     if K[2] == 'R'
		     print "Player 2 wins!"
			 flag = 1 
		 elif K[2] == 'B'
		     print "Player 1 wins!"
			 flag = 1
				 