from pydantic import BaseModel, ConfigDict, Extra

from main.libs.utils import make_json_response


class BaseSchema(BaseModel):
    model_config = ConfigDict(
        extra=Extra.ignore,
        from_attributes=True,
        str_strip_whitespace=True,
    )

    @classmethod
    def jsonify(cls, value):
        payload = cls.model_validate(value).model_dump_json()
        return make_json_response(payload)
