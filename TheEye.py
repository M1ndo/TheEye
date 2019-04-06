#!/usr/bin/python2
# Created ybenel

import optparse
import socket,datetime
from time import sleep
from os import system as sy
try:
   import json
except:
        print("[!] Error [ Json ] Is Not Exist !!!\n[*] Please Install It Using This Command: pip2 install simplejson")
        exit(1)
try:
   import urllib2
except KeyboardInterrupt:
    pass
except:
        print("[!] Error [ Urllib2 ] Is Not Exist !!!\n[*] Please reinstall your python, because it comes with python")
        exit(1)

####################
wi='\033[1;37m'
rd='\033[1;31m'
gr='\033[1;32m'
yl='\033[1;33m'
pu='\033[1;35m'
cy='\033[1;36m'
Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
yellow="\033[1;36m"
Red="\033[1;31m"
purple="\033[35m"
Light="\033[95m"
cyan="\033[96m"
stong="\033[39m"
unknown="\033[38;5;82m"
unknown2="\033[38;5;198m"
unknown3="\033[38;5;208m"
unknown4="\033[38;5;167m"
unknown5="\033[38;5;91m"
unknown6="\033[38;5;210m"
unknown7="\033[38;5;165m"
unknown8="\033[38;5;49m"
unknown9="\033[38;5;160m"
unknown10="\033[38;5;51m"
unknown11="\033[38;5;13m"
unknown12="\033[38;5;162m"
unknown13="\033[38;5;203m"
unknown14="\033[38;5;113m"
unknown15="\033[38;5;14m"
####################



#############time####################
                                    #
mytime = datetime.datetime.now()    #
hour = mytime.hour                  #
min = mytime.minute                 #
sec = mytime.second                 #######
timenow = "{}:{}:{}".format(hour,min,sec) #
###########################################


### CHECK INTERNET ######################################
                                                        #
server = "www.google.com"                               #
                                                        #
def check():                                            #
  try:                                                  #
     host = socket.gethostbyname(server)                #
     conn = socket.create_connection((host, 80), 2)     #
     return True                                        #
  except:                                               #
     pass                                               #
  return False                                          #
checknet1 = check()                                     #
checknet2 = checknet1                                   #
checknet3 = checknet2                                   #
                                                        #
################ DONE!###################################

def msgerror():
        print(rd + "\n[!]:Ops:"+yl+"You Not Connected To ["+rd+" INTERNET"+yl+" ]"+Blue+"\n[*]"+gr+":"+wi+"Please Connect To [ "+rd+"INTERNET"+wi+" ] And Try Again "+rd+":)")
        exit()

