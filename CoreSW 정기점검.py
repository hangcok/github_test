import datetime
import getpass

#       datetime
now = str(datetime.datetime.now())
date_arr = now.split('-')
year = date_arr[0]
month = date_arr[1]
day = date_arr[2][0:2]
log_date = year+month+day # 20201009

COMMANDS = [
        "show chassis alarms | no-more",
        "show chassis environment  | no-more",
        "show chassis hardware | no-more",
        "show chassis fpc | no-more",
        "show chassis power | no-more",
        "show chassis fan | no-more",
        "show chassis routing-engine | no-more",
        'show log messages |match "failed|error" |last 300  | no-more',
        "show system uptime  | no-more",
        "show system core-dump  | no-more",
        'show configuration firewall family inet filter Access-filter | no-more',
        "show route summary  | no-more",
        "show route protocol static  | no-more",
        "show isis adjacency | no-more",
        "show bgp summary  | no-more",
        "show chassis routing-engine  | no-more",
        "show task replication  | no-more",
        "show interfaces description  | no-more",
        'show interfaces  | no-more',
        'show interfaces description  | no-more',
        'show interfaces terse  | no-more',
        'show interfaces extensive | match "Physical interface|error"  | no-more'
]


def main():

# 모든 Tab에서 실행
    for i in range(1, crt.GetTabCount()+1):
        tab=crt.GetTab(i)
        if tab.Session.Connected == True:
                tab.Activate()

                #        hostname
                row = tab.Screen.CurrentRow
                # ù��° �ٿ��� 20��°���� hostname ������ ����
                hostname = tab.Screen.Get(row, 1, row, 50)
                # @ �������� array �� �з�
                arr = hostname.split('@')  # ������@gans-lae001>
                arr1 = arr[1].split('>')

                # log name
                log_filename = log_date + "-" + arr1[0]  # 20201009-gans-lae001>

#                tab.Session.LogFileName="C:\\Users\\sjm01\\Desktop\\김태준\\CRT log\\" + str(log_filename)+ ".log"
                tab.Session.LogFileName ="C:\\CRT log\\" + str(log_filename)+ ".log"
                tab.Screen.Send('\r')
                tab.Session.Log(True)

                # Command enter
                for temp in range(0, len(COMMANDS)):


                    tab.Screen.Send(COMMANDS[temp] + '\r')
                    tab.Screen.WaitForString('@'+arr1[0])



                tab.Session.Log(False)
                tab.Screen.Send("exit" + '\r')


        else:
            crt.Dialog.MessageBox('connection is false')
        
        test tetettstets

ffffffffffff
main()
