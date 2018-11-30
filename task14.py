# evil 是 Bert, evil4.jpg 只有通过IE浏览器才能够看到
import xmlrpc.client
xmlrpc_instance = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(xmlrpc_instance.system.listMethods())
print(xmlrpc_instance.system.methodHelp('phone'))
print(xmlrpc_instance.phone('Bert'))