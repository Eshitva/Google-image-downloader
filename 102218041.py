from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
import sys
from download_google_imgs import downloader


class BulkImageDownloaderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Main layout
        layout = QVBoxLayout()

        # Title
        title_label = QLabel("Interface: Download bulk images")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: red;")
        layout.addWidget(title_label)

        # Keyword input
        keyword_layout = QHBoxLayout()
        keyword_label = QLabel("Key Word:")
        self.keyword_input = QLineEdit()
        keyword_layout.addWidget(keyword_label)
        keyword_layout.addWidget(self.keyword_input)
        layout.addLayout(keyword_layout)

        # Number of images input
        num_images_layout = QHBoxLayout()
        num_images_label = QLabel("# of Images:")
        self.num_images_input = QLineEdit()
        num_images_layout.addWidget(num_images_label)
        num_images_layout.addWidget(self.num_images_input)
        layout.addLayout(num_images_layout)

        # Email ID input
        email_layout = QHBoxLayout()
        email_label = QLabel("Email Id:")
        self.email_input = QLineEdit()
        email_layout.addWidget(email_label)
        email_layout.addWidget(self.email_input)
        layout.addLayout(email_layout)

        # Submit button
        submit_button = QPushButton("Submit")
        submit_button.setStyleSheet("background-color: orange; color: white; font-weight: bold;")
        submit_button.clicked.connect(self.download_images)
        layout.addWidget(submit_button)

        # Set layout
        self.setLayout(layout)
        self.setWindowTitle("Bulk Image Downloader")
        self.setGeometry(300, 300, 400, 200)

    def download_images(self):
        keyword = self.keyword_input.text().strip()
        num_images = self.num_images_input.text().strip()
        email = self.email_input.text().strip()

        # Validation
        if not keyword:
            QMessageBox.critical(self, "Error", "Keyword is required!")
            return
        if not num_images.isdigit() or int(num_images) <= 0:
            QMessageBox.critical(self, "Error", "# of Images must be a positive integer!")
            return
        if "@" not in email or "." not in email:
            QMessageBox.critical(self, "Error", "Invalid Email ID!")
            return

        # Attempt to download images
        try:
            downloader.download(
                keyword,
                get_urls=False,
                output_name=None,
                num_images=int(num_images),
                root_dir="google_images",
                add_ons=["4k"],
                verbose=True,
            )
            QMessageBox.information(
                self, "Success", f"Downloaded {num_images} images for '{keyword}' successfully!"
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")


def main():
    app = QApplication(sys.argv)
    window = BulkImageDownloaderApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
