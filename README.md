
# Bulk Image Downloader - PyQt5 Application

This is a PyQt5-based graphical user interface (GUI) application for downloading bulk images from Google using a specified keyword, the desired number of images, and an email ID.

## Features

- **User-Friendly Interface**: Input keyword, number of images, and email ID in a simple and clear form.
- **Bulk Download**: Download multiple images at once based on the provided keyword.
- **Input Validation**: Ensures all fields are properly filled with valid data.
- **Error Handling**: Displays informative error messages for invalid inputs or issues during download.

## Requirements

- Python 3.x
- PyQt5
- `download_google_imgs` library

## Installation

1. Clone this repository or download the code.
2. Install the required dependencies:
   ```bash
   pip install PyQt5 download_google_imgs
   ```

## Usage

1. Run the application:
   ```bash
   python bulk_image_downloader.py
   ```
2. Enter the following details in the GUI:
   - **Key Word**: The search term for the images (e.g., "Bike").
   - **# of Images**: The number of images to download (e.g., 100).
   - **Email Id**: Your email address (for reference purposes).
3. Click the **Submit** button to start downloading the images.

## Project Structure

- `bulk_image_downloader.py`: Main application script.
- `README.md`: Documentation for the project.

## Notes

- Ensure that the `download_google_imgs` library is correctly installed and configured for downloading images.
- The downloaded images will be stored in the `google_images` folder in the current working directory.

## License

This project is licensed under the MIT License.

---

Developed with ❤️ using Python and PyQt5.
