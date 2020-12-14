import cv2
import os


def load_save_images(folder_in, folder_out):
    #go through each file in the input folder with a for loop
    for filename in os.listdir(folder_in):
    
        #opening the file with cv2.imread and storing a copy in the variable img: : cv2.imread(os.path.join(path, filename))
        img = cv2.imread(os.path.join(folder_in,filename))
        
        #stop condition
        if img is not None:
        
            #start transforming the image, e.g. with a function(img)
            
            #with imwrite save image into folder with os.path.join: cv2.imwrite(os.path.join(path, filename), img)
            cv2.imwrite(os.path.join(folder_out, 'out_' + str(filename)), img)
            
            
def main():
    #store the path to the image directories into the variables, the paths are in relation to the python file location
    folder_in = "test_images"
    folder_out = "test_images_output"
    
    load_save_images(folder_in, folder_out)


if __name__ == "__main__":
    main()
