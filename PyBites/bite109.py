workout_schedule = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
rest, chill, go_train = 'Rest', 'Chill out!', 'Go train {}'


def get_workout_motd(day):
    """First title case the passed in day argument
       (so monday or MONDAY both result in Monday).

       Then check if this title cased day is in the given workout_schedule 
       dict.

       If it is retrieve the workout (value), if not raise a KeyError.

       Return the chill variable if it's a rest day (Saturday / Sunday),
       else return the go_train variable with the workout interpolated.

       Examples:
       - if day is Saturday -> return 'Chill out!'
       - if day is Thursday -> return 'Go train Legs'
       - if day is Sunday -> return 'Chill out!'
       - if day is Monday -> return 'Go train Chest+biceps'

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day'"""
    #make it conform to the dictionary capitalized keys
    day = day.capitalize()
    day = day.strip()
    
    #search through the keys and find its string response
    activity = workout_schedule.get(day)
    if activity == 'Rest':
        return chill
    else:
        return go_train.format(activity)

#When I enter a paramter that will not be in the dictionary keys, it returns
#the go_train variable, with None in the {}.

def alt_get_workout_motd(day):
    day = day.capitalize()
    day = day.strip()
    #print(workout_schedule['day'])

    try:
        activity = workout_schedule[day]
        if activity == 'Rest':
            return chill
        else:
            return go_train.format(activity)

    except KeyError:
        print(f"{day} is not in the schedule.")