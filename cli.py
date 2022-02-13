import os
import time
from simple_term_menu import TerminalMenu
from tqdm import trange

def do_s():
    time.sleep(1)

def main():
    prompts = []
    prefix = "prompt-"
    suffix = ".txt"
 
    for i, f in enumerate(os.listdir("prompts")):
        if f.startswith(prefix) and f.endswith(suffix):
            p = f[len(prefix):][:-len(suffix)]
            prompts.append(f"{p}")
    
    #stories = ["[a] Activity", "[l] Location", "[f] From a File"]
    tm = TerminalMenu(prompts, title="Choose your starting prompt:")
    i = tm.show()
    print(prompts[i])

    for i in trange(100, desc='Processing datas'):
        do_s()

if __name__ == "__main__":
    main()
