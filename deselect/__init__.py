from fman import DirectoryPaneCommand
import os.path

class Deselect(DirectoryPaneCommand):
    def __call__(self):
        selected_files = self.pane.get_selected_files()
        if len(selected_files) >= 1 or (len(selected_files) == 0 and self.get_chosen_files()):
            if len(selected_files) == 0 and self.get_chosen_files():
                selected_files.append(self.get_chosen_files()[0])
            #
            # Loop through each file/directory selected.
            #
            for filedir in selected_files:
                self.pane.toggle_selection(filedir)
