import os

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from flask import Flask, redirect, url_for
from flask import render_template
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def load_rules(rules_dir):
    rules = {}
    for file in os.listdir(rules_dir):
        if file.endswith('yaml') or file.endswith('yml'):
            with open(os.path.join(rules_dir, file), 'r') as fh:
                rules[file.split('.')[0].capitalize()] = load(fh, Loader)
    return rules

def create_app(rules_dir):
    app = Flask(__name__)
    app.config['RULES'] = load_rules(rules_dir)
    bootstrap.init_app(app)

    @app.route('/rules/<ruleset>', methods=['GET'])
    def show_ruleset(ruleset):
        rules = app.config['RULES'][ruleset]

        return render_template(
            'ruleset.html', rulesets=sorted(app.config['RULES'].keys()),
            ruleset=ruleset, rules=rules
        )

    @app.route('/', methods=['GET'])
    def home():
        first_ruleset = sorted(app.config['RULES'].keys())[0]
        return redirect(url_for('show_ruleset', ruleset=first_ruleset))

    return app