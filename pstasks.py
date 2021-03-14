import time
import json
import sys
import platform 

class Tasklist:
    config_path = './config.json'
    config = []

    @classmethod
    def getConfig(self):
        if(self.config == []):
            try:
                configString = open(self.config_path).read()
            except:
                sys.exit('Could not load ' + self.config_path + ' file')

            try:
                self.config = json.loads(configString)
            except:
                sys.exit(self.config_path + ' file is not valid json')

            # TO DO: Check task validity

        return self.config

def main():

    start = time.time()
    print("------------------------------------------------")
    plt = platform.system()
    if plt == "Windows":
        print("Running on " + plt)
        import modules.windows as nativetools
    elif plt == "Linux":
        print("Running on " + plt)
        import modules.linux as nativetools
    elif plt == "Darwin":
        print("Running on " + plt)
        import modules.windows as nativetools
    else:
        print("Unidentified system" + plt)
    print("------------------------------------------------")
    
    tasklist=Tasklist.getConfig()

    for item in tasklist:
        task = nativetools.run(item)
        if task.returncode != 0:
            print("An error occured: %s", task.stderr)
        else:
            nativetools.output(task)
            continue


    print("------------------------------------------------")
    end = time.time()
    print("Finished tasks after:",end - start,"seconds")

if __name__ == '__main__':
     main()