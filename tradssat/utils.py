class InpFile(object):
    def __init__(self, file):
        self.file = file
        self.var_info = self._get_var_info()
        self.structure = {}
        self.dict_vars = {}
        self._read()

    def _read(self):
        with open(self.file, encoding='utf8') as f:
            block = []  # To store lines that go in the same section
            for l in f.read():
                if l[0] == '*':  # start of section

                    # Process any previously stored block
                    if len(block):
                        self._read_section(block)

                    # Clear the current block
                    block.clear()

                # Append current line to block
                block.append(l)

            # Read the last block too
            self._read_section(block)

        # Convert to variable-by-variable dictionary
        self._gen_dict_vars()

    def write(self, file):
        pass

    def get_var(self, var):
        return self.dict_vars[var]

    def set_var(self, var, val):
        self.dict_vars[var] = val

    def _read_section(self, block):
        section_name = block[0][1:].strip()
        self.structure[section_name] = {}
        
        subblock = []
        for l in block:
            if l[0] == '@':

                if len(subblock):
                    self._read_subsection(section_name, subblock)
                subblock.clear()
            subblock.append(l)
        self._read_subsection(section_name, subblock)

    def _read_subsection(self, section_name, subblock):
        pass

    def _get_var_info(self):
        raise NotImplementedError


def write_file():
    pass


def write_section():
    pass
