from flask import Flask, request, render_template_string, send_from_directory
import random

app = Flask(__name__)

@app.route('/style.css')
def css():
    return send_from_directory('.', 'style.css')


@app.route("/", methods=["GET", "POST"])
def game():

    result = ""
    user_choice = ""
    computer_choice = ""

    if request.method == "POST":

        youDict = {
            "snake": 1,
            "water": -1,
            "gun": 0
        }

        reverseDict = {
            1: "Snake 🐍",
            -1: "Water 💧",
            0: "Gun 🔫"
        }


        youstr = request.form["choice"]

        you = youDict[youstr]

        computer = random.choice([-1, 0, 1])


        user_choice = reverseDict[you]
        computer_choice = reverseDict[computer]


        if computer == you:
            result = "It's a Draw! 🤝"

        elif computer == -1 and you == 1:
            result = "You Win! 🎉"

        elif computer == -1 and you == 0:
            result = "You Lose! 😢"

        elif computer == 1 and you == -1:
            result = "You Lose! 😢"

        elif computer == 1 and you == 0:
            result = "You Win! 🎉"

        elif computer == 0 and you == -1:
            result = "You Win! 🎉"

        elif computer == 0 and you == 1:
            result = "You Lose! 😢"


    with open("index.html", "r") as file:
        html = file.read()


    html = html.replace("{{result}}", result)
    html = html.replace("{{user_choice}}", user_choice)
    html = html.replace("{{computer_choice}}", computer_choice)


    return render_template_string(html)


if __name__ == "__main__":
    app.run(debug=True)