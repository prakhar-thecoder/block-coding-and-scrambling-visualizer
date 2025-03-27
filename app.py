from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from block_coding import map_4B5B, map_8B10B
from scrambling import B8ZS, HDB3
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/block-coding",methods=["GET", "POST"])
def block_coding():
    if request.method == "POST":
        binary_sequence = request.form.get("binary_sequence")
        encoding_type = request.form.get("encoding")

        if encoding_type == "4B5B":
            _, blocked_signal, plot_url = map_4B5B(binary_sequence)
        elif encoding_type == "8B10B":
            _, blocked_signal, plot_url = map_8B10B(binary_sequence)
        else:
            blocked_signal = []
            plot_url = None

        binary_sequence = [bit for bit in _]
        binary_sequence = " ".join(binary_sequence)    
        blocked_string = " ".join(map(str, blocked_signal))
        return render_template("block_code.html", binary_sequence=binary_sequence, encoding_type=encoding_type, blocked_string=blocked_string, plot_url=plot_url)

    return render_template("block_code.html", binary_sequence=None, encoding_type=None, blocked_string=None, plot_url=None)


@app.route("/scrambling", methods=["GET", "POST"])
def scrambling():
    if request.method == "POST":
        binary_sequence = request.form.get("binary_sequence")
        encoding_type = request.form.get("encoding")

        if encoding_type == "B8ZS":
            _, scrambled_signal, plot_url = B8ZS(binary_sequence)
        elif encoding_type == "HDB3":
            _, scrambled_signal, plot_url = HDB3(binary_sequence)
        else:
            scrambled_signal = []
            plot_url = None

        binary_sequence = [bit for bit in _]
        binary_sequence = " ".join(binary_sequence)    
        scrambled_string = " ".join(map(str, scrambled_signal))
        return render_template("scrambling.html", binary_sequence=binary_sequence, encoding_type=encoding_type, scrambled_string=scrambled_string, plot_url=plot_url)

    return render_template("scrambling.html", binary_sequence=None, encoding_type=None, scrambled_string=None, plot_url=None)

@app.route('/all-in-one', methods=["GET", "POST"])
def all_in_one():
    if request.method == "POST":
        binary_sequence_input = request.form.get("binary_sequence")
        
      
        binary_sequence_output_1, scrambled_signal_1, plot_url_1 = B8ZS(binary_sequence_input)
        binary_sequence_output_2, scrambled_signal_2, plot_url_2 = HDB3(binary_sequence_input)
        binary_sequence_output_3, blocked_signal_1, plot_url_3 = map_4B5B(binary_sequence_input)
        binary_sequence_output_4, blocked_signal_2, plot_url_4 = map_8B10B(binary_sequence_input)

       
        binary_sequence_display = " ".join(binary_sequence_input)
        scrambled_string_1 = " ".join(map(str, scrambled_signal_1))
        scrambled_string_2 = " ".join(map(str, scrambled_signal_2))
        blocked_string_1 = " ".join(map(str, blocked_signal_1))
        blocked_string_2 = " ".join(map(str, blocked_signal_2))

        return render_template(
            "all_in_one.html",
            binary_sequence=binary_sequence_display,
            scrambled_string_1=scrambled_string_1,
            scrambled_string_2=scrambled_string_2,
            blocked_string_1=blocked_string_1,
            blocked_string_2=blocked_string_2,
            plot_url_1=plot_url_1,
            plot_url_2=plot_url_2,
            plot_url_3=plot_url_3,
            plot_url_4=plot_url_4
        )


    return render_template(
        "all_in_one.html",
        binary_sequence=None,
        scrambled_string_1=None,
        scrambled_string_2=None,
        blocked_string_1=None,
        blocked_string_2=None,
        plot_url_1=None,
        plot_url_2=None,
        plot_url_3=None,
        plot_url_4=None
    )



    

if __name__ == "__main__":
    app.run(debug=True)
