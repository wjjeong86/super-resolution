#
'''============================================================================='''
import PIL, PIL.Image as Image, numpy as np
def imshow(image):
    assert image.dtype==np.uint8 or image.dtype==np.float32
    
    print(f'{image.dtype}{image.shape}')
        
    if image.dtype==np.float32:
        image = np.uint8(image*255)
    
    image = np.squeeze(image)
    image_pil = Image.fromarray(image)
    
    try:
        display(image_pil)
    except:
        print(f"화면출력안됨 {image.shape}")
    
    return
    
    
if __name__ == '__main__':
    
    
    image = np.uint8(
            np.random.randint(0,255, (128,128))
    )
    image = np.float32(
            np.random.rand(128,128)
    )
    
    imshow(image)
'''============================================================================='''