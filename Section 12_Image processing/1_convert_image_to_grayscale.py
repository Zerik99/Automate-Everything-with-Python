"""A simple app to convert an image to grayscale. Will use OpenCV."""
from pathlib import Path
import cv2
import numpy as np
from numpy import ndarray, generic, dtype
from typing import Generator


def main() -> None:
    """Main function."""
    image_dir: Path = Path("Section 12_Image processing/images")
    images: Generator[Path, None, None] = image_dir.glob("*.jpeg")
    color_images: list[Path] = [
        image for image in images if "_grayscale" not in image.stem
    ]

    print(color_images)

    for image_path in color_images:
        print(image_path)
        with open(image_path, "rb") as f:
            color_image: ndarray[int, dtype[generic]] = get_image(
                "/".join(image_path.parts)
            )
            grayscale_image: ndarray[int, dtype[generic]] = convert_to_grayscale(
                color_image
            )

            write_image_to_file(grayscale_image, image_path.stem)


def get_image(_path) -> ndarray[int, dtype[generic]]:
    """Get the image from the file system."""
    color_img: ndarray[int, dtype[generic]] = cv2.imread(
        filename=_path, flags=1
    )  # pylint: disable=E1101
    return color_img


def convert_to_grayscale(_color_img) -> ndarray[int, dtype[generic]]:
    """Convert the image to grayscale."""
    grayscale_img: np.ndarray[int, np.dtype[np.generic]] = cv2.cvtColor(
        src=_color_img, code=cv2.COLOR_BGR2GRAY
    )  # pylint: disable=E1101
    return grayscale_img


def write_image_to_file(_out_image, _image_name) -> None:
    """Write the grayscale image to the file system."""
    cv2.imwrite(
        f"Section 12_Image processing/images/{_image_name}_grayscale.jpeg", _out_image
    )
    return None


if __name__ == "__main__":
    main()
