#!/usr/bin/env python
# coding: utf-8

# In[3]:


hour=int(input("enter hours:"))
minute=int(input("Enter minutes:"))
sec=(hour*3600)+(minute*60)
print(hour,"hours","minute",minute,"seconds",sec)


# In[87]:


for i in range(1,6):
    for j in range(1,i+1):
        print(j%2,end=" ")
    print()    


# In[ ]:


#Q.4) Write a code to accept a number & print
#in words.
#Ex: 123
#Three Two One


# In[65]:



arr=['zero','one','two','three','four','five','six','seven','eight','nine']
def number(n):
    if(n==0):
        return ""
    else:
        small_ans=arr[n%10]
        ans=number(int(n/10)) + small_ans + " "
    return ans    

n=int(input("enter a numbers")) 
print("number entered was:",n)
print("converted to word it becomes:",end="")
print(number(n))      
      
      
      
      


# In[83]:


a='13567'
for i in range(0,len(a)):
     print(a[i]*(i+1))
print()    


# In[72]:


p=100
rs=int(input("enter a amount rupees"))
total=rs*p
print(total,"paise")


# In[74]:


s=input("enter a string")
print(s[1::2])


# In[94]:


a=(input("enter a string"))
d=l=s=0
for c in a:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        s=s+1
    print("letters",l)
    print("digits",d)
    print("symbols",s)
        


# In[2]:


n = int(input("Enter number"))
sum = 0
for num in range(1, n + 1, 1):
    sum = sum + num
print("Sum of first ", n, "numbers is: ", sum)
average = sum / n
print("Average of ", n, "numbers is: ", average)


# In[ ]:





# In[ ]:




