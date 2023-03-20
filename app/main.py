from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
  return "Get in there!"

if __name__ == '__main__':
  app.run(debug=True)