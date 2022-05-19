from parser.parser import generate_parser

if __name__ == '__main__':
    # generate parser.
    parser = generate_parser()

    # take the arguments from the cli.
    args = parser.parse_args()

    # check if the file operations flag is set
    # if it is set, then take input and output path.
    # if not then do the algorithms based on the mode from the cli.
    if(args.file_ops):
        print("File Ops Mode")
    else:
        print("Default Mode")


