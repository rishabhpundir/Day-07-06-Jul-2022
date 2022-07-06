# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal. 


# n = int(input('Enter the number of students : '))
# student_marks = {}
# for i in range(n):
#     name, *line = input(f'Enter student {i+1} name & marks with spaces inbetween : ').split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = str(input('Enter the name of the student you want to calculate avg. marks for :'))

# avg = str(sum(student_marks[query_name])/len(student_marks[query_name]))

# if len(avg) <= 4:
#     x = avg + '0'
# elif len(avg) > 4:
#     x = round(float(avg), 2)

# print(f'{query_name} has scored {x} as average marks.')


# --------------------------------------------------------------------------------------------------------------------


# Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear

# times per group except for the Captain's room.

# Mr. Anant needs you to help him find the Captain's room number.
# The total number of tourists or the total number of groups of families is not known to you.
# You only know the value of

# and the room number list.

# Input Format

# The first line consists of an integer,
# , the size of each group.
# The second line contains the unordered elements of the room number list.

# counter = 0
# occupants = {}
# no_of_members = int(input('Type the number of family members per group : '))
# room_numbers = str(input('Enter the unordered room numbers list : '))
# room_no_list = room_numbers.split()
# family_rooms = set(room_no_list)
# captain_room = 0

# for i in family_rooms:
#     counter=0
#     for j in room_no_list:
#         if i == j:
#             counter+=1
#     occupants[i] = counter

# for room in occupants:
#     if occupants[room] == 1:
#         print(f"The Captain's room number is {room}.")


# no_of_members = int(input('Type the number of family members per group : '))
# room_numbers = str(input('Enter the unordered room numbers list : '))
# room_no_list = room_numbers.split()
# captain_room = [room for room in room_no_list if room_no_list.count(room)==1]
# print(captain_room[0])



    
