from jnpr.junos import Device
from jnpr.junos.op.ospf import OspfNeighborTable
import smtplib

MAIL_LOGIN = 'dbhor@outlook.com'
MAIL_PW ='Westerly@1234*'
TO_ADDR = 'dbhor@outlook.com'
MAIL_SERVER ='smtp-mail.outlook.com'
SMTP_SSL_PORT = 587
SUBJ = 'OSPF adjacency test results'

USER = 'labroot'
PASSWD = 'lab123'
R1 ='10.85.164.207'
R2 = '10.85.164.210'

def check_ospf_full_adj(dev, neighbor_count):
    ospf_table = OspfNeighborTable(dev)
    ospf_table.get()
    if len(ospf_table) != neighbor_count:
        return False
    for neighbor in ospf_table:
        if neighbor["ospf_neighbor_state"] != "Full":
            return False
    return True


def str_result(test_result):
    return 'Success' if test_result else 'Fail'


def main():
    with Device(host=R1, user=USER, password=PASSWD) as dev:
        result1 = check_ospf_full_adj(dev, 2)
        print('Test OSPF adjacencies on R1: ' + str_result(result1))

        with Device(host=R2, user=USER, password=PASSWD) as dev:
            result2 = check_ospf_full_adj(dev, 2)
            print('Test OSPF adjacencies on R2: '+ str_result(result2))


            print('Sending email.')
            body_msg = 'Test results: % s, % s, % s\n' % (str_result(result1), str_result(result2))
            msg = 'From: % s\nTo: % s\nSubject: % s\n\n % s\n' % (MAIL_LOGIN, TO_ADDR, SUBJ, body_msg)
            mailserver = smtplib.SMTP(MAIL_SERVER, SMTP_SSL_PORT)
            mailsever.set_debuglevel(1)
            mailserver.ehlo()
            mailserver.starttls()

            mailserver.login(MAIL_LOGIN, MAIL_PW)
            mailserver.sendmail(MAIL_LOGIN, TO_ADDR, msg)
            mailserver.quit()
            print('email sent')

        if __name__ == '__main__':
            main()
