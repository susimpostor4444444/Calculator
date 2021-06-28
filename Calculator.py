
print('    ADDITION    ')

add1 = input("Enter a number: ")
add2 = input("Enter another number: ")

answer = float(add1) + float(add2)
print (add1, "+", add2, "=", answer) 



print('    SUBTRACTION    ')

sub1 = input('Enter a number: ')
sub2 = input('Enter another number: ')

answer2 = float(sub1) - float(sub2)
print (sub1, "-", sub2, "=", answer2)



print('    MULTIPLICATION    ')

mult1 = int(input('Enter a number: '))
mult2 = int(input('Enter another number: '))

answer3 = mult1 * mult2
print(mult1, "x", mult2, "=", answer3)

print ("\tDIVISION")

divis1 = int(input("Enter a number: "))
divis2 = int(input("Enter a number: "))

answer4 = divis1 / divis2
print(divis1, "/", divis2, "=", answer4)


buttpp = input (" Division doesn't exist. Harrumph....      ")
#This says if the the input is 4 characters, then you're cool
if len( buttpp ) == 4:
    print ("""Wha...
            how...
                        did you just guess..? """)
    flag =input('           TEST TO SEE IF YOU ARE USING HACKS: ENTER ANY AMOUNT OF CHARACTERS: ')   
    if len (flag) == 16:  
            print('             HAXOR DETECTED. ENDING SIMULATION.')

    else: 
        print('             NO HACKS DETECTED. YOU ARE PATHETIC. ENDING SIMULATION.')

else: 
    print('What were you trying to do?')









