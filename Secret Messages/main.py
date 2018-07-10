# https://codeclubprojects.org/en-GB/python/secret-messages/

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newMessage = ''

# character = input('Please enter a character : ')

message = input('Please enter a message : ')
for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        # print(position)

        newPosition = (position + key) % 26
        # print(newPosition)

        newCharacter = alphabet[newPosition]
        # print('The new character is : ', newCharacter)

        newMessage += newCharacter
    else:
        newMessage += character

print('Your new message is :', newMessage)
