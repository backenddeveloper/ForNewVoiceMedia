from jinja2 import Environment, FileSystemLoader


class View:

    @staticmethod
    def render(template, args=None):
        loader = FileSystemLoader('cli/templates')
        return \
            Environment(loader=loader).get_template(template).render(args=args)
