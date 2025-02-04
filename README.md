# wbrowser

wbrowser is a simple web browser built with PyQt5 and WebEngine for browsing web pages.

## 🚀 Features
- Tabbed browsing
- Navigation buttons: "Back", "Forward", "Reload"
- URL input field
- Automatically adds "http://" if the protocol is not specified

## 💡 Requirements
- Python 3.x
- PyQt5

## 🛠 Installation
1. Create a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate   # for Linux/macOS
   venv\Scripts\activate     # for Windows
   ```
2. Install dependencies:
   ```bash
   pip install PyQt5 PyQtWebEngine
   ```

## 🌐 Usage
Run the application:
```bash
python wbrowser.py
```

## 🌍 Code Structure
- **BrowserWindow:** Main class for the browser window
- **add_new_tab():** Adds a new tab with Google loaded
- **navigate_to_url():** Navigates to the entered URL
- **update_url_bar():** Updates the address bar when the URL changes
- **closeEvent():** Clears settings upon application closure

## 🌟 Future Improvements
- Adding bookmarks
- Browsing history support
- Dark mode theme settings

## 🚩 License
MIT License
