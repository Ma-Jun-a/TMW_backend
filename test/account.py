import sys,time,os,subprocess,json, importlib, binascii, hashlib, shutil
import xml.etree.ElementTree as ET
# from flask_script import Manager
# from app.tables.IAT import Project, Tree, Sample, Task, iatShellData, GlobalValues, iatCaseInfo, iatKeyValues
# from app import app,db
from datetime import datetime
def configTestElement(test_domain,params=None,proxy=None):
  domain = test_domain
  protocol = ""
  port = ""
  if domain:
    if "://" in test_domain:
      protocol = test_domain.split("://")[0]
      domain = test_domain.split("://")[1]
      if ":" in domain:
        domain = domain.split(":")[0]
    formatTestDomain = test_domain.replace("://","")
    if ":" in formatTestDomain:
      port = formatTestDomain.split(":")[1]
  ConfigTestElement = ET.Element("ConfigTestElement",{
    "guiclass":"HttpDefaultsGui",
    "testclass":"ConfigTestElement",
    "testname":u"HTTP请求默认值",
    "enabled":"true",
  })
  elementProp = ET.SubElement(ConfigTestElement,"elementProp", {"name": "HTTPsampler.Arguments", "elementType": "Arguments",
                                           "guiclass": "HTTPArgumentsPanel", "testclass": "Arguments",
                                           "testname": u"用户定义的变量", "enabled": "true"})
  collectionProp = ET.SubElement(elementProp,'collectionProp',{"name":"Arguments.arguments"})
  # if projectGlobalValues:
  #   for item in projectGlobalValues:
  #     if item:
  #       paramElementProp = ET.Element('elementProp',{"name":item["key"], "elementType":"HTTPArgument"})
  #       ET.SubElement(paramElementProp,'boolProp',{"name":"HTTPArgument.always_encode"}).text = 'false'
  #       ET.SubElement(paramElementProp,'stringProp',{"name":"Argument.value"}).text = item["value"]
  #       ET.SubElement(paramElementProp,'stringProp',{"name":"Argument.metadata"}).text = '='
  #       ET.SubElement(paramElementProp,'boolProp',{"name":"HTTPArgument.use_equals"}).text = 'true'
  #       ET.SubElement(paramElementProp,'stringProp',{"name":"Argument.name"}).text = item["key"]
  #       collectionProp.append(paramElementProp)

  if params:
    for item in params:
      if item:
        paramElementProp = ET.Element('elementProp',{"name":item["key"], "elementType":"HTTPArgument"})
        ET.SubElement(paramElementProp,'boolProp',{"name":"HTTPArgument.always_encode"}).text = 'false'
        ET.SubElement(paramElementProp,'stringProp',{"name":"Argument.value"}).text = item["value"]
        ET.SubElement(paramElementProp,'stringProp',{"name":"Argument.metadata"}).text = '='
        ET.SubElement(paramElementProp,'boolProp',{"name":"HTTPArgument.use_equals"}).text = 'true'
        ET.SubElement(paramElementProp,'stringProp',{"name":"Argument.name"}).text = item["key"]
        collectionProp.append(paramElementProp)
        print(paramElementProp.items())
        print(paramElementProp.attrib)

  ET.SubElement(ConfigTestElement, 'stringProp', {"name": "HTTPSampler.domain"}).text = domain
  ET.SubElement(ConfigTestElement, 'stringProp', {"name": "HTTPSampler.port"}).text = port
  ET.SubElement(ConfigTestElement, 'stringProp', {"name": "HTTPSampler.protocol"}).text = protocol
  ET.SubElement(ConfigTestElement, 'stringProp', {"name": "HTTPSampler.contentEncoding"})
  ET.SubElement(ConfigTestElement, 'stringProp', {"name": "HTTPSampler.path"})
  ET.SubElement(ConfigTestElement, 'stringProp', {"name": "HTTPSampler.concurrentPool"}).text = "6"
  if proxy:
    try:
      userName = ''
      password = ''
      server = ''
      port = ''
      if "@" in proxy:
        userConfig = proxy.split('@')[0]
        proxyConfig = proxy.split('@')[1]
        userName = userConfig.split(':')[0]
        password = userConfig.split(':')[1]
        server = proxyConfig.split(':')[0]
        port = proxyConfig.split(':')[1]
      elif ":" in proxy:
        server = proxy.split(':')[0]
        port = proxy.split(':')[1]
      ET.SubElement(ConfigTestElement, 'stringProp', {"name": "HTTPSampler.proxyHost"}).text = server
      ET.SubElement(ConfigTestElement, 'stringProp', {"name": "HTTPSampler.proxyPort"}).text = port
      ET.SubElement(ConfigTestElement, 'stringProp', {"name": "HTTPSampler.proxyUser"}).text = userName
      ET.SubElement(ConfigTestElement, 'stringProp', {"name": "HTTPSampler.proxyPass"}).text = password
    except Exception as e:
      print("proxy error",e)
  ET.SubElement(ConfigTestElement, 'stringProp', {"name": "HTTPSampler.connect_timeout"})
  ET.SubElement(ConfigTestElement, 'stringProp', {"name": "HTTPSampler.response_timeout"})
  print(ConfigTestElement.items())
  return ConfigTestElement

configTestElement('https://www.baidu.com/',params=[{"key":"value","value":"11"}])