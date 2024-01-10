courses = ['History', 'Math', 'Physics','CompSci']
courses_2 = ['Art', 'Education']
nums = [1, 5, 2, 4, 3]

#courses.append('Art') #add an item to the END of the list/courses
#if we wanted to add 'Art' to a specific location, use INSERT method - it takes two arguments: 1) the index where you want to insert the value and 2) the vlaue itself
#courses.insert(0, 'Art') #it will insert Art the beginning of our list b/c of that 0

#the extend method can be used if we want to add multiple values to our list

#courses.insert(0, courses_2) #this would add ['Art', 'Education'], 'History' etc. which wouldn't add each individual value
#this is why we need to use the extend method

#courses.extend(courses_2) #extend only takes 1 argument, it will add the values of our 2nd list to our original list

#courses.remove('Math') would remove Math
#courses.pop() would remove the last value in our list - CompSci would be "popped" off our list
#courses.reverse() would print out our courses but in reverse
#courses.sort() would sort in alphabetical order - if it contained numbers, it would sort in ascending order
#courses.sort(reverse=True) would sort courses in descending order

courses.sort()
nums.sort()

print(courses)
print(nums)