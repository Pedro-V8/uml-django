# Django UML Generator

Uml-Django is a library that aims to convert project models into a UML diagram, indicating their attributes, methods and the relationships of all entities.

## How it Works

From a file created at the root of the project (this is an important step that will be demonstrated below), it will be necessary to create an instance of the Library Class, passing the path to the project's "settings.py" file as a parameter.

With this configuration duly performed and executing the created file, an inspection will be carried out throughout the project in search of all the models of the apps present. Once identified, their attributes, methods, and their relationships with other models, if any, will be saved.

After that, a png file named "class diagram.png" will be created (also in the project root) with a simple class diagram of all classes of the identified models.

## Installation and Usage

Before starting the installation, below are important guidelines to ensure the proper functioning of the application.

- Make sure that python and pip are properly updated, in the current release the library was created with python Python 3.9.6 and Pip 21.2.4. Be with equal or higher versions.

- Install in the same environment as the project's dependencies, for example with the python virtual environment activated (venv), so that the inspection is effective.


1.  Start by downloading the "django_uml" dependency via pip

```
pip3 install uml-django
```

2. Create a .py file at the root of the project (this step is important), below is an example of a simple project and the extension file called "inspect_class.py"

```
.
├── db.sqlite3
├── django_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── app_01/
├── app_02/
└── app_03/
├── requirements.txt
├── inspect_class.py <---
├── venv

```
- The project has 3 apps and the "django_project" directory where the configuration file "settings.py" is located. In addition, the file "inspect_class.py" was added to the root of the project

3. With the file created, just follow the code below, which consists of instantiating an object and parameterizing the path to the project's "settings.py" file, then just call two functions as shown below.

```
from uml_django.inspect import Inspect

inspect_obj = Inspect('django_project.settings')

inspect_obj.inspect()
inspect_obj.create_UML()
```

4. Run the file "inspect_class.py"

```
python3 inspect_class.py
```

After the guidelines, the png file with the diagram will appear in the root of the project with the name "class_diagram.png", containing all the project models synthesized in a class diagram

## Final Considerations
This is an Open-Source project, so you are free to receive suggestions for improvements and enhancements to ensure the quality and viability of the code.
This communication will be very effective if applied in Issues and PR's openings so that the maintainers can discuss and implement new ideas and bug fixes.