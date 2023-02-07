class Logger(object):
    """A file based message logger with the following properties

    Attributes:
        filename: a string represtenting full path of the log file
        to which this logger will write its messages
    """

    class __logger:
        def __init__(self, filename):
            self.val = None
            self.filename = filename

        def write_log(self, level: str, msg: str) -> str:
            """Log writer that outputs errors to a log. Needs the filename adding to line 1"""
            with open(
                f"/home/ashleyspeight/Projects/Python_Design_Patterns/log/{self.filename}.log",
                "a",
            ) as log_file:
                log_file.write("[{0}] {1}\n".format(level, msg))

        def critical(self, msg):
            self.write_log("CRITICAL", msg)

        def error(self, msg):
            self.write_log("ERROR", msg)

        def warn(self, msg):
            self.write_log("WARN", msg)

        def info(self, msg):
            self.write_log("INFO", msg)

        def debug(self, msg):
            self.write_log("DEBUG", msg)

    instance = None

    def __new__(cls, filename):
        if not Logger.instance:
            Logger.instance = Logger.__logger(filename)
        return Logger.instance
