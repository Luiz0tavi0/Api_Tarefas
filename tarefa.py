#tarefa.py
import uuid
from builtins import classmethod
import json


class Tarefa:
    def __init__(self, responsavel, tarefa, status):
        self.id = uuid.uuid4().__str__()
        self.responsavel = responsavel
        self.tarefa = tarefa
        self.status = status

    @classmethod
    def from_json(cls, json):
        instance = cls(json['responsavel'], json['tarefa'], json['status'])
        #json_dict= json.loads(json_string)
        return instance#cls(**json_string)