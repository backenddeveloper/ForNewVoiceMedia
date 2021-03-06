import sys

from cli.exceptions import FinishedException, ValidationException
from cli.main import Main

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
                print promise.message
                promise = promise.dispatch(sys.stdin)

        except FinishedException, exception:
            print promise.message
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
