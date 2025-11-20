import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
import time

def init():
    app = QApplication(sys.argv)

    html = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HtmlPlaceholderDesktop</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(135deg, #89f7fe, #66a6ff);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      min-height: 100vh;
      padding-top: 50px;
      margin: 0;
    }
    h1 {
      color: #fff;
      text-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }
    textarea {
      width: 80%;
      max-width: 800px;
      height: 400px;
      padding: 15px;
      font-size: 16px;
      border-radius: 10px;
      border: none;
      box-shadow: 0 4px 15px rgba(0,0,0,0.2);
      resize: vertical;
    }
  </style>
</head>
<body>
  <h1>HtmlPlaceholderDesktop</h1>
  <h3>Введите код</h3>

  <textarea id="myTextarea" rows="30" cols="60">index.html</textarea>
  <button id="openBtn">Открыть</button>

  <script>
    let code = document.getElementById("myTextarea");

    document.getElementById("openBtn").onclick = () => {
      let content = code.value;
      document.open();
      document.write(content);
      document.close();
    };
  </script>
</body>
</html>"""

    view = QWebEngineView()
    view.setHtml(html)
    view.show()

    sys.exit(app.exec())

# Запуск
if __name__ == "__main__":
    print("нужный модуль  для Htmlplaceholder")
    time.sleep(158)
