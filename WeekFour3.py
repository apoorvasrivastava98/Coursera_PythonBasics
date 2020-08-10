Q1-Which of these is the accumulator variable?

byzo = 'hello world!'
c = 0
for x in byzo:
    z = x + "!"
    print(z)
    c = c + 1
ans-D. c
Yes, this is the accumulator variable. By the end of the program, it will have a full count of how many items are in byzo.

Q2-Which of these is the sequence?

cawdra = ['candy', 'daisy', 'pear', 'peach', 'gem', 'crown']
t = 0
for elem in cawdra:
    t = t + len(elem)
ans-A. cawdra
Yes, this is the sequence that we iterate over.

Q3-Which of these is the iterator (loop) variable?

lst = [5, 10, 3, 8, 94, 2, 4, 9]
num = 0
for item in lst:
    num += item
ans-A. item
Yes, this is the iterator variable. It changes each time but is not the whole sequence itself.

Q4-What is the iterator (loop) variable in the following?

rest = ["sleep", 'dormir', 'dormire', "slaap", 'sen', 'yuxu', 'yanam']
let = ''
for phrase in rest:
    let += phrase[0]
The iterator variable is
ans-phrase
 
Q5-Currently there is a string called str1. Write code to create a list called chars which should contain the characters from str1. Each character in str1 should be its own element in the list chars.
 
 str1 = "I love python"
# HINT: what's the accumulator? That should go here.

chars = []
for character in str1:
    chars.append(character)
