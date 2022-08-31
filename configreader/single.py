from configparser import SafeConfigParser
from configparser import ConfigParser
from .baseconfiguration import BaseConfiguration


__all__ = ["Single"]


#   TODO:
#       Add content does not work; need to standardize input
#       format I.E. (json, dict) or something that makes
#       more sense.
#   TODO:
#       Would also like to implement way to load in int &
#       str versions of config file values, might be too much
#       to try and do byte and hex data but possibly if an
#       easy way can be figured out.


"""
Single module/class parses & loads sections, content of one specific
configuration file given. Takes absolute path of configuration file,
will load into content attribute in dict format. New content is
writable to the same configuration file given.
"""


class Single(BaseConfiguration):

    _ConfigObj = ConfigParser()
    _singlePath = None
    _singleFileName = None
    _singleFullPath = None

    def load_single(self, path):
        """Load single configuration file"""
        self._singleFullPath = path
        self._single_load_content()

    def add_content(self, newContent):
        """Adds new section & content to configObj"""
        for content in newContent:
            sectionName, sectionContent = self.prepare_content(content)
            self._ConfigObj[f"{sectionName.lower()}"] = sectionContent
            self._single_write_file()

    def _single_load_content(self):
        """Load content from config file & return dict."""
        self._single_load_sections()
        parser = SafeConfigParser()
        parser.optionxform = str
        found = parser.read(rf"{self.workingDir}\{self._singleFullPath}")
        if not found:
            raise ValueError('No config file found!')
        for name in self.sections:
            self.content[f"{name}"] = dict(parser.items(name))

    def _single_load_sections(self):
        """Load all sections of ini file into class sections list."""
        self._single_read_file()
        self.sections = self._ConfigObj.sections()

    def _single_read_file(self):
        """Read file from path and return content."""
        with open(rf"{self.workingDir}\{self._singleFullPath}", "r") as file:
            self._ConfigObj.read_file(file)

    def _single_write_file(self):
        """Writes ConfigObj to class INI file"""
        with open(rf"{self.workingDir}\{self._singleFullPath}", "w") as file:
            self._ConfigObj.write(file)
