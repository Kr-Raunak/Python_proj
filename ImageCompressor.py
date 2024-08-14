
# Importing the required modules
try:
	from tkinter import *
	from tkinter import messagebox as mb
	from PIL import Image
	from os import path
except Exception as e:
	# If there is an error while the importing of the required modules, then we print the error on the console screen and exit the script

	print('[ Error : {} ]'.format(e))
	quit()

# The main script starts here
def aboutAuthor():
	""" The function which launches the tkinter window for displaying the about author information """

	try:
		# Creating the about author tkinter window and its contents

		aboutWin = Tk()
		aboutWin.title('About Author  -  Image Compressor')
		Label(aboutWin, text = 'About Author', font = ('', 12, 'bold', 'italic'), foreground = 'black').pack(padx = 5, pady = 5)
		Label(aboutWin, text = """ National Institute of Technology
		-- Kumar Raunak.
			""", font = ('', 11), foreground = 'black').pack(padx = 5, pady = 5)
	except Exception as e:
		# If there is an error during the process, we display the error to the user through the message box

		mb.showerror('Error', e)

def appHelp():
	""" The function which launches the tkinter window for displaying the application help information """

	try:
		# Creating the help tkinter window and its contents

		helpWin = Tk()
		helpWin.title('Help  -  Image Compressor')
		Label(helpWin, text = 'Help', font = ('', 12, 'bold', 'italic'), foreground = 'black').pack(padx = 5, pady = 5)
		Label(helpWin, text = """

			""", justify = 'left', font = ('', 11), foreground = 'black').pack(padx = 5, pady = 5)
	except Exception as e:
		# If there is an error during the process, we display the error to the user through the message box

		mb.showerror('Error', e)

def compress(fileLocation, outputFileLocation, compressionLevel):
	""" The function to compress the required image files and save them as specified output locations. The level of compression is also specified by the user in the 3rd argument. The function uses the 'Image' class from the 'PIL' module and 'path' class from the 'os' module. The function if faces an error, it launches an tkinter messagebox. """

	try:
		if path.isfile(fileLocation):
			# If the user specified file exists, then we continue the process

			img = Image.open(fileLocation)
			# Creating the new resolution tuple for the compressed image
			compressionLevel = int(compressionLevel)
			resolution = (int(img.size[0]/compressionLevel), int(img.size[1]/compressionLevel))

			# Resizing the image file
			compressedImg = img.resize(resolution, Image.ANTIALIAS)
			compressedImg.save(outputFileLocation, quality = 90, optimize = True)
		else:
			# If the user specified file does not exists, then we raise an FileNotFoundError

			raise FileNotFoundError('Not such file "{}" found on the local machine.'.format(fileLocation))
	except Exception as e:
		# If there is an error raised during the execution of the above codes, then we display the error to the user using the tkinter messagebox and return the function

		mb.showerror('Error', e)
		return 0
	else:
		# If the codes are executed without any error, then we display the success message

		mb.showinfo('Image compressed successfully', 'The requested image file has been compressed successfully and saved at {}'.format(outputFileLocation))
		return 0

def main():
	""" The main function of the script """

	# Creating the main tkinter window
	win = Tk()
	win.title('Image Compressor')
	win.geometry('500x300')
	win.resizable(0, 0)

	# Creating the form elements
	frame1 = Frame(win)
	frame1.pack(padx = 5, pady = 5, fill = X)
	Label(frame1, text = 'Image file location', foreground = 'black', font = ('', 11, '')).pack(side = LEFT, padx = 5)
	fileLocation = StringVar(win)
	Entry(frame1, textvariable = fileLocation, font = ('', 11, ''), width = 100).pack(side = LEFT, padx = 5)

	frame2 = Frame(win)
	frame2.pack(padx = 5, pady = 5, fill = X)
	Label(frame2, text = 'Compression level', foreground = 'black', font = ('', 11, '')).pack(side = LEFT, padx = 5)
	compressionLevel = StringVar(win)
	Entry(frame2, textvariable = compressionLevel, font = ('', 11, ''), width = 100).pack(side = LEFT, padx = 5)

	frame3 = Frame(win)
	frame3.pack(padx = 5, pady = 5, fill = X)
	Label(frame3, text = 'Output file location', foreground = 'black', font = ('', 11, '')).pack(side = LEFT, padx = 5)
	outputFileLocation = StringVar(win)
	Entry(frame3, textvariable = outputFileLocation, font = ('', 11, ''), width = 100).pack(side = LEFT, padx = 5)

	# The button to be pressed to start the compression
	Button(win, text = 'Compress', foreground = 'green', background = 'black', activeforeground = 'black', activebackground = 'green', font = ('', 11,), padx = 10, pady = 7.5, command = lambda : compress(fileLocation.get(), outputFileLocation.get(), compressionLevel.get())).pack()

	# Adding the menubar to our application
	menubar = Menu(win)
	win.config(menu = menubar)

	# File menu
	filemenu = Menu(menubar, tearoff = 0, font = ('', 10, ''))
	filemenu.add_separator()
	filemenu.add_command(label = 'Exit', command = quit)

	# About menu
	aboutmenu = Menu(menubar, tearoff = 0, font = ('', 10, ''))
	aboutmenu.add_command(label = 'About author', command = aboutAuthor)
	aboutmenu.add_command(label = 'Help', command = appHelp)

	# Adding the both menus to the main menubar
	menubar.add_cascade(label = 'File', menu = filemenu)
	menubar.add_cascade(label = 'About', menu = aboutmenu)

	mainloop()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		# If the user presses CTRL+C key, then we exit the script

		quit()
