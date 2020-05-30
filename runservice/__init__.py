from core.quicksearch_matchers import contains_chars
from fman import DirectoryPaneCommand, show_quicksearch, QuicksearchItem, show_status_message, clear_status_message, show_alert
from subprocess import run, PIPE
from os import path
import json

class RunService(DirectoryPaneCommand):

    def __call__(self):
        show_status_message('Getting Services...')
        result = show_quicksearch(self._suggest_script)
        if result:
            #
            # Launch the script given. Show the output.
            #
            query, script = result

            #
            # Run the script.
            #
            Output = run('', stdout=PIPE, shell=True)
            if Output.returncode == 0:
                show_alert(Output.stdout.decode("utf-8"))
            else:
                show_alert("Command line error.")
        clear_status_message()

    def _suggest_script(self, query):
        show_alert('/usr/bin/osascript "' + path.dirname(path.realpath(__file__)) + '/serviceMenu.scpt"')
        output = run('/usr/bin/osascript "' + path.dirname(path.realpath(__file__)) + '/serviceMenu.scpt"', stdout=PIPE, shell=True)
        show_alert(output.stdout.decode("utf-8"))
        services = json.loads(output.stdout.decode("utf-8"))

        #
        # Suggested one to the user and let them pick.
        #
        for service in services:
            if service.name.strip() != "":
                serviceName = service.name
                match = contains_chars(serviceName.lower(), query.lower())
                if match or not query:
                    yield QuicksearchItem(serviceName, highlight=match)
