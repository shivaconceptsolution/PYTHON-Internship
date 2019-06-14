m1 = int(input("enter physics marks"))
m2 = int(input("enter chem marks"))
m3 = int(input("enter maths marks"))
m4 = int(input("enter english marks"))
m5 = int(input("enter hindi marks"))

if (m1>=0 and m1<=100)  and (m2>=0 and m2<=100) and (m3>=0 and m3<=100) and (m4>=0 and m4<=100) and (m5>=0 and m5<=100):
   count=0
   dist=""
   sub=""
   grace=0
   if m1>=75:
      dist+=" PHYSICS "
   if m2>=75:
      dist+=" CHEM "
   if m3>=75:
      dist+=" MATHS "
   if m4>=75:
      dist+=" ENGLISH "
   if m5>=75:
      dist+=" HINDI "   
   if m1<33:
   	 count=count+1
   	 sub+=" PHYSICS "
   	 grace=m1
   if m2<33:
   	 count=count+1
   	 sub+=" CHEMISTRY "
   	 grace=m2
   if m3<33:
   	 count=count+1
   	 sub+=" MATHS "
   	 grace=m3
   if m4<33:
   	 count=count+1
   	 sub+=" ENGLISH "
   	 grace=m4
   if m5<33:
   	 count=count+1
   	 sub+=" HINDI "
   	 grace=m5
   if count==0 or (count==1 and grace>=28):
     if count==0: 
       per = (m1+m2+m3+m4+m5)/5
     else:
       per = (m1+m2+m3+m4+m5+(33-grace))/5 
     if per>=33 and per<45:
        print("pass with third division with "+str(per)+"%")
     elif per<60:
        print("pass with second division with "+str(per)+"%")
     else:
        print("pass with first division with "+str(per)+"%")
     if dist!="":
        print("Distinction subject name is "+dist)
     if grace!=0:
        print("YOU Are pass by Grace and Grace subject name is "+sub+" Grace marks is "+str(33-grace)) 
   elif count==1:
     print("suppl in "+sub)
   else:
     print("fail in "+sub)     


else:
   print("All subject marks should be 0 to 100")	
