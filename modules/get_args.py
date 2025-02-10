import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", nargs='+', help="YouTube URLs")
    args = parser.parse_args()
    return args.url

if __name__ == "__main__":
    urls = get_args()
    print(urls)
