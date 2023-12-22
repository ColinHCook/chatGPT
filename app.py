from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Replace 'your_openai_api_key' with your actual OpenAI API key
openai.api_key = 'insert api key here'

import openai

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        question = request.form.get("question")
        if question:
            # Updated API call
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  
                messages=[{"role": "user", "content": question}]
            )
            answer = response['choices'][0]['message']['content']
            return render_template("index.html", answer=answer)
        else:
            return render_template("index.html", answer="Please enter a question.")
    return render_template("index.html", answer=None)



if __name__ == "__main__":
    app.run(debug=True)
