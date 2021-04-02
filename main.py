import sys
import os

def main():
    print("here")
    content_download()
    


def content_download():
    while True:
        try:
            arch = sys.argv[2]
        except:
            print("Looks like you did not enter an architecture. Please try again.")
            arch = input("Please enter desired architecture: ")
            continue
        else:
            print("Input recieved")
            print(arch)
            break
        finally:
            print("executed")