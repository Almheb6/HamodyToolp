<h1 align="center">HamodyTools</h1>
<p align="center">It's a Usefull Project for Developers ... It show instagram business email </p>

<p align="center"> • DevVloper The Lib BY 7AMODY • </p>

## Installing :
```
pip install HamodyTools

``` python
from HamodyTools import Hamody

user = "<user get email>"
sessionid = "<sessionid instagram>"
check = Hamody.get(user,sessionid)

if check == False:
	print ("• Email Is Not Business ")
	
else:
	print(check)
	#check : email = ******@****.com
	
```