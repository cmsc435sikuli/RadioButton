C_DIR=$(pwd)
JAR_DIR=$(cd $(dirname $0) && pwd)
cd $JAR_DIR
cd ..
./greplayer jfc -g GUITAR-Default.GUI -e efg.efg -t $2 --main-class Project --urls $JAR_DIR/Project.jar --config-file config/configuration.xml -m $1
cd $C_DIR
