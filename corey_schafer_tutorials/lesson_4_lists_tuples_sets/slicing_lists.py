
courses = ['History', 'Math', 'Physics', 'CompSci'] #within brackets, we put each value we want separated by a comma

#print(courses) #if we run the code here, it will print out the courses listed above

#print(len(courses)) #it will print out 4 - b/c there are 4 values in our list

#print(courses[0]) #brackets will access values in the list to find the location of the value we want, the location is an index and it starts at 0
# so, to access the first value of our list, we put [0] and the output will be 'History'

#if we did print(courses[3]), the output would be CompSci b/c it is our 3rd value since we start at 0 (aka total length which is 4 minus 1, which is 3 to access the last value)
#if we did print(courses[-1]), the output would also be CompSci since it is starting at the end of the list - more convenient if we don't know the length of the list

print(courses[0:2]) #output would be 'History', 'Math' b/c what 0:2 is saying is we want all of the values b/w the beginning and up to but not including the 2nd index (which would be Physics)
# print(courses[:2]) would give us the same result b/c it would assume we would want to start at the beginning
