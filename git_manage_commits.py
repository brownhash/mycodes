def manage_commits():
	import os

	def git_run(filename, message, branch):
		try:
			command = "git checkout -b" + branch
			try:
				os.system(command)
				print("----------------------------------------------------")
				print("Git checkout to >>{}<< branch: Done".format(branch))
				print("----------------------------------------------------")
			except:
				print("----------------------------------------------------")
				print("Already in >>{}<< branch".format(branch))
				print("----------------------------------------------------")
			command = "git pull origin " + branch
			os.system(command)
			print("----------------------------------------------------")
			print("Pulled the latest commit from specified branch")
			print("----------------------------------------------------")
			command = "git add " + filename
			os.system(command)
			print("----------------------------------------------------")
			print("File >>{}<< added to current stack".format(filename))
			print("-"*len(message))
			command = "git commit -am " + "\"" + message + "\""
			os.system(command)
			print("-"*len(message))
			print(">>{}<< appended as commit message".format(message))
			print("----------------------------------------------------")
			command = "git push origin " + branch
			os.system(command)
			print("----------------------------------------------------")
			print("All changes pushed to >>{}<< branch".format(branch))
			print("----------------------------------------------------")

		except:
			print("----------------------------------------------------")
			print("Some error occured")
			print("----------------------------------------------------")

	command = "git status"
	print("####################################################")
	print("----------------------------------------------------")
	print("Current changes in repository - ")
	print("----------------------------------------------------")
	os.system(command)
	print("####################################################\n")
	filename = str(input(
		"Enter filenames separated by spaces and use * at the ending\nExample: >>> file1 file2 file3 *\nEnter file names >>>")).split(
		" ")
	branch = str(input("Enter branch >>>"))
	message_status = str(input("Use same commit message for all files(y or n)\n>>>"))
	if (message_status == "Y" or message_status == "y"):
		message = str(input("Enter commit message >>>"))
		for i in filename:
			if (i != "*"):
				try:
					file_check = open(i, "r")
					file_check.close()

					print("####################################################")
					print("Filename - \"{}\"".format(i))
					print("####################################################\n")
					git_run(i, message, branch)

				except:
					print("####################################################")
					print(">>{}<< no such file exists".format(i))
					print("####################################################\n")
			else:
				print("####################################################")
				print("FINISHED")
				print("####################################################\n")

	elif (message_status == "N" or message_status == "n"):
		for i in filename:
			if (i != "*"):
				try:
					file_check = open(i, "r")
					file_check.close()

					print("####################################################")
					print("Filename - \"{}\"".format(i))
					print("####################################################\n")
					message = str(input("Enter commit message for {} >>>".format(i)))
					git_run(i, message, branch)

				except:
					print("####################################################")
					print(">>{}<< no such file exists".format(i))
					print("####################################################\n")
			else:
				print("####################################################")
				print("FINISHED")
				print("####################################################\n")

manage_commits()
