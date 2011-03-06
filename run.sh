C_DIR=$(pwd)
JAR_DIR=$(cd $(dirname $0) && pwd)
cd $JAR_DIR
jar cvfm Project.jar METADATA/MANIFEST.mf *.class > /dev/null
cd ..
./gripper jfc --main-class Project --urls $JAR_DIR/Project.jar
cd $C_DIR
