🔐 Secure Caesar Chat
A simple yet elegant web-based chat application built using Streamlit that encrypts and decrypts messages using the Caesar Cipher. This project focuses on privacy, ease of use, and a beautiful UI using a pastel-themed color palette.

<!-- (Optional: add a screenshot of your app) -->

✨ Features
🔒 End-to-end message encryption using Caesar Cipher

📝 Send & view decrypted messages with an easy-to-use interface

🎨 Modern pastel UI with custom styling (pink, purple, deep blue, beige palette)

💾 Persistent message storage in a text file (messages.txt)

🎈 Responsive design with tabs for sending and viewing messages

🛠️ Technologies Used
Streamlit – Python web app framework

Python 3.x – Core language

HTML/CSS – Custom UI styling using embedded CSS

⚡ Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/<your-username>/secure-caesar-chat.git
cd secure-caesar-chat
Install dependencies

bash
Copy
Edit
pip install streamlit
Run the app

bash
Copy
Edit
streamlit run app.py
Open in your browser: http://localhost:8501

📂 Project Structure
pgsql
Copy
Edit
secure-caesar-chat/
├── app.py           # Main Streamlit app
├── messages.txt     # Stores encrypted messages
├── .streamlit/      # (Optional) Custom theme config
└── README.md        # Project documentation
🧠 How it Works
Encryption: Messages are encrypted using Caesar Cipher with a user-defined shift.

Storage: Encrypted messages, along with shift values and timestamps, are stored in a messages.txt file.

Decryption: When viewing messages, the app automatically decrypts them using the stored shift value.

📸 Screenshots
Add screenshots or GIFs of the UI here!

🚀 Future Improvements
Add user authentication (login/logout system)

Use a database (SQLite / Firebase) instead of text file

Real-time chat using WebSockets

Multiple cipher options (Vigenère, AES, etc.)

🤝 Contributing
Contributions are welcome!

Fork the repo

Create a new branch (feature-branch)

Commit changes and submit a pull request

📜 License
This project is licensed under the MIT License – free to use and modify.

💡 Inspiration
This project was created to demonstrate how even classic cryptography like Caesar Cipher can be built into a functional and modern-looking web app.


VIDEO DEMO:
