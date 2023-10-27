# restaurant-finder
Restaurant finder<br >

## File structure
<pre>
Project:
    data:
        data generated goes into this folder
    notebooks:
        jupyter notebooks goes into this folder
    src:
        __init__.py
        custom python modules goes into this folder
    .gitignore
    README.md
    requirements.txt
    setup.py
</pre>
## Setting up
### Run in venv
`> py -m venv <environment name>` <br >
`> <environment name>\Scripts\activate` <br >
`> pip install --upgrade pip` <br > 

### Install build and run
`> py -m pip install --upgrade pip` <br >

`> pip install -r requirements.txt` <br >
Use to install new packages. <br >
`> py -m manage_pip install|uninstall packages` <br >
`> jupyter-lab` <br >

### To execute restaurant function
`run last cell in restuarant.ipynb found in the notebook folder`

###
In jupyter notebook
Go to notebooks -> Demo-automation.ipynb
kernel -> Restart & Clear Output
cell -> Run all below

#### Run manage_pip.py
The use of `pip freeze > -l > requirements.txt` to update the packages has led to installation failure in some cases. <br >

The `pip freeze` command was found to appended incompatible local environments packages from source that are not required in a different installation setting. Run the command below when installing or uninstalling addtional packages to avoid installation failures. <br >

`> py manage_pip.py install|uninstall packages`

Running this script rather than pip to prevent appending all the installed packages from a local environment when adding other packages.

#### Run executable
`Go to app folder in dist folder click on app.exe to run`
`To build run- -> pyinstaller app.py ->  check app.spec -> pyinstaller app.spec`
