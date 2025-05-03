import math
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class LinearAlgebraProject:

    @staticmethod
    def image_transform(image_np, linear_transform):
        # Get the dimensions of the image
        height, width, channels = image_np.shape

        # Define the center
        center_x = width / 2
        center_y = height / 2

        # Loop through each pixel in the image and apply the transformation
        transformed_image = np.zeros_like(image_np)

        for y in range(height):
            for x in range(width):
                # Translate the pixel to the origin
                translated_x = x - center_x
                translated_y = -(y - center_y)

                # Apply the transformation: matrix vector multiplication
                transformed_x, transformed_y = linear_transform@np.array([translated_x, translated_y])

                # Translate the pixel back to its original position
                transformed_x += center_x
                transformed_y = - transformed_y + center_y

                # Round the pixel coordinates to integers
                transformed_x = int(round(transformed_x))
                transformed_y = int(round(transformed_y))

                # Copy the pixel to the transformed image
                if (transformed_x >= 0 and transformed_x < width and
                    transformed_y >= 0 and transformed_y < height):
                    transformed_image[transformed_y, transformed_x] = image_np[y, x]

        return transformed_image

    @staticmethod
    def main():
      
        # Define the image file path
        image_path = "image0.png"
        # Load the image
        image0 = Image.open(image_path)
        #plt.imshow(image)

        # Convert the image as a numpy array
        image0_np = np.array(image0)

        print(f'The dimension of the image_np is {image0_np.shape}')

        #plt.imshow(image0)
        #plt.show()

        #TRANSFORMATION 1
        t1 = np.array([
            [1/math.sqrt(2), 0],
            [0, 1/math.sqrt(2)]
        ])

        # apply transform
        image1_np = LinearAlgebraProject.image_transform(image0_np, t1)
        # convert a numpy array to image
        image1 = Image.fromarray(image1_np)

        #plt.imshow(image1)
        #plt.show()
        
        #TRANSFORMATION 2
        t2 = np.array([
            [-3/5, 4/5],
            [4/5, 3/5]
        ])
        
        # apply transform
        image2_np = LinearAlgebraProject.image_transform(image1_np, t2)
        # convert a numpy array to image
        image2 = Image.fromarray(image2_np)

        #plt.imshow(image2)
        #plt.show()

        #TRANSFORMATION 3
        t3 = np.array([
            [3/5, -4/5],
            [-4/5, -3/5]
        ])
        
        # apply transform
        image3_np = LinearAlgebraProject.image_transform(image2_np, t3)
        # convert a numpy array to image
        image3 = Image.fromarray(image3_np)

        #plt.imshow(image3)
        #plt.show()

        #TRANSFORMATION 4
        t = np.array([
            [-3 / (5 * math.sqrt(2)), 4 / (5 * math.sqrt(2))],
            [4 / (5 * math.sqrt(2)), 3 / (5 * math.sqrt(2))]
        ])
        
        # apply transform
        image1_np = LinearAlgebraProject.image_transform(image1_np, t)
        # convert a numpy array to image
        image1 = Image.fromarray(image1_np)

        #plt.imshow(image1)
        #plt.show()

        #TRANSFORMATION 5
        t_inv = np.array([
            [-6 / (5 * math.sqrt(2)), 8 / (5 * math.sqrt(2))],
            [8 / (5 * math.sqrt(2)), 6 / (5 * math.sqrt(2))]
        ])
        
        # apply transform
        image3_np = LinearAlgebraProject.image_transform(image3_np, t_inv)
        # convert a numpy array to image
        image3 = Image.fromarray(image3_np)

        #plt.imshow(image3)
        #plt.show()

        #TRANSFORMATION 6
        ft = np.array([
            [0, 0.5],
            [1, 0]
        ])
        
        # apply transform
        image4_np = LinearAlgebraProject.image_transform(image1_np, ft)
        # convert a numpy array to image
        image4 = Image.fromarray(image4_np)

        plt.imshow(image4)
        plt.show()
        
LinearAlgebraProject.main()