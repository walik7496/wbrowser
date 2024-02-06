import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTextBrowser, QAction, QTabWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings


class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("wbrowser")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.tabs = QTabWidget()
        self.layout.addWidget(self.tabs)

        self.add_new_tab()

        self.nav_bar_layout = QHBoxLayout()
        self.layout.addLayout(self.nav_bar_layout)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.current_tab_browser.back)
        self.nav_bar_layout.addWidget(self.back_button)

        self.forward_button = QPushButton("Forward")
        self.forward_button.clicked.connect(self.current_tab_browser.forward)
        self.nav_bar_layout.addWidget(self.forward_button)

        self.reload_button = QPushButton("Reload")
        self.reload_button.clicked.connect(self.current_tab_browser.reload)
        self.nav_bar_layout.addWidget(self.reload_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.nav_bar_layout.addWidget(self.url_bar)

        self.go_button = QPushButton("Go")
        self.go_button.clicked.connect(self.navigate_to_url)
        self.nav_bar_layout.addWidget(self.go_button)

    def add_new_tab(self):
        browser = QWebEngineView()
        browser.setUrl(QUrl("http://www.google.com"))
        self.tabs.addTab(browser, "New Tab")
        browser.urlChanged.connect(self.update_url_bar)
        self.current_tab_browser = browser

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith('http'):
            url = 'http://' + url
        self.current_tab_browser.setUrl(QUrl(url))

    def closeEvent(self, event):
        for i in range(self.tabs.count()):
            browser = self.tabs.widget(i)
            settings = browser.settings()
            settings.clearAll()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec_())
