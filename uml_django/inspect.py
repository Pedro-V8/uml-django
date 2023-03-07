import os
import importlib
import inspect
import ast
import django

from plantuml import PlantUML


class Inspect():
    def __init__(self , settings):
        #os.environ['DJANGO_SETTINGS_MODULE'] = settings
        #django.setup()
        self.root = '.'        
        self.classLIST = []
        self.url = 'http://www.plantuml.com/plantuml/img/'

    def create_diagram(self , classes):
        uml = PlantUML(self.url)
        # Gerar imagem do diagrama de classe
        print("Generating UML...")
        image = uml.processes(classes)
        with open("class_diagram.png", "wb") as f:
            f.write(image)
        
        print("Diagram created successfully !")

    def create_UML(self):
        string_base = """
        @startuml
        """

        for item in self.classLIST:
            classe = f"""
            class {item['nome']} {{
            """
            for atributo in item['atributos']:
                classe += f"""
                - {atributo}
                """
            for metodo in item['metodos']:
                classe += f"""
                + {metodo}()
                """
            classe += f"""
            }}
            """
            string_base += classe
        for item in self.classLIST:
            if item['herda']:
                for herda in item['herda']:
                    string_base += f"""
                    {item['nome']} <-- {herda}
                    """
        string_base += "@enduml"
    
        self.create_diagram(string_base)

    def pega_classe(self , arquivo):
        arquivo_new = arquivo[2:].replace('/', '.')
        arquivo_classe = importlib.import_module(arquivo_new[:-3])
        
        for nome_classe , classe in inspect.getmembers(arquivo_classe, inspect.isclass):
            #print(classe.__module__)
            if classe.__module__ == arquivo_classe.__name__:
                classDict = {
                    'nome': nome_classe,
                    'atributos': [],
                    'metodos': [],
                    'herda': []
                }
                if len(classe.__bases__) > 0:
                    for base in classe.__bases__:
                        if base.__name__ != 'object':
                            classDict['herda'].append(base.__name__)
                
                tree = ast.parse(inspect.getsource(classe))
                for node in tree.body:
                    for member in node.body:
                        if isinstance(member, ast.FunctionDef):
                            #print(f"Método: {member.name}")
                            classDict['metodos'].append(member.name)
                        elif isinstance(member, ast.Assign): 
                            for target in member.targets:
                                #print(f"Atributo: {target.id}")
                                classDict['atributos'].append(target.id)
                    self.classLIST.append(classDict)


    def inspect_files(self , caminho='.'):
        # Lista todos os arquivos e diretórios no caminho especificado
        arquivos_e_diretorios = os.listdir(caminho)
        

        for item in arquivos_e_diretorios:
            caminho_completo = os.path.join(caminho, item)
            if os.path.isfile(caminho_completo):
                if item.endswith('.py') and 'models' in item:
                    print(f'Detected Model File => {item}')    
                    self.pega_classe(caminho_completo)

            elif os.path.isdir(caminho_completo):
                
                if item != '__pycache__' and item != 'venv' and item != '.git' and item != 'migrations':
                    print(f'Detected Dir => {item} , inspecting...')
                    # chama a função de listagem de arquivos novamente para o diretório encontrado
                    self.inspect_files(caminho_completo)
    
    def inspect(self):
        print("Inspecting...")
        self.inspect_files()
        print("Inspection successfully completed !")