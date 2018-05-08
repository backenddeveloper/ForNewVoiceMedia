import sys

from cli.exceptions import FinishedException, ValidationException
from cli.main import Main
from cli.view import View

if __name__ == '__main__':
    
    '''
    First we remove the name of this script from the arguments
    '''
    sys.argv.pop(0)
    arguments = sys.argv

    while True:

        try:
            promise = Main(arguments)
            while True:
                print promise.get_message()
                promise = promise.dispatch(sys.stdin.readline())

        except FinishedException, exception:
            print promise.get_message()
            continue
        except KeyboardInterrupt, signal:
            print "caught signal, exiting cleanly"
            exit(0)
        except ValidationException, exception:
            print exception.message
            exit(1)
        except Exception, exception:
            print exception.message
            exit(2)
