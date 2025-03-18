from flask import *
from flask_cors import CORS
import block_coding


app = Flask(__name__)
CORS(app)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/block-coding", methods=["POST"])
def block_coding_4B5B():
    if request.method == "POST":
        binary_seq = request.form["binary_sequence"]

        pattern, new_pattern, img = block_coding.map_4B5B(binary_seq)
        
        return render_template("index.html", plot_url=img)


if __name__ == "__main__":
    app.run(debug=True)
