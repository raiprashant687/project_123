from Utils_Package.config import Config
from Utils_Package.utils import Utils
from Utils_Package.git_utils import GITUtils

import os
import sys
import datetime

iteration_count = 1


class Execution:

    def __init__(self):
        self.config = Config()
        # self.utils = Utils(self.config)
        # self.gitUtils = GITUtils(self.config)
        # singleton = Singleton()

    def executeParameters(self):
        # print("execute parameters")
        # ==============================================================================================
        if self.isArgumentsTobePassed:
            # print("Checking for parameters ")
            if len(sys.argv) > 1:
                # print("there are arguments being passed")
                if (sys.argv[1] in ("LAB1", "INT", "UAT")):
                    # print("expected arguments::: ")
                    self.config.setEnv(sys.argv[1])
                    print("Testing initiated for ENV: " + str(self.config.getENV()))
                else:
                    print(
                        "not an expected argument for Environment. Please enter the environment you want to execute (LAB1 / INT / UAT)")
                    exit()
            else:
                print(
                    "Arguments are not being passed. Please enter the environment you want to execute (LAB1 / INT / UAT)")
                exit()
        else:
            print("Dont wait for arguments to be passed")
            self.config.setEnv("LAB1")
        self.utils = Utils(self.config)
        self.gitUtils = GITUtils(self.config)

    def executeGITLABSync(self):
        # print("executeGITLABSync")
        # ============================================================================================== #
        try:
            if self.isGITLABSync:

                # gitUtils.checkForLatest()
                remote_branch_name = self.config.getRemoteBranch()
                self.gitUtils.UpdateGITBranchWithLatestChanges(remote_branch_name)
                print("Finished GitLAB sync")
            else:
                print("GITLAB sync is disabled")
        except:
            print("Not able to sync with GITLAB, proceeding with the existing scripts")

    def environmentSetup(self):
        print("proceed with EnvironmentSetup")
        self.executeParameters()
        self.executeGITLABSync()

        if not (self.config.getPlatform() == "windows"):
            # set no_proxy as well
            print("setting proxy config")
            os.environ["no_proxy"] = "be,ocp.tc.corp"

    def executeScripts(self):
        currentDT = datetime.datetime.now()
        print("\n ##################### Executing Scripts on: " + str(currentDT) + "#####################")
        path = self.config.getSanityTestSuite()
        # print(path)
        # ============================================================================================== #
        if self.isScriptExecution:

            # Separate JMX and Postman collections and saved in separate list
            self.utils.prepareJMXAndPostmanCollections(path)

            if self.isPostmanScriptEanbled:
                print("\n ##################### Testing of Postman Collections ##################### \n")
                self.utils.prepareAndExecutePostmanCollections()
            else:
                print("Postman SCripts are disabled")

            if self.isJMXScriptEnabled:
                print("\n ##################### Testing of JMX Scripts ##################### \n")
                self.utils.prepareAndExecuteJMXScripts()
            else:
                print("JMeter Scripts are disabled")
        else:
            print("Script execution is disabled")

    def execute(self):

        self.isScriptExecution = True
        self.isGITLABSync = True
        self.isJMXScriptEnabled = True
        self.isPostmanScriptEanbled = True
        self.isArgumentsTobePassed = True

        self.environmentSetup()
        self.executeScripts()


# ============================================================================================== #

execution = Execution()

for i in range(0, iteration_count):
    print("\nIteration count is: " + str(i))
    execution.execute()

