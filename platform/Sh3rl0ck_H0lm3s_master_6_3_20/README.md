# Serious Game: Sh3rlock H0lme$

## Requirements
Before installing the python requirements it is necessary to have certain libraries installed on the developer machine depending on the environment:
##### Windows
It is necessary to have [Microsoft Visual C++ 14.0](https://visualstudio.microsoft.com/es/downloads/). The steps to follow are those:
1. Go to the web https://visualstudio.microsoft.com/es/downloads/.
2. Download _Visual Studio 2019_, specifically the ___Community___ version and run the installer.

3. In the Workloads tab select the following component:
    * _Development for the desktop with C++_ (within the Windows section)


#####Linux
It is necessary that the environment has python installed and the development dependencies:
```bash
sudo apt update && sudo apt install python3 python3-pip python3-dev default-libmysqlclient-dev postgresql libpq-dev
```
<!-- You need to have installed:
- [Django](https://docs.djangoproject.com/en/2.2/intro/install/#install-django)
- [Django Data Importer](https://django-data-importer.readthedocs.io/en/latest/index.html) to be able to bind cases in xml to python objects.
- [Django bootstrap4](https://django-bootstrap4.readthedocs.io/en/latest/#)
-->

##### Python Libraries
All the python library requirements are in the requirements.txt file and to install everything it is only necessary to execute:
```bash
pip install -r requirements.txt
```
In the event that you are in a windows environment, the mysqlclient library will give an error, this particular library must be installed manually:
1. Go to the URL [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient).
2. Download the compatible version for your windows and your python version.
3. Manually install the downloaded file by going to the path where it is and running:
    ```bash
    pip install mysqlclient-1.4.4-cp37-cp37m-win32.whl
    ```

## Model generation
For the generation of the game model, XML schemas are used for its definition. In this way your later
importing via XML will force the data to have the desired structure.

The [_generateDS_](http://www.davekuhlman.org/generateDS.html) utility is used to generate the model. In the project
you will find the _generateDS_ folder with everything you need. However, it may be necessary to install
the tool.

Requires python to have the six, requests, and lxml dependencies installed. To install it, execute the following command:
```bash
pip install six requests lxml
```

To generate the models through an XSD you have to execute the following command in the terminal being located in the
_generateDS_ directory.

```bash
python gends_run_gen_django.py -f -v --no-class-suffixes ../game/static/xsd/<schema>.xsd
```

This will generate multiple files, the important ones for the project are _models.py_, _forms.py_ and _admin.py_ whose
content can be copied into the project files themselves. Another important generated file is _schemalib.py_,
which should be copied to the parsers directory. This file is the one who processes a linked input xml
with the schema and returns an object with the data for later import into the database.

# Prepare Docker server
Docker needs to be configured for remote api's. For this it is necessary to add the following line at the end of the
/etc/default/docker file
```
DOCKER_OPTS="-H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock"
```
The next step is to restart the Docker service:
```
sudo systemctl daemon-reload
sudo service docker restart
```


## Start guacamole apache server with docker

It is necessary to download the image of the guacamole server on the docker server, for this you have to execute the following
 statement on the machine running docker:
```bash
docker pull guacamole/guacd
```
Although when the application starts up it checks that the docker container with the guacamole apache server is
active and if not, it lifts it, if you want to start it manually you have to execute the following command:
```bash
docker run --rm --name guacd -d -p 4822:4822 guacamole/guacd
```

## Compile localized literals

You need to have the gettext tools utility installed.
##### linux
```bash
sudo apt install gettext
```
#####windows
* You need to download the installer from [this page](https://mlocati.github.io/articles/gettext-iconv-windows.html) with Flavor _static_ and install it.
 
 To compile the literals that are in the application, either in the different python modules or in the templates, there is
than run the following command:
```bash
python manage.py makemessages --ignore=generateDS* --ignore=importer/parsers/* --ignore=venv/* --locale sp
```
In this case we are transferring the messages to the .po file corresponding to Spanish.

## Compilation of SCSS styles

If you want to compile the .scss files so that the .css is generated, you have to execute the following co
