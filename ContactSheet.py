import PIL
from PIL import Image, ImageDraw, ImageFont
from PIL import ImageEnhance



# read image and convert to RGB
image=Image.open("python-pillow/MountShasta.jpg").convert("RGB")
images=[]
r,g,b = image.split()

# Create 3 images for 3 different channels
for i in range (0,3):
    t=[r,b,g]
    t2=[r,b,g]
    for j in (.1,.5,.9):
        t[i]=t[i].point(lambda a: a * j)
        initial_contact_sheet=PIL.Image.new(image.mode, (image.width,image.height+100))
        result=Image.merge('RGB',tuple(t))
        initial_contact_sheet.paste(result,(0,0))
        txt = Image.new("RGB", (image.width, 100))
        fnt = ImageFont.truetype("ariel.ttf", 50)
        d = ImageDraw.Draw(txt)
        d.text((10,20), f"channel {i} intensitiy {j}", font=fnt, fill=(255,255,255,255))
        initial_contact_sheet.paste(txt,(0,image.height))
        images.append(initial_contact_sheet)
        t[i]=t2[i]
           

#create a contact sheet
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
contact_sheet.show()

