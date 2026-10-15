marks=[78,65,92,45,80] 
marks.sort()
total=0
count=0
pass_count=0
pass_subc=0
fail_subc=0
for mark in marks:
   total=total+mark
   if mark>=40:
     pass_count=pass_count+1
     pass_subc=pass_subc+1
   else:
     fail_subc=fail_subc+1

average=total/len(marks)
higest=marks[-1]
lowest=marks[0]
 
print("Total marks=",total)
print("Average=",average)
print("Higest marks=",higest)
print("Lowest marks=",lowest)
if pass_count==len(marks):
  print("Final result= PASS")
else:
  print("Final result= FAIL")
print("Passed subject=",pass_subc)
print("failed subject=",fail_subc)
