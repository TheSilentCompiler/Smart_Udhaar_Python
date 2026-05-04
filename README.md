Smart Udhaar v4.0 - Enterprise Ledger
Smart Udhaar is a high-performance desktop application designed for small to medium enterprises to manage credit (Udhaar) transactions, monitor customer debt, and assess credit risk in real-time. Built with a modern, dark-themed UI, it provides a seamless experience for shopkeepers and administrators to maintain financial transparency.

✨ Features
Secure Authentication: Admin-level login protection to ensure data privacy.

Real-time Dashboard: Instantly view total market debt, inventory count, and high-risk customers.

Customer Directory: Comprehensive list of all registered customers with their total outstanding balances.

Detailed Udhaar Tracking: Granular tracking of every item purchased on credit, including quantity, unit price, and timestamps.

Credit Analysis & Risk Assessment: Automated grading system that flags "Blacklisted" customers based on their credit scores.

Modern UI/UX: Built using customtkinter for a responsive, high-definition dark mode interface.

🛠️ Tech Stack
Frontend: CustomTkinter (Modernized Tkinter library)

Language: Python 3.x

Database: MySQL / PostgreSQL (via db_config)

Styling: ttk Custom Themes

🚀 Installation & Setup
1. Clone the Repository
Bash
git clone https://github.com/TheSilentCompiler/Smart_Udhaar_Python.git
cd smart-udhaar
2. Install Dependencies
Ensure you have the required libraries installed:

Bash
pip install customtkinter mysql-connector-python
3. Database Configuration
Create a db_config.py file in the root directory to handle your database connection:

Python
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="smart_udhaar_db"
    )
4. Run the Application
Bash
python main.py
🖥️ Usage Guide
Login: Use the default credentials (Username: admin, Password: admin123).

Home: Check the "System Statistics" cards for a quick health check of your business finances.

Add Customer: Use the sidebar to register new clients with their CNIC and contact details.

Tracking: Navigate to "Udhaar Item Tracking" to see exactly which products were taken on credit and when.

Risk Management: Monitor the "Credit Analysis" tab to identify customers with low safety scores.

📂 Project Structure
main.py: The entry point of the application containing the UI logic.

db_config.py: Database connection utility.

assets/: (Optional) Icons and images used in the application.

🛡️ Security Note
The current version uses a hardcoded admin login for demonstration purposes. For production environments, it is recommended to move authentication to a hashed database table.

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request