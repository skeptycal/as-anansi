import enum


class Err(enum.Enum):
    """ C++ style error messages """
    # setup C++ style error messages
    # reference: Advanced Bash-Scripting Guide
    #   <http://tldp.org/LDP/abs/html/exitcodes.html#EXITCODESREF>

    # from /usr/include/sysexits.h
    # Copyright (c) 1987, 1993
    # The Regents of the University of California.  All rights reserved.
    ERR_OK_ = 0                  # successful termination

    # - The Linux Documentation Project has a list of reserved codes that
    #   also offers advice on what code to use for specific scenarios. These
    #   are the standard error codes in Linux or UNIX.

    ERR_ERROR_ = 1               # catchall for general errors
    ERR_SHELLERR_ = 2            # misuse of shell builtins (BASH)

    ERR__BASE_ = 64              # base value for error messages
    ERR_USAGE_ = 64              # command line usage error
    ERR_DATAERR_ = 65            # data format error
    ERR_NOINPUT_ = 66            # cannot open input
    ERR_NOUSER_ = 67             # addressee unknown
    ERR_NOHOST_ = 68             # host name unknown
    ERR_UNAVAILABL_ = 69         # service unavailable
    ERR_SOFTWARE_ = 70           # internal software error
    ERR_OSERR_ = 71              # system error (e.g., can't fork)
    ERR_OSFILE_ = 72             # critical OS file missing
    ERR_CANTCREAT_ = 73          # can't create (user) output file
    ERR_IOERR_ = 74              # input/output error
    ERR_TEMPFAIL_ = 75           # temp failure; user is invited to retry
    ERR_PROTOCOL_ = 76           # remote error in protocol
    ERR_NOPERM_ = 77             # permission denied
    ERR_CONFIG_ = 78             # configuration error
    ERR__MAX_ = 78               # maximum listed value

    # Linux / Unix codes
    ERR_CANTEXECUTE_ = 126       # command invoked cannot execute
    ERR_NOTFOUND_ = 127          # command not found; possible $PATH error or typo
    ERR_BADARG_ = 128            # invalid argument
    ERR_FATALARG_ = 129          # fatal error
    ERR_CTRL_C_ = 130            # script terminated by Control-C
