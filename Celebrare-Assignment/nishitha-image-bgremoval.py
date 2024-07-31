'''
*****************************************
Modules needed : easygui, rembg, PIL
pip install easygui
pip install rembg
pip install Pillow | PIL
*****************************************
Running it through command prompt will allow you to directly select the image and process it,
allows you to select destination where you want to save your edited image
Ex: input: Select an image from File Explorer ex: select namelogo.png
    output: Select the destination folder & give file name with extension Ex - namelogoNew.png
'''
from PIL import Image
from rembg import remove
import easygui
inputPath = easygui.fileopenbox(title="Select image file")
outputPath = easygui.filesavebox(title="Save file to....")

inputImage = Image.open(inputPath)
outputImage = remove(inputImage)
outputImage.save(outputPath)
print('Image background removed successfully')