import sys
import optparse
from os import listdir, walk, getcwd
from os.path import split, join, abspath, isfile
from distutils.dir_util import copy_tree
from random import choice
from string import letters, digits, punctuation
from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = join(split(abspath(__file__))[0], 'template/')

def go_go_go():
    """ Copy templates to new location and trigger parse """

    usage = "usage: %prog [options] project_name [base_destination_dir]"
    parser = optparse.OptionParser(usage=usage)
    options, args = parser.parse_args()

    if len(args) not in (1, 2):
        parser.print_help()
        sys.exit(1)
    project_name = args[0]

    if len(args) > 1:
        base_dest_dir = args[1]
    else:
        base_dest_dir = ''
    dest = join(base_dest_dir, project_name)
    
    copy_tree(TEMPLATE_DIR, dest) # copy files over
    parse_templates(project_name, generate_secret_key(), dest) # trigger parse

def parse_templates(project_name, secret_key, dest_dir):
    """ Perform variable replacement in templates """

    env = Environment(loader=FileSystemLoader(dest_dir))
    includes = ['.gitignore', '.py']
    
    valid_templates = validate_templates(env.list_templates(), includes)

    for template_file in valid_templates:
        template = env.get_template(template_file)
        outfile = open(join(dest_dir, template_file), 'w')
        rendered_output = template.render(project_name=project_name, secret_key=generate_secret_key())
        outfile.write(rendered_output)
        outfile.close()

def generate_secret_key(length=50):
    """ Generates a simple secret key of variable length """

    chars = letters + digits + punctuation
    key = ''.join(choice(chars) for _ in range(length))
    return key.replace('\'', '') # return safe key

def validate_templates(items, includes):
    """ Validate template listing """

    valid_templates = []
    for f in items:
        for i in includes: # makes my skin crawl
            if i in f and not '.pyc' in f:
                valid_templates.append(f)
    return valid_templates
