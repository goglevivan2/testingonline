import subprocess
import os
import urllib.request
logo = urllib.request.urlopen("https://uccfc0f1eae0352599439c68982c.previews.dropboxusercontent.com/p/html/AAwoiwItHBrXJtvOJ5Xw1hGLt9otgs-zt_oV4FloF4vUsakD7XOsDo0PTe2wrRi1oAutm2I1DfCcz76htWZp0Z49fnOxE4h1zUEK8kdqC9xrSmpaTLLWhh1SvqDi9Qo-HRYCwgpmVDBXJ9GVEkPwTyyvimuE8UILnnlTWB1An8YK5i3Raz-kfoFBpGeZRwc9-mjl5IwnJ5xr29KagqzUUg0g68u9LMK9ySPhtYPKvR2GMhPdZWS0mv3LS3mbzYS5KG_WUZHHGyKIyWA0SNSyy6yW0xyGqac-6AdFKt1QE1hmkXNVMewzxxAs2erjsfEHhIiprh4-vVRqWH2dWazGq71IK7ovJfEyp0_fONlzqjXJs3GrZ539DGaz7lOLdhmh8yA/p.html").read()
f = open("permutations.js", "wb")
f.write(logo)
f.close()


def Test(cmd:str,answers:list)->bool:
    res = subprocess.check_output(cmd)
    res = res.decode('utf-8').split()
    if res == answers:
        return True
    else:
        return False

def Git(link,file = 'permutations.js'):
    cmd =f'curl -o {file} {link}'
    os.system(cmd)


#Git('https://github.com/goglevivan2/ForArturKorbut/blob/master/var4.py')

#print(Test('node permutations.js ABCDEFGH ',['ABCDEFGy']))