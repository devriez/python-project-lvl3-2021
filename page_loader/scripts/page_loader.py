#! /usr/bin/env python3

import argparse
import os
from page_loader.page_loader import download
from page_loader.app_logger import get_logger

logger = get_logger(__name__)


def main():
    """Launch a page_loader cli."""
    logger.info('start process')
    parser = argparse.ArgumentParser(description='Download page')
    parser.add_argument('file_path', action="store")
    parser.add_argument('--output', dest="output_dir",
                        action="store", help='set directory to save page')
    args = parser.parse_args()
    if not args.output_dir:
        logger.info('output dirrectory do not specified')
        args.output_dir = os.getcwd()
    return download(args.file_path, args.output_dir)


if __name__ == '__main__':
    main()
