import cv2

# load images
image = cv2.imread("Section 12_Image processing/images/elfs.jpeg")
watermark = cv2.imread("Section 12_Image processing/images/watermarks/watermark.png")

# define watermark position.
x = image.shape[1] - watermark.shape[1]
y = image.shape[0] - watermark.shape[0]

# gets the region of interest (ROI) of the image.
watermark_position = image[y:, x:]
# cv2.imwrite("Section 12_Image processing/images/watermark_position.png", watermark_position)

# blends the watermark with the snippet of the original image.
blend = cv2.addWeighted(watermark_position, 0.5, watermark, 0.3, 0)
# cv2.imwrite("Section 12_Image processing/images/watermark_blend.png", watermark_position)

# replaces the region of interest with the blended watermark.
image[y:, x:] = blend
cv2.imwrite("Section 12_Image processing/images/elfs_watermarked.jpeg", image)
