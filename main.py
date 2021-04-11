from flask import Flask, Blueprint
from flask.globals import request
from flask.json import jsonify
from flasgger import Swagger
import pytube

app = Flask(__name__)  # inicializa a API
Swagger(app)


@app.route('/', methods=['GET'])
def index():
    """
    API Download yutube videos
    ---
    tags:
      - uTube download videos
    parameters:
      - name: url
        in: path
        type: string
        required: true
        description: URL youtube
    responses:
      500:
        description: Internal Server Error!
      200:
        description: Sucess!
        schema:
          id: url
          properties:
            url:
              type: string
              description: url
              default: JSON

    """
    return youtube_download()


def youtube_download():
    # Parametros inseridos formato JSON (Postman)

    url = request.json['url']
    youtube = pytube.YouTube(url)

    for stream in youtube.streams:
        print(stream)

    pytube.YouTube(url).streams.get_highest_resolution().download('_downloads')

    return jsonify('Sucesso')


if __name__ == '__main__':
    app.run(debug=True)  # executa a aplicação
