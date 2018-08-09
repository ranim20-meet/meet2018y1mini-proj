from PIL import Image #imports folder
im = Image.open('paper.png') #gets the image
pix = im.load() #load returns a pixel access object that can be used to read and modify pixels
print(im.size) #prints the image size in pixels [x,y]
print(pix[30,15]) #prints the RGB value of a chosen pixel [x,y]
new_width  = 32
new_height = 32
imW = im.resize((new_width, new_height), Image.ANTIALIAS)
imW.save('white_paper.png')
 
# Blue
width, height = im.size # assigns the 
for x in range(width): 
    for y in range(height): #For loops inside of for loops?! Why do we need two for loops?
        r,g,b = pix[x,y]
        if not (r>230 and g>230 and b>230): #Why did I put this if statement here? Try getting rid of it and running.
            pix[x,y] = (r//2,g//2,b) #Why did I do //? Try it with normal division.
new_width  = 32
new_height = 32
imB = im.resize((new_width, new_height), Image.ANTIALIAS)
imB.save('blue_paper.png')


# Red
for x in range(width): 
    for y in range(height): #For loops inside of for loops?! Why do we need two for loops?
        r,g,b = pix[x,y]
        if not (r>230 and g>230 and b>230): #Why did I put this if statement here? Try getting rid of it and running.
            pix[x,y] = (r*2,g,b//2) #Why did I do //? Try it with normal division.
imR = im.resize((new_width,new_height), Image.ANTIALIAS)
imR.save('red_paper.png')

# Green
for x in range(width): 
    for y in range(height): #For loops inside of for loops?! Why do we need two for loops?
        r,g,b = pix[x,y]
        if not (r>230 and g>230 and b>230): #Why did I put this if statement here? Try getting rid of it and running.
            pix[x,y] = (r//2,g*2,b) #Why did I do //? Try it with normal division.
imG = im.resize((new_width,new_height), Image.ANTIALIAS)
imG.save('green_paper.png')

# Yellow
for x in range(width): 
    for y in range(height): #For loops inside of for loops?! Why do we need two for loops?
        r,g,b = pix[x,y]
        if not (r>230 and g>230 and b>230): #Why did I put this if statement here? Try getting rid of it and running.
            pix[x,y] = (r*2,g,b//4) #Why did I do //? Try it with normal division.
imY = im.resize((new_width,new_height), Image.ANTIALIAS)
imY.save('yellow_paper.png')
