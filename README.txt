
# Project: Comparative Analysis and Development of an Identity Detection Tool

## Overview

This project focuses on enhancing cybersecurity by developing a comprehensive tool that assists users in identifying and mitigating email breaches. The project is divided into two primary objectives:

Develop a Threat Model:

The threat model is designed to verify if an email address has been compromised in any known data breaches.
If a breach is detected, the model further evaluates the sensitivity of the associated password, determining whether it is commonly used or easily guessable.
Users are promptly informed about the status of their email and password, with recommendations for immediate action, such as changing the password, if necessary.
Build a Scraping Tool and User Interface:

The project includes the development of a scraping tool that collects publicly available leaked data.
The scraped data is securely stored in a MongoDB database, which serves as a critical data source for the threat model.
Alongside the scraping tool, a user-friendly web interface is provided, enabling users to upload text files containing potentially leaked data.
The uploaded files are automatically processed, and the data is securely stored in MongoDB, ensuring that the database remains updated with the latest information.
Through these two components, the project aims to provide a robust solution for detecting email breaches and assessing password security, empowering users to take proactive steps in safeguarding their personal information.


## Prerequisites

- Python 3.12
- Flask
- MongoDB
- Required Python packages listed in `requirements.txt`

## Installation

1. **Clone the repository:**

   \`\`\`bash
   git clone <repository-url>
   cd Project
   \`\`\`

2. **Install the required packages:**

   Make sure you have Python 3 installed. You can install the necessary packages using pip:

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. **Set up MongoDB:**

   Ensure MongoDB is installed and running on your machine. The application is configured to connect to MongoDB using default settings. Adjust the connection settings in the code if necessary.

## Running the Application

To run the application, follow these steps:

1. **Open Command Prompt in Administrator Mode:**

   Open Command Prompt with administrator privileges to ensure the application runs smoothly.

2. **Navigate to the project directory:**

   \`\`\`bash
   cd Project
   \`\`\`

3. **Run the Flask application:**

   \`\`\`bash
   python app3.py
   \`\`\`

4. **Access the application:**

   - To upload leaked data, open your web browser and navigate to `http://127.0.0.1:5000`.
   - To use the email breach detection feature, the development server will be available at `http://127.0.0.1:5005`.

## How It Works

### 1. Leaked Data Processing and Storage (Code 1)

- The application reads a text file containing leaked data.
- The data is cleaned and processed before being securely stored in the MongoDB database.

### 2. User Interface for Data Upload (Code 2)

- The Flask app provides an upload page where users can submit text files containing leaked data.
- The uploaded files are automatically processed and stored securely in MongoDB.

# MongoDB Leak Data

The MongoDB leak data is in json format. Due to the large size of the data, it has been uploaded on cloud for accessing

## Accessing the Data

### Cloud Storage
The full dataset (1.23GB) can be downloaded from the following link:
[Download Full Dataset](https://drive.google.com/file/d/1YiUjud9P6t44gultkjzJkBukugWQ3RdA/view?usp=sharing)



### 3. Email Breach Detection (Code 3)

- Users can check if their email addresses have been breached.
- If a breach is detected, the application checks the sensitivity of the associated password and informs the user about potential risks.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask Documentation: [Flask](https://flask.palletsprojects.com/)
- MongoDB Documentation: [MongoDB](https://www.mongodb.com/docs/)
