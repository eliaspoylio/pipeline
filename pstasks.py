import time
import subprocess
import json
import sys

class Tasklist:
    config_path = './config.json'
    config = []

    @classmethod
    def run(self, cmd):
        #completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
        completed = subprocess.run([cmd], shell=True)
        return completed

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
    
    tasklist=Tasklist.getConfig()

    for item in tasklist:
        task = Tasklist.run(item)
        if task.returncode != 0:
            print("An error occured: %s", task.stderr)
        else:
            #print(task.stdout.decode("utf-8"))
            print(task.stdout)
            continue


    print("------------------------------------------------")
    end = time.time()
    print("Finished tasks after:",end - start,"seconds")

    import platform 
    plt = platform.system()
    if plt == "Windows":
        print("Your system is " + plt)
    elif plt == "Linux":
        print("Your system is " + plt)
    elif plt == "Darwin":
        print("Your system is " + plt)
    else:
        print("Unidentified system" + plt)

if __name__ == '__main__':
     main()