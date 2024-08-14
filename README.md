"""
Image Compressor (Python3)

An image compressor tool made using python3 and tkinter GUI framework. It is a graphical application which serves the sole purpose of compression of JPG and PNG image files. It also uses the Pillow library (PIL) for working with image files and objects.

Dependencies : tkinter (python3 module), Pillow (python3 module)

Author : Kumar Raunak (E-Mail : kumarrounak03@gmail.com)
"""


The application is very simple to use. Follow the below steps for proper usage of this application :
1. First enter the complete location of the image file that you are going to compress. e.g., /home/mrwsb/Photos/image1.jpg
2. Then, enter the compression level in numeric form. The number you enter divides the current resolution of the image,
just like enter 2 for half compression.
3. At last, enter the output file location with extension (either .jpg or .png).
This is the place where our compressed image will be saved. Finally, press on the compress button. And wait for the result.

If there is an error, it will be informed to you through the alert boxes. Also after successgfull compression, the message
box will be informing you that.
