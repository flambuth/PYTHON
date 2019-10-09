from collections import namedtuple

BeltStats = namedtuple('BeltStats', 'score ninjas')

ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5)}


def get_total_points(belts=ninja_belts):
   total_points = 0
   for belt in ninja_belts.values():
      belt_points = belt[0] * belt[1]
      total_points += belt_points
   return total_points
######################
# First title case the passed in day argument
#        (so monday or MONDAY both result in Monday).

#        Then check if this title cased day is in the given workout_schedule dict.

#        If it is retrieve the workout (value), if not raise a KeyError.

#        Return the chill variable if it's a rest day (Saturday / Sunday),
#        else return the go_train variable with the workout interpolated.

#        Examples:
#        - if day is Saturday -> return 'Chill out!'
#        - if day is Thursday -> return 'Go train Legs'
#        - if day is Sunday -> return 'Chill out!'
#        - if day is Monday -> return 'Go train Chest+biceps'

#        Trivia: /etc/motd is a file on Unix-like systems that contains
#        a 'message of the day


#Need to make the except block raise an exception
#Need to change the try block to return the Train {} or Chill.

workout_schedule = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}

rest, chill, go_train = 'Rest', 'Chill out!', 'Go train {}'


def get_workout_motd(day):
   try:
      day = day.capitalize()
      day in workout_schedule.keys()   
      print(f"It's {day}, so you should {workout_schedule[day]} ")
   except :
      print(f"{day} is not in the schedule.") 