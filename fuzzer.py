#!/usr/bin/env python3

import requests
import argparse
import threading
from queue import Queue


def get_argument(): 
        parser = argparse.ArgumentParser(description='Subdomain Enumerator')
        parser.add_argument("--url", help="enter a url e.g. https://example.com/test-page")
        parser.add_argument("--wordlist", help="add a wordlist e.g. path to wordlist file")
        parser.add_argument("--threads", help="not required default of 10", type = int, default = 10)
        parser.add_argument("--output", help="not required, save the output to a file default = results.txt", default = "results.txt")
        return parser.parse_args()


def load_wordlist(path):
        with open(path) as file:
                words = [line.strip() for line in file.readlines() if line.strip() != ""]
        return words

def check_path(full_url, output):
        try:
                response = requests.get(full_url)
                if response.status_code == 200:
                        print("Found ",full_url)
                        open(output, "a").write(full_url + "\n")
                elif response.status_code == 301 or response.status_code == 302:
                        print("Found ",full_url," (redirected)")
                        open(output, "a").write(full_url + " (redirected)\n")
                elif response.status_code == 403:
                        print("Found ",full_url, " forbidden")
                        open(output, "a").write(full_url + " (forbidden)\n")                      
        except requests.exceptions.RequestException:
                pass


def worker(url, queue, output): 
        while not queue.empty():
                fuzz = queue.get()
                if url.endswith("/"):
                        path = url + fuzz
                else:
                        path = url + "/" + fuzz
                check_path(path, output)
                queue.task_done()      

def main():
        print("""

                                                                          
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   
                                                                          
     ███████╗ ██████╗ ██████╗ ███████╗██╗  ██╗                          
     ██╔════╝██╔═══██╗██╔══██╗██╔════╝██║ ██╔╝                          
     ███████╗██║   ██║██████╔╝█████╗  █████╔╝                           
     ╚════██║██║   ██║██╔══██╗██╔══╝  ██╔═██╗                           
     ███████║╚██████╔╝██████╔╝███████╗██║  ██╗                          
     ╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝                         
                                                                          
                     __                                                   
        .--.  .-.   //                                                    
       /    \/   \ //                                                     
      |  o  |  o |//                                                      
       \    /\   //                                                       
     ~~~\__/  \_//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                    
        |      /|        Directory & File Fuzzer v1.0                    
        |_____/ |              [ by C0rmat ]                             
       /  / /  /                                                          
      /__/_/__/                                                           
                                                                          
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

          
  """)
        args = get_argument()
        words = load_wordlist(args.wordlist)
        q = Queue()
        for word in words:
                q.put(word)
        threads = []
        for i in range(args.threads):
                t = threading.Thread (target=worker, args=(args.url, q, args.output))
                t.start()       
                threads.append(t)
        
        for i in threads:
                i.join()

if __name__ == "__main__":
        main()
      





