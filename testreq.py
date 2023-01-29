import requests
r = requests.post('http://1.gpu.garden:8337/notify',json={"message":"your child was caught saying words that contain [toxicity, adult explict]"})
rtext = r.text
print(rtext)