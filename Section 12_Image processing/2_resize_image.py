"""a simple app to resize an image. Will use OpenCV."""
import cv2
from numpy import ndarray, generic, dtype


def main() -> None:
    """Main function."""
    image: ndarray[int, dtype[generic]] = cv2.imread(
        "Section 12_Image processing/images/galaxy.jpeg"
    )
    print(image.shape)
    write_image_to_file(_image=resize_image(image, 50), _image_name="galaxy")


def calculate_new_dimensions(_image, _scale_percent) -> tuple[int, int]:
    """Calculate the new dimensions of the image."""
    width = int(_image.shape[1] * _scale_percent / 100)
    height = int(_image.shape[0] * _scale_percent / 100)
    return width, height


def resize_image(_image, _scale_percent) -> ndarray[int, dtype[generic]]:
    """Resize the image."""
    width, height = calculate_new_dimensions(_image, _scale_percent)
    resized_image: ndarray[int, dtype[generic]] = cv2.resize(
        src=_image, dsize=(width, height)
    )
    return resized_image


def write_image_to_file(_image, _image_name) -> None:
    """Write the grayscale image to the file system."""
    cv2.imwrite(
        f"Section 12_Image processing/images/resized/{_image_name}_resized.jpeg", _image
    )
    return None


if __name__ == "__main__":
    main()
