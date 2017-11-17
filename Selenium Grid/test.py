# java -jar selenium-server-standalone-3.6.0.jar -role hub
# java -jar selenium-server-standalone-3.6.0.jar -role node -port 5555
# java -jar selenium-server-standalone-3.6.0.jar -role node -port 6666

from selenium.webdriver import Remote
import os,time
import subprocess


lists = {
    'http://127.0.0.1:4444/wd/hub': 'chrome',
    'http://127.0.0.1:6666/wd/hub': 'firefox',
}

comm= {"hub_user":"java -jar C:\Users\dell\Desktop\selenium-server-standalone-3.6.0.jar -role hub",
        "node_a":"java -jar C:\Users\dell\Desktop\selenium-server-standalone-3.6.0.jar -role node -port 5555",
		"node_b":"java -jar C:\Users\dell\Desktop\selenium-server-standalone-3.6.0.jar -role node -port 6666"

}
s="up and running"

def startup():
    for item in comm.values():
	    subprocess.Popen(item)

	
    



def test():
    for host, browser in lists.items():
        print(host, browser)

        driver = Remote(command_executor=host,
            desired_capabilities={'platform': 'ANY',
                                  'browserName': browser,
                                  'version': '',
                                  'javascriptEnabled': True}
            )

        driver.get('https://www.baidu.com')
        driver.find_element_by_id("kw").send_keys("remote")
        driver.find_element_by_id("su").click()

    
	

def main():
    startup()
    test()


if __name__=="__main__":
    main()
