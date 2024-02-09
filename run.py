from src.main.server.server import app

if __name__ == "__main__":
    print('Server is running on 0.0.0.0:3000')
    app.run(host='0.0.0.0', port=3000, debug=True)
