from flask import Flask
from flask.globals import request
from flask.json import jsonify
import pytube

app = Flask(__name__)  # inicializa a API


@app.route('/')  # cria uma rota
def main():
    # Parametros inseridos formato JSON (Postman)
    url = request.json['url']

    youtube = pytube.YouTube(url)

    for stream in youtube.streams:
        print(stream)

    from pytube import YouTube

    youtube = YouTube(url)

    pytube.YouTube(url).streams.get_highest_resolution().download('_downloads')

    # video = youtube.streams.get_highest_resolution()
    # video.download('/Downloads')

    # Retorna um resultado em JSON

    return jsonify('Sucesso')


# return jsonify({'resultado': resultado, 'media': media})

# Retorna resultado por um template html
# return render_template('index.html', media=media, resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)  # executa a aplicação
