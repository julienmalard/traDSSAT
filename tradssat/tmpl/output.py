from .file import File


class OutFile(File):

    def _get_var_info(self):
        raise NotImplementedError
