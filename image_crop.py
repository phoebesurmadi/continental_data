# Import necessary libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to display images
def display_images(original_img, cropped_img):
    # Convert BGR images to RGB for displaying with Matplotlib
    original_img_rgb = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
    cropped_img_rgb = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)

    # Create a subplot to display the images side by side
    plt.figure(figsize=(10, 5))

    # Display original image with ROI
    plt.subplot(1, 2, 1)
    plt.imshow(original_img_rgb)
    plt.title("Original Image with ROI")
    plt.axis('off')  # Hide axis

    # Display cropped ROI
    plt.subplot(1, 2, 2)
    plt.imshow(cropped_img_rgb)
    plt.title("Cropped ROI")
    plt.axis('off')  # Hide axis

    # Adjust layout and show the plots
    plt.tight_layout()
    plt.show()

def main():
    # Read the input image
    image_path = "/content/picture.jpg"  # Replace with your image path
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found. Please check the path.")
        return

    print("Image read successfully.")

    # Define the Region of Interest (ROI) coordinates
    roi_x, roi_y, roi_width, roi_height = 400, 400, 600, 600
    print("ROI coordinates defined.")

    # Draw a rectangle around the ROI for visualization
    cv2.rectangle(image, (roi_x, roi_y), (roi_x + roi_width, roi_y + roi_height), (0, 255, 0), 2)

    # Crop the Region of Interest (ROI)
    roi = image[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]
    print("Cropped the ROI.")

    # Display the original image with ROI and the cropped ROI
    display_images(image, roi)

if __name__ == "__main__":
    main()
