import os
import time

def createFolder():
    os.mkdir('admin')
    os.mkdir('superadmin')
    os.mkdir('clientwidget')

def adminSetup():
    try:
        envFile = open('../admin/env.admin.development', 'r')
        os.chdir('admin')
        os.system("git clone -b admin https://gitlab.com/autovista/chatbot-frontend.git")
        os.chdir('chatbot-frontend')
        with open('.env.development', 'w') as envNew:
            for line in envFile:
                envNew.write(line)
            envFile.close()
        
        os.system('yarn install')
        os.chdir('../')
    except Exception as e:
        print('Something went wrong.')
        print(e)

def superadminSetup():
    try:
        envFile = open('../admin/env.superadmin.development', 'r')
        os.chdir('superadmin')
        os.system("git clone -b super-admin https://gitlab.com/autovista/chatbot-frontend.git")
        os.chdir('chatbot-frontend')
        with open('.env.development', 'w') as envNew:
            for line in envFile:
                envNew.write(line)
            envFile.close()
        
        os.system('yarn install')
        os.chdir('../')
    except Exception as e:
        print('Something went wrong.')
        print(e)

def clientwidgetSetup():
    try:
        envFile = open('../admin/env.superadmin.development', 'r')
        os.chdir('clientwidget')
        os.system("git clone -b new-ui https://gitlab.com/autovista/chatbot-frontend-clientwidget.git")

        os.chdir('chatbot-frontend-clientwidget')
        with open('.env.development', 'w') as envNew:
            for line in envFile:
                envNew.write(line)
            envFile.close()
        
        os.system('yarn install')
        os.chdir('../')
    except Exception as e:
        print('Something went wrong.')
        print(e)

if __name__=='__main__':
    print('Starting your system frontend setup..')
    time.sleep(3)
    createFolder()
    print('Folders created successfully..')
    print('Cloning admin....')
    adminSetup()
    print('admin cloned and builded successfully')
    print('Cloning superadmin....')
    superadminSetup()
    print('super-admin cloned and builded successfully')
    print('Cloning clientwidget....')
    clientwidgetSetup()
    print('clientwidget cloned and builded successfully')
    print('Now you can switch to any one folder and run "yarn start"')
