# --------------
#Code starts here
#Step 1
print("Step 1............................................................\n")
def read_file(path):

  file=open(file_path,"r")
  sentence= file.readline()
  file.close()
  return sentence

sample_message=read_file(file_path)
print("Sample Message : ",sample_message)

#Step 2
print("Step 2............................................................\n")

#Calling the function to read file  

def read_file(path):
  file=open(file_path_1,"r")
  sentence= file.readline()
  file.close()
  return sentence

message_1=read_file(file_path_1)
print("Message 1 ",message_1)

#Calling the function to read file

def read_file(path):
  file=open(file_path_2,"r")
  sentence= file.readline()
  file.close()
  return sentence

message_2=read_file(file_path_2)
print("Message 2 ",message_2)

#Function to fuse message

def fuse_msg(message_a,message_b):
  quotient=(int(message_b)//int(message_a))
  return str(quotient) 


#Calling the function 'fuse_msg'

secret_msg_1=fuse_msg(message_1,message_2)

#Printing the secret message 

print("Secret Message 1: ",secret_msg_1)

#Step 3
print("Step 3............................................................\n")



#Code starts here

def read_file(path):
  file=open(file_path_3,"r")
  sentence= file.readline()
  file.close()
  return sentence

message_3= read_file(file_path_3)
print("Message 3: ",message_3)

def substitute_msg(message_c):
   if(message_c == 'Red'): 
     sub='Army General'
   elif(message_c == 'Green'):
     sub= 'Data Scientist'
   else:
     sub='Marine Biologist'
   return sub  

secret_msg_2=substitute_msg(message_3)  

print("Secret Message 2 :",secret_msg_2)

#Step 4
print("Step 4............................................................\n")


# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here
def read_file(path):
  file=open(file_path_4,"r")
  sentence= file.readline()
  file.close()
  return sentence

message_4 = read_file(file_path_4)
print("Message 4: ",message_4)

def read_file(path):
  file=open(file_path_5,"r")
  sentence= file.readline()
  file.close()
  return sentence

message_5 = read_file(file_path_5)
print("Message 5: ",message_5)

def compare_msg(message_d,message_e):
   a_list=[]
   b_list=[]
   c_list=[]
   a_list=message_d.split()
   b_list=message_e.split()
   c_list= [i for i in a_list if i not in b_list]
   final_msg= " ".join(c_list)
   #print("Final Message :",final_msg)
   return final_msg

secret_msg_3= compare_msg(message_4,message_5)   
print("Secret Message 3 :",secret_msg_3)

#Step 5
print("Step 5............................................................\n")


#Code starts here
def read_file(path):
  file=open(file_path_6,"r")
  sentence= file.readline()
  file.close()
  return sentence

message_6 = read_file(file_path_6)
print("Message 6 :",message_6)

def extract_msg(message_f):
   a_list=[]
   b_list=[]
   a_list=message_f.split()
   even_word = lambda x : len(x)%2==0 
   b_list=list(filter(even_word,a_list))
   final_msg=" ".join(b_list)
   return final_msg

secret_msg_4=extract_msg(message_6)
print("Secret Message 4 :",secret_msg_4)

#Step 6
print("Step 6............................................................\n")


#Secret message parts in the correct order

message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here

secret_msg= " ".join(message_parts)

def write_file(secret_msg,path):
   file= open(path,"a+")
   file.write(secret_msg)
   file.close()

write_file(secret_msg,final_path)
print("Secret Message :",secret_msg)



