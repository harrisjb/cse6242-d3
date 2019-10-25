To install on EC2 follow the below guidelines:
1. Create a free micro instance
    I'm using Ubuntu Server 16.04 LTS (HVM), SSD Volume Type
    expose port 9000 for gunicorn (Only needed for test)
    22 (SSH), 80 (HTTP), 443 (HTTPS), and 3389 (RDP, optional).

    add an elastic ip (in case we need to dump this instance but don't want to change IP's)

2. Start the instance and login with ssh
   * `ssh -i "PRIVATE-key.pem" ubuntu@xxx.xxx.xxx.xxx` (Provide your own permissions file and IP)
   * `sudo apt-get update`
   * `sudo apt-get -y upgrade`
   * `sudo apt-get -y install python3-pip python3-dev`
   * `sudo apt-get -y install python3-venv`
   * `pip3 install --upgrade pip setuptools`

3. Create a virtual environment for our project
   * `mkdir ~/Applications`
   * `python3 -m venv Applications/python_envs`
   * `source ~/Applications/python_envs/bin/activate`
   * `pip install --upgrade pip`
   * `pip install wheel`
   * `pip install flask`
   * `pip install flask-wtf`
   * `pip install gunicorn`
   * `pip install gevent`

4. clone project to the EC2 Instance
   * `cd ~/Applications`
   * `git clone https://github.com/dphiggs01/opioid_epidemic_analysis.git`
   * `source ~/Applications/python_envs/bin/activate`
   * `cd opioid_epidemic_analysis;nohup ./run.sh &`
   * Note: If the server is running you must stop the currently running server
   * `cd ~/Applications/opioid_epidemic_analysis;kill -9 ``cat gunicorn.pid`` ` ;

5. Check the running web app
   * visit http://xxx.xxx.xxx.xxx


   for d in `ps -auxww|grep python|cut -d' ' -f6`;do echo $d; done
  

