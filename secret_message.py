#encrypts messages according to the key provided
#special characters are not encrypted

# alphabet='abcdefghijklmnopqrstuvwxyz'
# key=int(input('enter your key: '))
# new_message=''
# question=input('please enter a message: ')

# for character in question:
#     if character in alphabet:
#         position=alphabet.find(character)
#         newPosition=(position+key)%26
#         newCharacter=alphabet[newPosition]
#         new_message+=newCharacter
#     else:
#         new_message+=character
# print(new_message)

#friendship calculator

name1=input("your name: ")
name2=input("your friend's name: ")
score=0
for character in name2:
    if character in 'aeiou':
        score+=5
        print(f"your friendship score is {score} ")
    if character in 'friend':
        score+=13
        print(f"your friendship score is {score} ")
    if score>=100:
        print("best friends!")





