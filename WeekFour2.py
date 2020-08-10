Q1-Which method would you use to figure out the position of an item in a list?
    D. .index()
   Yes, index will return the position of the first occurance of an item.
   
Q2-Which method is best to use when adding an item to the end of a list?
     C. .append()
     Yes, though you can use insert to do the same thing, you don't need to provide the position.
    
Q3-Write code to add ‘horseback riding’ to the third position (i.e., right before volleyball) in the list sports.
      sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
      sports.insert(2,'horseback riding')

Q4-Write code to take ‘London’ out of the list trav_dest.
       trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
       trav_dest.remove('London')
       
Q5-Write code to add ‘Guadalajara’ to the end of the list trav_dest using a list method.
        trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
        trav_dest.append("Guadalajara")
        
Q6-Write code to rearrange the strings in the list winners so that they are in alphabetical order from A to Z.
         winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
         winners.sort()

Q7-Write code to switch the order of the winners list so that it is now Z to A. Assign this list to the variable z_winners.
          winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
          winners.sort(reverse=True)
          z_winners = winners





