from flask import Flask, jsonify, request
from json import dumps, loads, JSONEncoder
from tarefa import Tarefa

app = Flask(__name__)

t1 = (Tarefa("Pedro", "implementar Autenticação", "pendente").__dict__)
t2 = (Tarefa("Marcos", "Alguma outra coisa", "concluido").__dict__)
t3 = (Tarefa('Leandro', "implementar Autenticação", "concluido").__dict__)

tarefas = [t1, t2, t3]

@app.route('/', methods=['GET', 'POST', 'DELETE', 'PUT'])
def tarefa():

    global tarefas

    if request.method == 'GET':
        return jsonify(tarefas)

    elif request.method == 'POST':
        tarefa = loads(request.data)
        tn = Tarefa.from_json(tarefa)
        tarefas.append(tn.__dict__)
        return jsonify({"Id_nova_tarefa" : tn.id})

    elif request.method == 'DELETE':
        id_search= request.args.get("id")
        tarefas = list(filter(lambda tarefa: tarefa['id'] != id_search, tarefas))
        return jsonify(tarefas)

    elif request.method == 'PUT':
        id_search = request.args.get('id')
        pos= -1
        for t in range(tarefas.__len__()):
            if tarefas[t]['id'] == id_search:
                pos=t
                break
        if pos != -1:

            tarefa = loads(request.data)
            changes = Tarefa.from_json(tarefa)
            tarefas[pos]['responsavel'] = changes.responsavel
            tarefas[pos]['tarefa'] = changes.tarefa
            tarefas[pos]['status'] = changes.status
            return jsonify(sucess=True)
        else:
            return jsonify(sucess=False)


if __name__ == "__main__":
    app.run(debug=True)