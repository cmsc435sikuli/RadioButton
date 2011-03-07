import os, string, sys, subprocess

C_DIR = os.getcwd()
JAR_DIR = sys.path[0]

if os.getenv("JDK_HOME"):
    JDK_HOME = os.getenv("JDK_HOME")
elif os.getenv("JAVA_HOME"):
    JDK_HOME = os.getenv("JAVA_HOME")
else:
    for i in os.listdir("c:\\program files\\java"):
        if string.find(i, 'jdk') == 0:
            JDK_HOME = "c:\\program files\\java\\" + i

print JDK_HOME

if not JDK_HOME:
    raise Exception("JDK not found")


os.chdir(JAR_DIR)

subprocess.call(JDK_HOME + "\\bin\\jar.exe" + " cvfm Project.jar METADATA/MANIFEST.mf *.class")
os.chdir("..")
subprocess.call("python gripper" + " jfc --main-class Project --urls " + JAR_DIR + "\\Project.jar")

os.chdir(C_DIR)
