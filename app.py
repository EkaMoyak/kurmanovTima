from flask import Flask

# Инициализация приложения Flask
app = Flask(__name__)

# Импорт маршрутов из routes.py
import routes

if __name__ == "__main__":
    # Запуск приложения
    app.run(debug=True)