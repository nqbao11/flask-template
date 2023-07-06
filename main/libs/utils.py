from flask import Response


def make_json_response(dumped_payload: str):
    return Response(dumped_payload, status=200, mimetype="application/json")
