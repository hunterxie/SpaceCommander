import os
import os.path
import sys
class ModifyCustomFormatter(object):
    def file_extension(self, path):
        return os.path.splitext(path)[1]

    def checkNSError(self, filePath):
        file = open(filePath)
        lines = file.readlines()
        curLine = 0
        for line in lines:
            curLine = curLine + 1
            if "if(error)" in line or "if (error)" in line:
                #forward 20 lines search NSError* error or NSError *error
                beginIndex = 0
                if curLine - 20 >= 0:
                    beginIndex = curLine - 20
                for i in range(curLine, beginIndex, -1):
                    forwardLineStr = lines[i].strip()
                    if forwardLineStr.find("NSError") == 0:
                        print(filePath)
                        print('curLine:', curLine)
                        print(line)
                        print('checkNSError:', i, lines[i])
                        break
        file.close()

    # == nil || ==nil || == NO  || ==NO || == YES || ==YES || == true || == TRUE || == false
    def checkBooleans(self, filePath):
        file = open(filePath)
        curLine = 0
        for line in file:
            curLine = curLine + 1
            if "== nil" in line or "==nil" in line or "== NO" in line or "==NO" in line or "== YES" in line or "==YES" in line or "== true" in line or "== TRUE" in line or "== false" in line :
                print(filePath)
                print('curLine:', curLine)
                print('checkBooleans:',line)
        file.close()

    # strong NString || strong NSArray || strong NSDictionary
    def checkPropertyStrong(self, filePath):
        file = open(filePath)
        curLine = 0
        for line in file:
            curLine = curLine + 1
            if "strong) NString" in line or "strong)NString" in line or "strong) NSArray" in line or "strong)NSArray" in line or "strong) NSDictionary" in line or "strong)NSDictionary" in line:
                print(filePath)
                print('curLine:', curLine)
                print('checkPropertyStrong:', line)
        file.close()

    # (nonatomic) || , nonatomic) ||  ,nonatomic) || , nonatomic ) except xib
    def checkPropertyOrder(self, filePath):
        file = open(filePath)
        curLine = 0
        for line in file:
            curLine = curLine + 1
            if "(nonatomic)" in line or ", nonatomic)" in line or ",nonatomic)" in line or ", nonatomic )" in line:
                if "nonatomic) IBOutlet" in line:
                    continue
                print(filePath)
                print('curLine:', curLine)
                print('checkPropertyOrder:', line)
        file.close()

    # NSString* text || NSString * text (later)
    # NSArray arrayWithObjects || NSDictionary dictionaryWithObjectsAndKeys || NSNumber numberWith
    def checkVariables(self,filePath):
        file = open(filePath)
        curLine = 0
        for line in file:
            curLine = curLine + 1
            if "NSArray arrayWithObjects" in line or "NSDictionary dictionaryWithObjectsAndKeys" in line or "NSNumber numberWith" in line:
                print(filePath)
                print('curLine:', curLine)
                print('checkVariables:', line)
        file.close()

    # if (a) abcd;
    def checkIf(self, filePath):
        file = open(filePath)
        curLine = 0
        for line in file:
            curLine = curLine + 1
            if "if (" in line or "if(" in line:
                if not "{\n" in line:
                    print(filePath)
                    print('curLine:', curLine)
                    print('checkIf:', line)
        file.close()

    # must be #pragma mark -
    def checkPragma(self, filePath):
        file = open(filePath)
        curLine = 0
        for line in file:
            curLine = curLine + 1
            if "#pragma mark" in line:
                if not "#pragma mark - " in line:
                    print(filePath)
                    print('curLine:', curLine)
                    print('checkPragma:', line)
        file.close()

    # controller.m view.m cell.m VC.m must have #pragma mark - Lifecycle


    #check public comment
    def checkPublicMethodComment(self, filePath):
        file = open(filePath)
        lines = file.readlines()
        curLine = 0
        for line in lines:
            curLine = curLine + 1
            if "-(" in line or "+(" in line or "- (" in line or "+ (" in line :
                forwardLineStr = lines[curLine-1]
                if not "/" in forwardLineStr:
                    print(filePath)
                    print('curLine:', curLine)
                    print('checkPublicMethodComment:', line)
        file.close()

    #check define comment --Macro
    def checkMacroComment(self,filePath):
        file = open(filePath)
        lines = file.readlines()
        curLine = 0
        for line in lines:
            curLine = curLine + 1
            if "#define" in line:
                if "//" in line:
                    continue
                forwardLineStr = lines[curLine-1]
                if "#define" in forwardLineStr or not "//" in forwardLineStr:
                    print(filePath)
                    print('curLine:', curLine)
                    print('checkMacroComment:', line)
        file.close()

    #check lines between methods
    def checkMethodsLines(self,filePath):
        file = open(filePath)
        lines = file.readlines()
        curLine = 0
        for line in lines:
            curLine = curLine + 1
            if line.find("+ (") == 0 or line.find("- (") == 0:
            #if "+ (" in line or "- (" in line:
                beginIndex = 0
                if curLine - 10 >= 0:
                    beginIndex = curLine - 10
                spaceCount = 0
                for i in range(curLine, beginIndex, -1):
                    forwardLineStr = lines[i].strip()
                    if forwardLineStr.find("\n") == 0 or len(forwardLineStr) == 0:
                        spaceCount = spaceCount + 1
                    if forwardLineStr.find("}") == 0:
                        if spaceCount != 1:
                            print(filePath)
                            print('spaceCount:', spaceCount)
                            print('curLine:', curLine)
                            print('checkMethodsLines:', line)
                        break
        file.close()

    #checkMoreLines
    def checkMoreLines(self,filePath):
        file = open(filePath)
        lines = file.readlines()
        curLine = 0
        for line in lines:
            #print(line)
            curLine = curLine + 1
            line = line.strip()
            if line.find("\n") == 0 or len(line) == 0:
                if (curLine + 1) >=  len(lines):
                    return
                forwardLineStr = lines[curLine].strip()
                if forwardLineStr.find("\n") == 0 or len(forwardLineStr) == 0:
                    print(filePath)
                    print('forwardLineStr:', forwardLineStr)
                    print('curLine:', curLine)
                    print('checkMoreLines:', line)

        file.close()

    def getListdir(self, file_path):
        #for file in self.getListdir(path):
        #file_path = os.path.join(path, file)
        if not os.path.isdir(file_path):
            if self.file_extension(file_path) == ".m":
            #                print(file_path)
                self.checkNSError(file_path)
                self.checkBooleans(file_path)
                self.checkPropertyStrong(file_path)
                self.checkPropertyOrder(file_path)
                self.checkVariables(file_path)
                self.checkIf(file_path)
                self.checkPragma(file_path)
                self.checkMacroComment(file_path)
                self.checkMethodsLines(file_path)
            elif self.file_extension(file_path) == ".h":
#                print(file_path)
                self.checkMacroComment(file_path)
                self.checkPublicMethodComment(file_path)
    def run(self):
        if len(sys.argv) == 2:
            current_dir = os.path.dirname(__file__)
            current_dir = os.path.dirname(current_dir)
            current_dir = os.path.dirname(current_dir)
            src_dir = os.path.join(current_dir, sys.argv[1])
            #            print('src_dir:',src_dir)
            self.getListdir(src_dir)

if __name__ == "__main__":
    ModifyCustomFormatter().run()
