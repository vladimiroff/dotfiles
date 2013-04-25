#!/usr/bin/env python2
# coding: utf-8
"""
Program that convert text files from one encoding to another.
By default it is used to convert windows-1251 encoded subtitles
into ISO-8859-5 ecoded because this is encoding for cyrilic
characters in Panasonic Viera TV

created by Venelin Stoykov <vkstoykov@gmail.com>
"""
import sys
import os
from optparse import make_option, OptionParser

__version__ = (0, 2)

DEFAULT_INPUT_ENCODING = 'windows-1251'
DEFAULT_OUTPUT_ENCODING = 'iso-8859-5'

FAILSAFE_CHARACTERS = {
    u'\u2122': 'TM',
    u'\u201c': '"',
    u'\u201d': '"',
}


def get_version():
    return '.'.join(unicode(x) for x in __version__)


def get_failsafe_char(char, output_encoding):
    return FAILSAFE_CHARACTERS.get(char, '?').encode(output_encoding)


def convert_to(in_file_name,
               input_encoding=DEFAULT_INPUT_ENCODING,
               output_encoding=DEFAULT_OUTPUT_ENCODING):
    out_file_name = "%s.%s%s" % (in_file_name[:-4],
                                 output_encoding, in_file_name[-4:])

    with open(in_file_name, 'r') as in_file:
        try:
            content = in_file.read().decode(input_encoding)
        except Exception as ex:
            print "Can't read '%s' because: %s" % (in_file_name, ex)
        else:
            new_content = []
            for char in content:
                try:
                    new_content.append(char.encode(output_encoding))
                except Exception as ex:
                    new_content.append(get_failsafe_char(char, output_encoding))

            with open(out_file_name, 'w') as out_file:
                for char in new_content:
                    out_file.write(char)


def main(*args, **options):
    for in_file in args:
        convert_to(in_file, **options)


if __name__ == '__main__':
    prog_name = os.path.basename(sys.argv[0])
    opt_parser = OptionParser(
        prog=prog_name,
        version=get_version(),
        option_list=(
            make_option('-i', '--input-encoding', dest='input_encoding',
                        default=DEFAULT_INPUT_ENCODING,
                        help="Encoding on the input file"),
            make_option('-o', '--output-encoding', dest='output_encoding',
                        default=DEFAULT_OUTPUT_ENCODING,
                        help="Encoding on the output file"),
        )
    )
    options, args = opt_parser.parse_args(sys.argv[1:])
    main(*args, **options.__dict__)
