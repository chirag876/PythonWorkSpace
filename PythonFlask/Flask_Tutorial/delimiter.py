# Jinga 2 template engine provides some delimiters which can be used in the HTML to make it capable of dynamic data representation. The template system provides some HTML syntax which are placeholders for variables and expressions that are replaced by their actual values when the template is rendered.

# The jinga2 template engine provides the following delimiters to escape from the HTML.

# {% ... %} for statements
# {{ ... }} for expressions to print to the template output
# {# ... #} for the comments that are not included in the template output
# # ... ## for line statements
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    name = "Chirag"
    age = 2

    return render_template("delimiter.html", name=name, age=age)
if __name__ == '__main__':  
   app.run(debug = True)  
