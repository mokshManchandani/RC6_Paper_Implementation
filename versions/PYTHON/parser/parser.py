from argparse import ArgumentParser

def generate_parser():
    """
    This functions creates the parser with the following arguments
    -i, --input_file : input path
    -o, --output_file : output path
    -m, --mode : encryption / decryption
    -k , --key : key string in bytes
    -s, --text_string: block of bytes

    Returns
    Parser object
    """
    parser = ArgumentParser()
    # file operations flag, if set then input and output file will be generated.
    parser.add_argument("--file_ops","-fo",action="store_true",help="File operations flag")

    # file parsing arguments
    parser.add_argument('-i','--input_file',required=False,type=str,metavar='',help="Path to input file")
    parser.add_argument('-o','--output_file',required=False,type=str,metavar='',help="Path to output file")


    # cli input output mode parsing. no files are created in this version of events.
    parser.add_argument('-m','--mode',required=False,type=str,metavar='',help="Mode of operation")
    parser.add_argument('-k','--key',required=False,type=str,metavar='',help="Key string")
    parser.add_argument('-s','--text_string',required=False,type=str,metavar='',help="string to encrypt or decrypt")
    return parser

