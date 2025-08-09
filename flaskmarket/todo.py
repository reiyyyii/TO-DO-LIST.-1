from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

tasks = []

@app.route("/", methods = ["GET", "POST"])
def home():
    
    if request.method == "POST":
         task = request.form.get("task")
         if task:
             if len(tasks) >=5:
                 tasks.pop(0)
         tasks.append(task)
    return render_template("index.html", tasks = tasks)

@app.route("/reset", methods = ["POST"])
def reset():
    tasks.clear()
    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run(debug = True)