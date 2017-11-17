cd /d C:\Users\dell\Desktop\
start java -jar selenium-server-standalone-3.6.0.jar -role hub
start java -jar selenium-server-standalone-3.6.0.jar -role node -port 5555 -hub http://localhost:4444/grid/register
start java -jar selenium-server-standalone-3.6.0.jar -role node -port 6666 -hub http://localhost:4444/grid/register
