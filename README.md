# Contact-Book-Project

📒 Contact Book (Python CLI App)
A simple Contact Book application built using Python that allows you to add, view, search, update, and delete contacts. Contacts are stored in a local contacts.json file.

✅ Features
📥 Add new contacts

📄 View all saved contacts

🔍 Search contact by name or phone

✏️ Update existing contact details

🗑️ Delete a contact

💾 Data persistence using JSON file

📁 File Structure
bash
Copy
Edit
contact_book/
│
├── main.py               # Main menu to run the app
├── contact_manager.py    # All contact management logic
└── contacts.json         # JSON file to store contacts (created automatically)
🧑‍💻 How to Run
Clone or Download this repository.

Make sure you have Python 3.x installed.

Run the application:

bash
Copy
Edit
python main.py
Note: Ensure contact_manager.py is in the same directory as main.py.

📌 Sample Functionalities
1. Add Contact
yaml
Copy
Edit
Enter name: John Doe
Enter phone: 9800000000
Enter email: john@example.com
Enter address: Kathmandu
2. View Contacts
Displays a numbered list of all saved contacts with their details.

3. Search Contact
You can search by full or partial name/phone number.

4. Update Contact
Update only selected fields or leave blank to keep existing values.

5. Delete Contact
Confirmation is required before deletion.

🛠 Requirements
Python 3.x

No external libraries required (uses built-in json and os)

📂 Data Storage
All contacts are stored in a file named contacts.json in the same folder. If the file doesn’t exist, it is created automatically on first run.

🔒 License
This project is open-source and free to use under the MIT License.
