#### Exercise 1a:

For run this script, please set couple variables:
```
export OPENWEATHER_API_KEY="xxxxxxxxxxxx"
export CITY_NAME="Honolulu"
```
After this run:
```
python getweather.py
```

#### Exercise 1b:
For the last step, the current user must be in the group "docker" (it was not automated with ansible for security reasons)
```
ansible-playbook -i "localhost," -c local site.yml
docker -v
docker info | grep 'Logging Driver'
```

#### Exercise: 1c:
Run buils.sh to build appropriate container
```
docker run --rm -e OPENWEATHER_API_KEY="xxxxxxxxxxxx" -e CITY_NAME="Honolulu" weather:dev
grep openweathermap /var/log/syslog
```

#### Exercise 2:
The script accepts ip or network number (in CIDR notation) as input parameter
for example: scanner 10.16.111.1
or           scanner 10.16.111.0/24
```
./scanner 10.1.1.1
```

#### Exercise 3:
There are two possible variables:
rsyslog_ip=<ip> to enable remote rsyslog server, it enables transmit log from syslog to remote server
custom_log_path=<path to custom log (wildcard allowed)> it enables transmit custom log to remote server
```
ansible-playbook -i "localhost," -c local rsyslog.yml --extra-vars "rsyslog_ip=<ip> custom_log_path=<path>"
```
