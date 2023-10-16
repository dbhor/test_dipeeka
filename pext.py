import requests
def get_auth_token():
    details = {}
    details['username'] = 'dbhor@juniper.net'
    details['passwd'] = 'Ec2_ebs@2020'# Add your password here
    details['url'] = 'https://api.mistsys.com'
    user = details['username']
    passwd = details['passwd']
    url = details['url']+"/api/v1/login"
    headers = {"Content-Type": "application/json"}
    data = {"email": user, "password": passwd}
    sess = requests.session()
    print(sess)
    resp = sess.post(url=url, headers=headers, json=data, verify=False)
    print(resp)
    token = resp.cookies['csrftoken']
    print(token)
    return(sess, token)







