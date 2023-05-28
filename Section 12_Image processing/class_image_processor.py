"""a class for image processing"""
from pathlib import Path
import cv2
from numpy import ndarray, generic, dtype


class ImageProcessor:
    """a class for image processing"""

    def __init__(self, _path) -> None:
        self.path: Path = _path
        self.image: ndarray[int, dtype[generic]] = self.get_image()

    def get_image(self) -> ndarray[int, dtype[generic]]:
        """Get the image from the file system."""
        image: ndarray[int, dtype[generic]] = cv2.imread(
            filename="/".join(self.path.parts), flags=1
        )  # pylint: disable=E1101
        return image

    def convert_to_grayscale(self) -> None:
        """Convert the image to grayscale."""
        grayscale_img: ndarray[int, dtype[generic]] = cv2.cvtColor(
            src=self.image, code=cv2.COLOR_BGR2GRAY
        )  # pylint: disable=E1101
        self.write_image_to_file("grayscale", grayscale_img)

    def resize_image(self, _scale_percent) -> None:
        """Resize the image."""
        width, height = self.calculate_new_dimensions(_scale_percent)
        resized_image: ndarray[int, dtype[generic]] = cv2.resize(
            src=self.image, dsize=(width, height)
        )
        self.write_image_to_file("resize", resized_image)

    def write_image_to_file(
        self, _action: str, _image: ndarray[int, dtype[generic]]
    ) -> str:
        """Write the grayscale image to the file system."""
        cv2.imwrite(
            f"{'/'.join(self.path.parts[0:-1])}/{_action}/{self.path.stem}_{_action}.jpeg",
            _image,
        )

        path_str: str = f"{'/'.join(self.path.parts[0:-1])}/{_action}/{self.path.stem}_{_action}.jpeg"
        return path_str

    def calculate_new_dimensions(self, _scale_percent) -> tuple[int, int]:
        """Calculate the new dimensions of the image."""
        width = int(self.image.shape[1] * _scale_percent / 100)
        height = int(self.image.shape[0] * _scale_percent / 100)
        return width, height
