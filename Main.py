import Server.MServer as MS
import Client.MClient as MC

def main():
  ms = MS.MServer()
  mc = MC.MClient()
  print(ms.stest())
  print(mc.test())
  

if __name__=="__main__":
  main()
