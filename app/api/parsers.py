from flask_restful import reqparse

client_get_parser = reqparse.RequestParser()
client_post_parser = reqparse.RequestParser()
client_put_parser = reqparse.RequestParser()
client_delete_parser = reqparse.RequestParser()

client_get_parser.add_argument(
    'page',
    type=int,
    location=['json', 'args', 'headers'],
    required=False
)

client_post_parser.add_argument('name', type=str, required=True)
