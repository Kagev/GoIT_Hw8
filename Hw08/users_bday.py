import datetime


def get_birthdays_per_week(users):
    current_date = datetime.date.today()
    start_of_week = current_date - datetime.timedelta(days=current_date.weekday())
    end_of_week = start_of_week + datetime.timedelta(days=6)

    bday_list = []

    for user in users:
        user_bday = user['birthday'].date()
        if start_of_week <= user_bday <= end_of_week:
            bday_list.append(user) 
    print('User with Birthday in this week: ')
    for user in bday_list:
        print(user['name'], '-', user['birthday'].strftime('%D.%M.%Y') )

#     current_date = datetime.date.today()
#     print(current_date)