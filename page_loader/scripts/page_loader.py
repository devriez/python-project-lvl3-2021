! /usr/bin/env python3

 import argparse
 import os
 from page_loader.page_loader import download


 def main():
     """Launch a page_loader cli."""
     parser = argparse.ArgumentParser(description='Download page')
     parser.add_argument('file_path', action="store")
     parser.add_argument('--output', dest="output_dir",
                         action="store", help='set directory to save page')
     args = parser.parse_args()
     if not args.output_dir:
         args.output_dir = os.getcwd()
     return download(args.file_path, args.output_dir)


 if __name__ == '__main__':
     main()
