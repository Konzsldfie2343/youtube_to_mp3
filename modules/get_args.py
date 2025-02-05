import argparse

def get_args():
          parser = argparse.ArgumentParser()
          parser.add_argument("url", help="YouTube URL")
          args = parser.parse_args()
          return args.url