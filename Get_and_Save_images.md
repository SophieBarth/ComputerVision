# How to automatically open and save images from and to a directory in Python
## Using cv2.imwrite | cv2.imread | os.path.join

If you are working on computer vision projects you might want to try them out on several images while working on the parameters.
To automate opening and saving images from and into directories, the OpenCV and OS packages are very helpful and easy to use. 

### Import OpenCV and Miscellaneous operating system interfaces
```
import cv2
import os
```
More about these libs and modules here:<br>
[OpenCV](https://docs.opencv.org/master/df/d65/tutorial_table_of_content_introduction.html), more specific about [cv2.imwrite and cv2.imread](https://docs.opencv.org/master/d4/da8/group__imgcodecs.html)
as well as, [Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html#module-os) and the [os.path modules](https://docs.python.org/3/library/os.path.html#module-os.path).

### Define the path relative to the location of your program

With *os.path.join(path, filename)* the path has to be defined in relation to the python file location.
In my case, the python file and the image in and out directories are all inside one directory called ComputerVision. <br>
ComputerVision:<br>
-images.py<br>
-test_images_input<br>
-test_images_output<br>

Thus the path is "test_images_input" and "test_images_output" (which I have defined in main). <br>
```
 folder_in = "test_images_input"
 folder_out = "test_images_output"
```

### Load and store images

The first part of the function contains going to the folder and going thrugh each file "filename" with a for loop. 
Then opening the file with cv2.imread and storing it in the variable img.
If a copy of the image was stored in img (not None), you can start transforming the image.

```
def load_save_images(folder_in, folder_out):

    #go through each file in the input folder with for loop
    for filename in os.listdir(folder_in):
    
        img = cv2.imread(os.path.join(folder_in,filename))
        
        #Stop condition
        if img is not None:
        
            #start transforming the image, e.g. with a function(img)
```

When the transformed image was returned, it's time to store it into the output folder.

cv2.imwrite(filename, image)
os.path.join(path, filename)
Combined:
cv2.imwrite(os.path.join(path, filename), image)

The variable folder_out contains the path to the directory. 
Changing the filename to a string, which already entails the format '.jpg' and adding the prefix 'out_' gives the output name. 

```
            #with imwrite save image, save into folder with os.path.join
            cv2.imwrite(os.path.join(folder_out, 'out_' + str(filename)), img)
```

### Caution
When you use cv2.imwrite and cv2.imread you might see a flip of red and blue. Open CV does not use a RBG, but a BGR colour space. Thus, the colours are flipped. 
Use the following to convert BGR to RGB:
```
im_rgb = cv2.cvtColor(im_cv, cv2.COLOR_BGR2RGB)
```
More information [here](https://note.nkmk.me/en/python-opencv-bgr-rgb-cvtcolor/).
