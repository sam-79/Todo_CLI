import argparse
import os
from datetime import date

cwd=os.getcwd()
helptext="""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""

def create():
	print('No tasks/Todo file in current working directory')
	print("Create todo & done file in cwd")
	x=input('[y/n] : ')
	if(x=='y' or x == 'Y'):
		with open(cwd+'/todo.txt','w') as W1, open(cwd+'/done.txt','w') as W2:
			W1.close()
			W2.close()
	elif(x=='n' or x=='N'):
		print('Abort')
	else:
		print('Unrecognized option\nAbort')
		

#Add task to todo.txt
def addTask(task):
	
	with open(cwd+'/todo.txt','a') as writer, open(cwd+'/done.txt','w') as W1:
		writer.write(task+"\n")
		writer.close()
		W1.close()

	
#Listing tasks
def showTask():
	
	with open(cwd+'/todo.txt','r') as reader:
		tasks=list(reader)
		for i in range(len(tasks),0,-1):
			print('[%d] '%i+tasks[i-1][:-1])
		reader.close()

#Delete task from todo.txt
def deleteTask(index,done=False):
	
	#This Delete/removes the todo from todo.txt 
	with open(cwd+'/todo.txt','r') as reader:
		tasks=list(reader)
		if(index<=len(tasks)):
			del_item=tasks.pop(index-1)
		else:
			print("Error: todo #%s does not exist. Nothing deleted."%index)
			exit()
		reader.close()
	
	#Rewrite all todos after deleting removing todo
	with open(cwd+'/todo.txt','w') as writer:
		writer.writelines(tasks)
		writer.close()
	
	#This block add completed task to done.txt			
	if(done):
		with open(cwd+'/done.txt','a') as writer:
			writer.write('x '+str(date.today())+' '+del_item[:-1]+"\n")
			writer.close()
			print('Marked todo #%s as done'%index)
				

#reports
def showReport():
	
	try:
		with open(cwd+'/todo.txt','r') as R1, open(cwd+'/done.txt','r') as R2:
			pending=list(R1)
			done=list(R2)
			if(len(done) != 0):
				date=done[-1][2:12]
				print(date,end=" ")
			print("Pending : "+str(len(pending))+" Completed : "+str(len(done)))
			R1.close()
			R2.close
	except Exception as ex:
		print(ex.__class__.__name__)
		if (ex.__class__.__name__=='FileNotFoundError'):
			create()

"""
Excution Starts here
"""
if __name__=="__main__":	
	# Create parser object
	parser=argparse.ArgumentParser(prog="TODO",description="Manage all your Todo's")
	
	#Add Arguments
	parser.add_argument("argument",help="Commands",choices=["add","ls","del","done","help","report"])
	
	parser.add_argument("option", nargs='?', default=" ",help='Index or task to add' )
	
	# Execute the parse_args() method
	args = parser.parse_args()
	
	##Manage Arguments
	if(args.argument == "add" and args.option != " "):
		x=addTask(args.option)
		print("Added todo: %s"%args.option)
	
	elif(args.argument == "ls" and args.option == " "):
		showTask()
	
	elif(args.argument == "del" and args.option != " "):
		deleteTask(int(args.option))
		print("Deleted todo #%s"%args.option)
	
	elif(args.argument == "done" and args.option != " "):
		deleteTask(int(args.option),done=True)
	
	elif(args.argument == "help" and args.option == " "):
		print(helptext)
	
	elif(args.argument == "report" and args.option == " "):
		showReport()
	
	else:
		print("Unrecognized Command")

