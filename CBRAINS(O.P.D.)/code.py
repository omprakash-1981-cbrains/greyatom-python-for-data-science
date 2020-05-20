# --------------
#Step 1
print("\nStep 1\n")
print("----------------------------------------------------------------------------\n")
class_1= ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class=class_1 + class_2
print("class_1 \n",class_1)
print("class_2 \n",class_2)
print("new_class \n",new_class)
new_class.append('Peter Warden')
print("updated new_class \n",new_class)
new_class.remove('Carla Gentry')
print("updated new_class \n",new_class)
print("-----------------------------------------------------------------------------\n")

#Step 2

print("\nStep 2\n")
courses={"Math"   : 65,
        "English" : 70,
        "History" : 80,
        "French"  : 70,
        "Science" : 60}
print(courses)
values = courses.values() #Return values of a dictionary.
total = sum(values) #Compute sum of the values.
print("Total : ", total)

percentage = (total/500)*100 
print("Percentage :",percentage)
print("-----------------------------------------------------------------------------\n")

#Step 3

print("\nStep 3\n")
mathematics= {"Geoffrey Hinton"     :78,
              "Andrew Ng"           :95,
              "Sebastian Raschka"   :65,
              "Yoshua Benjio"       :50,
              "Hilary Mason"        :70,
              "Corinna Cortes"  	:66,
              "Peter Warden"    	:75}
print(mathematics)
max_marks_scored = max(courses,key = courses.get)
print (max_marks_scored)

topper = max(mathematics,key = mathematics.get)
print (topper)
print("-----------------------------------------------------------------------------\n")


#Step 4

print("\nStep 4\n")

first_name,last_name=topper.split()
print(first_name)
print(last_name)

full_name=last_name+ " " + first_name
certificate_name = full_name.upper()
print(certificate_name)