##########################################=>>OPTIONS<<=###########################################
print("        "+Green+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Blue+"MMMMMMMMMMNKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Grey+"MMMMMMMMMNc.dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Reset+"MMMMMMMMWd. .kWMMMMMMMMMMMMMMMMMMMMMMW0KMMMMMMMMMM")
print("        "+yellow+"MMMMMMMMk:;. 'OMMMMMMMMMMMMMMMMMMMMMWx.,0MMMMMMMMM")
print("        "+Red+"MMMMMMMK:ok.  ,0MMMMMMMMMMMMMMMMMMMWO. .cXMMMMMMMM")
print("        "+purple+"MMMMMMNl:KO.   ;KWNXK00O0000KXNWMMWO' .c;dWMMMMMMM")
print("        "+Light+"MMMMMMx,xNk.    .;'...    ....';:l:.  ,0l,0MMMMMMM")
print("        "+cyan+"MMMMMK;,l;. .,:cc:;.                  .dx,lWMMMMMM")
print("        "+stong+"MMMMWo    ,dKWMMMMWXk:.      .cdkOOxo,. ...OMMMMMM")
print("        "+unknown+"MMMM0'   cXMMWKxood0WWk.   .lkONMMNOOXO,   lWMMMMM")
print("        "+unknown2+"MMMWl   ;XMMNo.    .lXWd. .dWk;;dd;;kWM0'  '0MMMMM")
print("        "+unknown3+"kxko.   lWMMO.      .kMO. .OMMK;  .kMMMNc   oWMMMM")
print("        "+unknown4+"X0k:.   ;KMMXc      :XWo  .dW0c,lo;;xNMK,   'xkkk0")
print("        "+unknown5+"kko'     :KMMNkl::lkNNd.   .dkdKWMNOkXO,    .lOKNW")
print("        "+unknown6+"0Kk:.     .lOXWMMWN0d,       'lxO0Oko;.     .ckkOO")
print("        "+unknown7+"kkkdodo;.    .,;;;'.  .:ooc.     .        ...ck0XN")
print("        "+unknown8+"0XWMMMMWKxc'.          ;dxc.          .,cxKK0OkkOO")
print("        "+unknown9+"MMMMMMMMMMMN0d:'.  .'        .l'  .;lxKWMMMMMMMMMN")
print("        "+unknown10+"MMMMMMMMMMMMMMMN0xo0O:,;;;;;;xN0xOXWMMMMMMMMMMMMMM")
print("        "+unknown11+"MMMMMMMMMMMMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown12+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown13+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown14+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+unknown15+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("        "+Blue+"                   "+unknown+"["+unknown15+"TheEye"+unknown+"]"+unknown+"         ")
print("     "+purple+"             "+unknown+"["+unknown9+"Created By ybenel"+unknown+"]"+unknown+"    "+Reset+"\n")
parse = optparse.OptionParser(unknown10+"""\

[$]                                                                   [$]
 +=====================================================================+
 |> USAGE: python2 ./TheEye.py -S <server_IP OR website> [OPTIONS...] <|
 +=====================================================================+
 |                                                                     |
 |                          >OPTIONS<:                                 |
 +=====================================================================+
 |                                                                     |
 |       -O <PORT>            ::> SCAN [SINGLE] PORT                   |
 |       -M <Many Port>       ::> SCAN [MANY] PORTS                    |
 |       -R <Range Port>      ::> [RANGE] PORTS                        |
 |       -T <Timeout>         ::> Set Timeout For Connection close     |
 |                                                                     |
 |                          >EXAMPLES<:                                |
 +=====================================================================+
 |                                                                     |
 |       TheEye -S www.google.com -O 80                                |
 |       TheEye -S 192.168.1.1 -M 80,443,21,22,23,25,53                |
 |       TheEye -S www.fb.com -R 1-1000                                |
 |                                                                     |
 |       TheEye --server 192.168.1.121 --one-port 80 --timeout 10      |
 |       TheEye -s www.google.com -m 21,22,23,80,443 -t 10             |
 |                      (Hack_The_Planet)                              |
 +=====================================================================+
[$]                                                                   [$]
""",version='TheEye Version: 1.0')
################################### DONE! #######################################################

###################### MAKE MAIN AND FUNCTION #######################################

def main():
  parse.add_option("-S","-s","--server",'--SERVER',dest="TARGET",type="string")
  parse.add_option("-O","-o","--one-port",'--ONE-PORT',dest="Oport",type="string")
  parse.add_option("-M","-m","--many-port",'--MANY-PORT',dest="Mport",type="string")
  parse.add_option("-R","-r","--range-port",'--RANGE-PORT',dest="Rport",type="string")
  parse.add_option("-T","-t","--timeout",'--TIMEOUT',dest="timeout",type="string")
  parse.add_option("-V","-v",'--VERSION',action="store_true",dest="version",default=False)
  (options,args) = parse.parse_args()
  if options.version:
     print("SpyPorte Version: 2.5")
  elif options.TARGET !=None and options.Oport !=None:
        target = options.TARGET
        port = options.Oport
        if int(port) < 0 or int(port) > 65535:
           print(rd+"\n["+yl+"!"+rd+"]"+yl+" Error: Invalid PORT[ "+wi+str(port)+yl+" ]\n"+rd+"["+yl+"!"+rd+"]"+yl+" Must Be Between [ "+wi+"0 "+yl+"&"+wi+" 65535"+yl+" ]")
           exit(1)
        def servername():
          try:
             ser = socket.getservbyport(int(port))
             return ser
          except OSError:
             return "TCP"
          except socket.error:
             return "TCP"
        servername = servername()
        global checknet1
        if target =="127.0.0.1":
                checknet1 = True

        if checknet1 == True:
         def checkser():
           if target !="127.0.0.1":
            try:
               ip = socket.gethostbyname(target)
               return True
            except:
                 pass
            return False
           else:
                return True
         if checkser() !=True:
                print(yl+"\n[!]:"+rd+"Error:["+yl+"404"+rd+"]"+wi+" SERVER Not Found"+rd+"!!")
                exit(1)
         try:
          ip = socket.gethostbyname(target)
          print(unknown2+"\n[*]:method: SINGLE-PORT=> [ {} ]".format(port))
          sleep(1.8)
          print(unknown8+"[>]:ServerIP: {}".format(ip))
          try:
           url = "http://ip-api.com/json/"
           reponse = urllib2.urlopen(url + str(ip) )
           name = reponse.read()
           labs = json.loads(name)
           test = labs['regionName']
           print(rd+"INFO"+gr+":["+wi+str(ip)+gr+"]===:")
           sleep(0.10)
           print(gr + "\t\t IP: " +stong+ labs['query'])
           sleep(0.10)
           print(gr+ "\t\t Status: " +unknown+ labs['status'])
           sleep(0.10)
           print(gr+ "\t\t Region: " +unknown5+ test)
           sleep(0.10)
           print(gr + "\t\t Country: " +unknown3+ labs['country'])
           sleep(0.10)
           print(gr + "\t\t City: " +unknown6+ labs['city'])
           sleep(0.10)
           print(gr + "\t\t ISP: "+unknown2 + labs['isp'])
           sleep(0.10)
           print(gr + "\t\t Lat,Lon: "+unknown4 + str(labs['lat']) + "," + str(labs['lon']))
           sleep(0.10)
           print(gr + "\t\t ZIPCODE: "+unknown12 + labs['zip'])
           sleep(0.10)
           print(gr + "\t\t TimeZone: " +unknown11 + labs['timezone'])
           sleep(0.10)
           print(gr + "\t\t AS: " +unknown15 + labs['as'])
           sleep(0.10)
           print(pu+"===============================\n"+wi)
          except:
                pass
          sleep(0.60)
          print(purple+"[$]:Start At: {}".format(timenow))
          sleep(0.60)
          print(Blue+"[#]:Checking.......")
          sleep(1.5)
          con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          if options.timeout !=None:
                        timeout = options.timeout
                        con.settimeout(int(timeout))
          else:
                        con.settimeout(5)
          con.connect((ip,int(port)))
          print(bl + "\n[+]"+gr+":"+wi+"PORT["+gr+str(port)+wi+"/"+cy+servername+wi+"] <="+gr+"OPEN"+wi+"=>")
         except KeyboardInterrupt:
                        print(rd+"[CTRL+C]:"+yl+"Exiting"+rd+".....")
                        sleep(2.5)
                        exit()
         except socket.error:
               print(rd+"\n[-]"+wi+":PORT["+rd+str(port)+wi+"/"+yl+servername+wi+"] <="+rd+"CLOSE!"+wi+"=>")
         except:
               print(rd+"\n[!]"+yl+"[ERROR] Something Went Wrong..."+gr+"Try Again :)")
               exit(1)
         print(gr+"---------------------------------\n[$]"+unknown7+" Shutdown At: {}".format(timenow))
        else:
                msgerror()

  elif options.TARGET !=None and options.Mport !=None:
        target = options.TARGET
        port = options.Mport
        if "," in port:
          ports = port.split(",")
        else:
                print(rd+"\n[!]"+yl+"[ERROR] Please Use"+gr+" ["+yl+" , "+gr+"]"+yl+" For Distinguish Ports"+gr+" Ex: "+yl+"22,80,23,25,135,445,21")
                exit(1)
        global checknet2
        if target =="127.0.0.1":
                checknet2 = True

        if checknet2 == True:
         def checkser():
           if target !="127.0.0.1":
            try:
               ip = socket.gethostbyname(target)
               return True
            except:
                 pass
            return False
           else:
                return True
         if checkser() !=True:
                print(yl+"\n[!]:"+rd+"Error:["+yl+"404"+rd+"]"+wi+" SERVER Not Found"+rd+"!!")
                exit(1)


         ip = socket.gethostbyname(target)
         print(unknown2+"\n[*]:method: MANY-PORT=> [ {} ]".format(port))
         sleep(1.8)
         print(unknown8+"[>]:ServerIP: {}".format(ip))
         try:
           url = "http://ip-api.com/json/"
           reponse = urllib2.urlopen(url + str(ip) )
           name = reponse.read()
           labs = json.loads(name)
           test = labs['regionName']
           print(rd+"INFO"+gr+":["+wi+str(ip)+gr+"]===:")
           sleep(0.10)
           print(gr + "\t\t IP: " +stong+ labs['query'])
           sleep(0.10)
           print(gr+ "\t\t Status: " +unknown+ labs['status'])
           sleep(0.10)
           print(gr+ "\t\t Region: " +unknown5+ test)
           sleep(0.10)
           print(gr + "\t\t Country: " +unknown3+ labs['country'])
           sleep(0.10)
           print(gr + "\t\t City: " +unknown6+ labs['city'])
           sleep(0.10)
           print(gr + "\t\t ISP: "+unknown2 + labs['isp'])
           sleep(0.10)
           print(gr + "\t\t Lat,Lon: "+unknown4 + str(labs['lat']) + "," + str(labs['lon']))
           sleep(0.10)
           print(gr + "\t\t ZIPCODE: "+unknown12 + labs['zip'])
           sleep(0.10)
           print(gr + "\t\t TimeZone: " +unknown11+ labs['timezone'])
           sleep(0.10)
           print(gr + "\t\t AS: " +unknown15+ labs['as'])
           sleep(0.10)
           print(pu+"===============================\n"+wi)
         except:
                pass
         sleep(0.60)
         print(purple+"[$]:Start At: {}".format(timenow))
         sleep(0.60)
         print(Blue+"[#]:Checking.......")
         sleep(1.5)
         for p in ports:
                        try:
                           servername = socket.getservbyport(int(p))
                        except socket.error:
                           servername = "TCP"
                        except OSError:
                           servername = "TCP"
                        try:
                           con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                           if options.timeout !=None:
                              timeout = options.timeout
                              con.settimeout(int(timeout))
                           else:
                                  con.settimeout(5)
                           con.connect((ip,int(p)))
                           print(bl + "\n[+]"+gr+":"+wi+"PORT["+gr+str(p)+wi+"/"+cy+servername+wi+"]"+wi+" <="+gr+"OPEN"+wi+"=>")
                        except KeyboardInterrupt:
                                print(rd+"[CTRL+C]:"+yl+"Exiting"+rd+".....")
                                sleep(2.5)
                                break
                        except socket.error:
                              print(rd+"\n[-]"+wi+":PORT["+rd+str(p)+wi+"/"+yl+servername+wi+"] <="+rd+"CLOSE!"+wi+"=>")
                        except:
                             print(rd+"\n[!]"+yl+"[ERROR] Something Went Wrong"+rd+" !!!")
         print(gr+"---------------------------------\n[$]"+unknown7+" Shutdown At: {}".format(timenow))

        else:
                msgerror()

  elif options.TARGET !=None and options.Rport !=None:
        target = options.TARGET
        port = options.Rport
        if "-" in port:
          ports = port.split("-")
          if int(ports[0]) > int(ports[1]):
                print(rd+"\n[!] "+yl+"Wrong,The First Range Port"+gr+"["+rd+str(ports[0])+gr+"]"+yl+" Is Bigger Than Last Range Port"+gr+"["+rd+str(ports[1])+gr+"]"+rd+" !!!")
                exit(1)
          elif int(ports[0]) > 65535 or int(ports[1]) > 65535:
             print(rd+"\n["+yl+"!"+rd+"]"+yl+" Error: Invalid Range-PORT[ "+wi+str(ports)+yl+" ]\n"+rd+"["+yl+"!"+rd+"]"+yl+" Must be between [ "+wi+"0 "+yl+"&"+wi+" 65535"+yl+" ]")
             exit(1)
        else:
                print(rd+"\n[!]"+yl+"[ERROR] Please Use"+gr+" ["+yl+" - "+gr+"]"+yl+" For Distinguish First Range to Last Range Ports "+gr+"Ex: "+yl+"1-50")
                exit(1)
        global checknet3
        if target =="127.0.0.1":
                checknet3 = True

        if checknet3 == True:
         def checkser():
           if target !="127.0.0.1":
            try:
               ip = socket.gethostbyname(target)
               return True
            except:
                 pass
            return False
           else:
                return True
         if checkser() !=True:
                print(yl+"\n[!]:"+rd+"Error:["+yl+"404"+rd+"]"+wi+" SERVER Not Found"+rd+"!!")
                exit(1)
         ip = socket.gethostbyname(target)
         print(unknown2+"\n[*]:method: RANGE-PORT=> [ {} ]".format(port))
         sleep(1.8)
         print(unknown8+"[>]:ServerIP: {}".format(ip))
         try:
           url = "http://ip-api.com/json/"
           reponse = urllib2.urlopen(url + str(ip) )
           name = reponse.read()
           labs = json.loads(name)
           test = labs['regionName']
           print(rd+"INFO"+gr+":["+wi+str(ip)+gr+"]===:")
           sleep(0.10)
           print(gr + "\t\t IP: " +stong+ labs['query'])
           sleep(0.10)
           print(gr+ "\t\t Status: " +unknown+ labs['status'])
           sleep(0.10)
           print(gr+ "\t\t Region: " +unknown5+ test)
           sleep(0.10)
           print(gr + "\t\t Country: " +unknown3+ labs['country'])
           sleep(0.10)
           print(gr + "\t\t City: " +unknown6+ labs['city'])
           sleep(0.10)
           print(gr + "\t\t ISP: "+unknown2 + labs['isp'])
           sleep(0.10)
           print(gr + "\t\t Lat,Lon: "+unknown4 + str(labs['lat']) + "," + str(labs['lon']))
           sleep(0.10)
           print(gr + "\t\t ZIPCODE: "+unknown12 + labs['zip'])
           sleep(0.10)
           print(gr + "\t\t TimeZone: " +unknown11+ labs['timezone'])
           sleep(0.10)
           print(gr + "\t\t AS: " +unknown15+ labs['as'])
           sleep(0.10)
           print(pu+"===============================\n"+wi)
         except:
                pass
         sleep(0.60)
         print(purple+"[$]:Start At: {}".format(timenow))
         sleep(0.60)
         print(Blue+"[#]:Checking.......")
         sleep(1.5)
         found = []
         try:
          for p in xrange( int(ports[0]) , int(ports[1])+1):
                        try:
                           servername = socket.getservbyport(int(p))
                        except socket.error:
                           servername = "TCP"
                        except OSError:
                           servername = "TCP"
                        try:
                           con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                           if options.timeout !=None:
                              timeout = options.timeout
                              con.settimeout(int(timeout))
                           else:
                              con.settimeout(0.05)
                           con.connect((ip,int(p)))
                           print(bl + "\n[+]"+gr+":"+wi+"PORT["+gr+str(p)+wi+"/"+cy+servername+wi+"] <="+gr+"OPEN"+wi+"=>")
                           found.append(p)
                        except KeyboardInterrupt:
                                print(rd+"[CTRL+C]:"+yl+"Exiting"+rd+".....")
                                sleep(2.5)
                                if len(found) > 0:
                                 print(gr+"\n["+cy+"*"+gr+"]"+wi+" OPEN PORT(s) "+gr+"Found!\n-----------------------------")
                                 loop =1
                                 for i in found:
                                  try:
                                   servername = socket.getservbyport(int(i))
                                  except socket.error:
                                    servername = "TCP"
                                  except OSError:
                                    servername = "TCP"
                                  print(gr+"\t["+wi+str(loop)+gr+"] "+yl+ip+wi+":"+gr+str(i)+wi+"/"+cy+servername+wi+" STATUS:[ "+gr+"OPEN"+wi+" ]")
                                  loop +=1
                                exit(1)

                        except socket.error:
                              print(rd+"\n[-]"+wi+":PORT["+rd+str(p)+wi+"/"+yl+servername+wi+"] <="+rd+"CLOSE!"+wi+"=>")
                        except:
                              print(rd+"\n[!]"+yl+"[ERROR] Something Went Wrong "+rd+"!!!")

          if len(found) > 0:
                print(rd+"---------------------------------\n[#]"+gr+" Result"+rd+" [#]\n")
                print(gr+"[*] "+wi+"TARGET:"+bl+" {}\n".format(target)+gr+"[*]"+wi+" OPEN PORT(s) "+gr+"Found!\n-----------------------------")
                loop =1
                for i in found:
                 try:
                  servername = socket.getservbyport(int(i))
                 except socket.error:
                  servername = "TCP"
                 except OSError:
                  servername = "TCP"
                 print(gr+"\t["+wi+str(loop)+gr+"] "+yl+ip+wi+":"+gr+str(i)+wi+"/"+cy+servername+wi+" STATUS:[ "+gr+"OPEN"+wi+" ]")
                 loop +=1
                print(gr+"\n[$]"+unknown7+" Shutdown At: {}".format(timenow))
          else:
                print(gr+"---------------------------------\n[#]"+rd+" Result"+gr+" [#]\n")
                print(gr+"[*] "+wi+"TARGET:"+yl+" {}\n".format(target)+wi+"["+rd+"!"+yl+"] OPEN PORT(s):"+rd+" No Open Port(s) Found !! :(")
                print(gr+"[$]"+unknown7+" Shutdown At: {}".format(timenow))
                exit(1)

         except KeyboardInterrupt:
          print(rd+"\n[CTRL+C]:"+yl+"Exiting"+rd+".....")
          sleep(2.5)
          if len(found) > 0:
           print(gr+"\n["+cy+"*"+gr+"]"+wi+" OPEN PORT(s) "+gr+"Found!\n-----------------------------")
           loop = 1
           for i in found:
            try:
               servername = socket.getservbyport(int(i))
            except socket.error:
               servername = "TCP"
            except OSError:
               servername = "TCP"
            print(gr+"\t["+wi+str(loop)+gr+"] "+yl+ip+wi+":"+gr+str(i)+wi+"/"+cy+servername+wi+" STATUS:[ "+gr+"OPEN"+wi+" ]")
            loop+=1
          exit(1)

        else:
                msgerror()
  else:

        print(parse.usage)
        exit(1)

if __name__=="__main__":
        main()
