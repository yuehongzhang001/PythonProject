from flask_script import Manager
from c1 import app

manager = Manager(app)

@manager.option('-n','--name',dest='name',default='nowcoder')
@manager.option('-u','--url',dest='url')
def hello(name,url):
    print 'hello ',name,url

@manager.command
def initialize_database():
    print 'initializing...'

if __name__=='__main__':
    manager.run()