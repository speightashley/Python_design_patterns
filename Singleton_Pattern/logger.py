filename = "ashlog"


def write_log(level: str, msg: str) -> str:
    """Log writer that outputs errors to a log. Needs the filename adding to line 1"""
    with open(f"/var/log/{filename}.log", "a") as log_file:
        log_file.write("[{0}] {1}\n".format(level, msg))


def critical(msg):
    write_log("CRITICAL", msg)


def error(msg):
    write_log("ERROR", msg)


def warn(msg):
    write_log("WARN", msg)


def info(msg):
    write_log("INFO", msg)


def debug(msg):
    write_log("DEBUG", msg)
