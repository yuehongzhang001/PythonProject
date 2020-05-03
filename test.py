from decorator import log
@log(level='xxx')
def Hi():
    print 'hi'

Hi()