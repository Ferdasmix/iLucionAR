import pandas as pd
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QMessageBox


class FeedbackForm(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the feedback form
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        self.comment_label = QLabel("Comment:")
        self.comment_input = QTextEdit()
        self.submit_button = QPushButton("Submit")

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.comment_label)
        layout.addWidget(self.comment_input)
        layout.addWidget(self.submit_button)

        # Set up the window
        self.setLayout(layout)
        self.setWindowTitle("Feedback Form")
        self.show()

        # Connect the button to the submit function
        self.submit_button.clicked.connect(self.submit)

    def submit(self):
        # Get the input values
        name = self.name_input.text()
        email = self.email_input.text()
        comment = self.comment_input.toPlainText()

        # Compile data into a DataFrame
        data = {'Name': [name], 'Email': [email], 'Comment': [comment]}
        df = pd.DataFrame(data)

        # Create the "feedback" subdirectory if it doesn't already exist
        if not os.path.exists("feedback"):
            os.makedirs("feedback")

        # Check if the "INFO.xlsx" file exists in the "feedback" directory
        file_path = os.path.join(os.getcwd(), "feedback", "INFO.xlsx")
        if os.path.exists(file_path):
            # Append data to existing Excel file
            existing_df = pd.read_excel(file_path)
            updated_df = pd.concat([existing_df, df], ignore_index=True)
            updated_df.to_excel(file_path, index=False)
        else:
            # Create new Excel file
            df.to_excel(file_path, index=False)

        # Display confirmation message
        QMessageBox.information(self, "Feedback Submitted", "Thank you for your feedback!")


if __name__ == '__main__':
    # Create the application
    app = QApplication([])

    # Create the feedback form
    feedback_form = FeedbackForm()

    # Run the application
    app.exec_()
