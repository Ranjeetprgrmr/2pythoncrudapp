# To activate the virtual environment = source venv/Scripts/activate
# To deactivate the virtual environment = source venv\Scripts\deactivate
# To generate the requirements.txt file = pip freeze > requirements.txt


# superuser credentials
# Username (leave blank to use 'lenovo'): 
# Email address: 
# Password: password
# Password (again): password

# register user
# username = manager1
# password = password123!@#



# pushing the code to github

# PS E:\PYTHON\2pythonCrudAppDeployed-CWD> git init
# Reinitialized existing Git repository in E:/PYTHON/2pythonCrudAppDeployed-CWD/.git/
# PS E:\PYTHON\2pythonCrudAppDeployed-CWD> git add .
# PS E:\PYTHON\2pythonCrudAppDeployed-CWD> git commit -m "initial commit"
# On branch main
# nothing to commit, working tree clean
# PS E:\PYTHON\2pythonCrudAppDeployed-CWD> git remote add origin https://github.com/Ranjeetprgrmr/2pythoncrudapp.git
# PS E:\PYTHON\2pythonCrudAppDeployed-CWD> git remote -v
# origin  https://github.com/Ranjeetprgrmr/2pythoncrudapp.git (fetch)
# origin  https://github.com/Ranjeetprgrmr/2pythoncrudapp.git (push)
# PS E:\PYTHON\2pythonCrudAppDeployed-CWD> git push origin master
# error: src refspec master does not match any
# error: failed to push some refs to 'https://github.com/Ranjeetprgrmr/2pythoncrudapp.git'
# PS E:\PYTHON\2pythonCrudAppDeployed-CWD> git remote add origin https://github.com/Ranjeetprgrmr/2pythoncrudapp.git
# error: remote origin already exists.
# PS E:\PYTHON\2pythonCrudAppDeployed-CWD> git push -u origin main
# Enumerating objects: 56, done.
# Counting objects: 100% (56/56), done.
# Delta compression using up to 12 threads
# Compressing objects: 100% (52/52), done.
# Writing objects: 100% (56/56), 26.02 KiB | 783.00 KiB/s, done.
# Total 56 (delta 6), reused 0 (delta 0), pack-reused 0 (from 0)
# remote: Resolving deltas: 100% (6/6), done.
# To https://github.com/Ranjeetprgrmr/2pythoncrudapp.git
#  * [new branch]      main -> main
# branch 'main' set up to track 'origin/main'.
# PS E:\PYTHON\2pythonCrudAppDeployed-CWD> 



# Render deployment successfull with this added as environment variable in render 
# DJANGO_SETTINGS_MODULE=crm.settings
# PYTHONPATH=/opt/render/project/src/crm
# DISABLE_COLLECTSTATIC=0

# build command in render
# pip install -r requirements.txt && python manage.py collectstatic --noinput