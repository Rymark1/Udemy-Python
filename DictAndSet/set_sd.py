# symmetric difference is finding items that exist in one list or the other, but not both.
# It is the opposite of set intersection, which provides items that are in both lists, but not only in one or the other

morning = ['Java', 'C', 'Ruby', 'Lisp', "C#"]
afternoon = ['Python', 'C#', 'Java', 'C', 'Ruby']

# the carat operator for symmetric difference is only useable when we are dealing with sets, not lists.
# possible_courses = morning ^ afternoon
# print(possible_courses)
# possible_courses_2 = afternoon.symmetric_difference(morning)
# print(possible_courses_2)

possible_courses = set(morning) ^ set(afternoon)
print(possible_courses)
# we can use the method symmetric difference when the action is performed on a set and a list is passed.
possible_courses_2 = set(afternoon).symmetric_difference(morning)
print(possible_courses_2)
