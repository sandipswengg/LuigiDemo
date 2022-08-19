# LuigiDemo
Demonstration of Luigi process


**Run the application:**
1) Setup the PIP Virtual Environment
2) Go to ./LuigiTasks/LuigiDemo
3) Make sure the folder ./LuigiTasks/LuigiDemo/OUTDIR is EMPTY
4) Run the command 
   [> luigi --module TaskA WriteLocalFileTask --local-scheduler]
5) Run the Luigi using remote
   > sudo ufw allow 8082/tcp
   > sudo sh -c ". venv/bin/activate ;luigid --background --port 8082"
   > luigid --port 8082 > /dev/null 2> /dev/null &
   > cd LuigiDemo/app [OR] PYTHONPATH='./LuigiDemo/app'
   [Run the application ==> luigi --module TaskA WriteLocalFileTask]
   > 
> 