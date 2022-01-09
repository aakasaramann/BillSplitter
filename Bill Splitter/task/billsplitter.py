from random import choice


def who_is_lucky(friendlist):
    lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n').title()
    if lucky_feature == 'No':
        print("No one is going to be lucky")
        return False
    elif lucky_feature == 'Yes':
        lucky_person = choice(friendlist)
        print(f"{lucky_person} is the lucky one!\n")
        return lucky_person


def create_friend_dict(number):
    print("Enter the name of every friend (including you), each on a new line:")
    friend_list = []
    for i in range(number):
        friend_list.append(input())
    bill_value = int(input("Enter the total bill value:\n"))
    lucky_guy = who_is_lucky(friend_list)
    if lucky_guy:
        friend_dict = {friend_name: round(bill_value / (number - 1), 2) for friend_name in friend_list}
        friend_dict[lucky_guy] = 0
        print(friend_dict)
    else:
        friend_dict = {friend_name: round(bill_value / number, 2) for friend_name in friend_list}
        print(friend_dict)


user_input = int(input("Enter the number of friends joining (including you):\n"))
if user_input <= 0:
    print("No one is joining for the party")
else:
    create_friend_dict(user_input)

