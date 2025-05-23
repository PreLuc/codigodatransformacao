import json

def carregar_tarefas(caminho='dados.json'):
    try:
        with open(caminho, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas, caminho='dados.json'):
    with open(caminho, 'w') as f:
        json.dump(tarefas, f, indent=4)
