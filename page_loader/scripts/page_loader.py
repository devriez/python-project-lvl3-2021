#! /usr/bin/env python3

import argparse
import os
import sys

import requests

from page_loader.engine import download
from page_loader.logger import get_logger

logger = get_logger(__name__)


def main():
    """Launch a page_loader cli."""
    logger.info('start process')
    parser = argparse.ArgumentParser(description='Download page')
    parser.add_argument('url', type=str)
    parser.add_argument('-o', '--output', help='set path for output', type=str,
                        default=os.getcwd())
    args = parser.parse_args()

    try:
        result_file_path = download(args.url, args.output)
        return result_file_path
    except requests.exceptions.RequestException as error:
        logger.critical(error)
        sys.exit(1)
    except OSError as error:
        logger.critical(error)
        sys.exit(1)
    except KeyboardInterrupt as error:
        logger.critical(error)
        sys.exit(1)


if __name__ == '__main__':
    main()
