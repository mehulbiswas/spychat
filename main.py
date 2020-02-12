from spy_details import spy, Spy,ChatMessage,friends
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored


STATUS_MESSAGES = ['Bringing Havoc among enemy','Mission accomplish','Saving The World']


print 'Welcome! Let\'s start.'

question = 'Do you want to continue as ' + spy.salutation + ''+spy.name+'(Y/N)? '
existing = raw_input(question)

# method to add status
def add_status():

    updated_status_message = None

    # if condition to check current status message
    if spy.current_status_message != None:

        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently.'

    default = raw_input('Do you want to select from older status messages(Y/N)?')# Default statement

    if default.upper() == 'N':
        new_status_message = raw_input('What status you want to set?')

        # Nested if
        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1


        message_selection = int(raw_input('\nChoose from the above messages '))


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]


    else:
        print 'The option chosen is not valid! Press either y or n. '


    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'Currently you don\'s have a status update'

    # returning updated status message  to user
    return updated_status_message


# Method to add a friend
def add_friend():

    new_friend = Spy('','',0,0.0)# initialising new friend variable

    new_friend.name = raw_input('Please add your friend\'s name: ')
    new_friend.salutation = raw_input('Mr. or Ms. ?: ')

    new_friend.name = new_friend.salutation + '' + new_friend.name

    new_friend.age = raw_input('Age: ')
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input('Rating: ')
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 16 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend added'
    else:
        print 'Invalid Entry. We can\'t add add spy with provided details'

    return len(friends)

# method to select a friend
def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation,friend.name,
                                                                friend.age,friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input('Choose a friend from your friends')

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

# Method to send message
def send_message():

    friend_choice = select_a_friend()

    original_image = raw_input('What is the name of image?')
    output_path = 'output.jpg'
    text = raw_input('What message you want to send?')
    Steganography.encode(original_image,output_path,text)

    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)

    print 'You image is ready with message'


# Method to read a friend
def read_message():

    sender = select_a_friend()

    output_path =raw_input('What is the name of file? ')

    secret_text = Steganography.decode(output_path)
    
    # condtion for special words in the message
    if "SOS" in secret_text:
        print 'Sending Backup'
    elif "HELP" in secret_text:
        print 'I am Coming'
    elif "SAVE ME" in secret_text:
        print "Don't panic we will save you"
    else:
        new_chat = ChatMessage(secret_text,False)

        friends[sender].chats.append(new_chat)

        print 'Your message has been saved'

# Method to read chat history
def read_chat_history():

    read_for = select_a_friend()

    print '\n6'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"),'You said:',chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"),friends[read_for].name,chat.message)

# Method to start a chat
def start_chat(spy):

    spy.name = spy.salutation +' '+ spy.name

    # If Codition to check the age
    if spy.age > 16 and spy.age < 40:

        print 'Authentication complete. Welcome '+ spy.name +' age: '+ str(spy.age) +' rating: ' +str(spy.rating)\
              +' Nice to see with us'

        show_menu = True

        # while condition to show the menu to user
        while show_menu:
            menu_choices = 'choose any one \n 1. Add a status update \n 2. Add a new friend \n3. Send a message ' \
                           '\n4. Read a message \n5. Read Chats from a user \n6. Close Application \n'
            menu_choice = raw_input(menu_choices)

            # Nested if for showing menu choices
            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False

    else:
        print 'Your age is not valid for a spy'

if existing == 'Y':
    start_chat(spy)
else:
    spy = Spy('','',0,0.0)

    spy.name = raw_input('Welcome to Spychat, you must tell me your spy name first: ')

    if len(spy.name) > 0:
        spy.salutation = raw_input('what should i call you Mr or Ms : ')

        spy.age = raw_input('What is your age :')
        spy.age = int(spy.age)

        spy.rating = raw_input('What is your rating :')
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print 'Please add a valid name'