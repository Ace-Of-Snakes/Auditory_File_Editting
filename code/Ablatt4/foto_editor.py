from PIL import Image
import numpy as np

def load_image():
    # load in original image
    path = "code/Ablatt4/test.png"
    image = Image.open(path)
    width = image.size[0]
    height = image.size[1]
    print(f'width: {width}, height: {height}')
    return image
    
def aufgabe1_1_manual_resize():
    image = load_image()
    # transfer image to numpy array
    np_img = np.array(image)
    slice_factor = 5
    # slice image by factor two
    img_sliced = np_img[::slice_factor,::slice_factor]

    # save image to Image Pillow object and to folder
    img_sliced = Image.fromarray(img_sliced)
    img_sliced.save(f"code/Ablatt4/fotos/test_sliced_{slice_factor}.png")
    print(img_sliced.size[0],img_sliced.size[1])

def aufgabe1_1_resize():
    image = load_image()

    resize_factor = 10
    # resize image by resize_factor
    img_resized = image.resize((image.size[0]//resize_factor,image.size[1]//resize_factor))
    # save image to Image Pillow object and to folder
    img_resized.save(f"code/Ablatt4/fotos/test_resized_{resize_factor}.png")
    print(img_resized.size[0],img_resized.size[1])
    

if __name__ == "__main__":
    aufgabe1_1_manual_resize()
    #aufgabe1_1_resize()