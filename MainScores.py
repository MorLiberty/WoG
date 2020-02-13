from flask import Flask

score_file_name = "Scores.txt"


def score_server():
    try:
        app = Flask(__name__)
        file_dict = eval(open(score_file_name, "r+").read())
        name = list(file_dict)[-1]
        score = file_dict[name]

        @app.route('/')
        def index():
            return """
                <html>
                    <head>
                        <title>Scores Game</title>
                    </head>
                    <body>
                        <h1><div id="score" style="color:blue">Hey {} Your score is {}</h1>
                    </body>
                </html>
            """.format(name, score)

        if __name__ == '__main__':
            app.run(debug=True, host='0.0.0.0')

    except FileNotFoundError:
        app = Flask(__name__)

        @app.route('/')
        def error():
            return """
                <html>
                    <head>
                        <title>Scores Game</title>
                    </head>
                    <body>
                    <body>
                        <h1><div id="score" style="color:red">Your name isn't exists</div></h1>
                    </body>
                </html>
            """

        if __name__ == '__main__':
            app.run(debug=True, host='0.0.0.0')


score_server()
