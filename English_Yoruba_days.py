days_dict = {'Sunday':'Aiku', 'Monday':'Aje',
             'Tuesday': 'Isegun', 'Wednesday':'Ojoru',
             'Thursday': 'Ojobo', 'Friday':'Eti',
             'Saturday':'Abameta'}

ENG_day = input('Enter a day in English here:')

def translator(ENG_day):
    if ENG_day in days_dict.keys():
        print('{} in Yoruba Language is {}'.format(ENG_day, days_dict[ENG_day]))
    else:
        print('Enter a valid day')

translator(ENG_day)
