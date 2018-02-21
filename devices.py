import pandas as pd
import requests
import matplotlib.pyplot   as plt

from managedevices.globals import username,password,CONFLUENCE_LOGIN_URL,CONFLUENCE_DEVICE_TRACKING_URL

s = requests.session()

s.post(CONFLUENCE_LOGIN_URL, data={"os_username": username, "os_password": password}, verify=False)

result = s.get(CONFLUENCE_DEVICE_TRACKING_URL, verify=False).content
print(result)
table = pd.read_html(result)
android_device = table[0]


phone_device = android_device[android_device[4] == 'Tablet']

phone_device.to_csv("devices_tablet.csv")

print(phone_device)
print(phone_device.groupby(5).size())
print(phone_device.groupby(1).size())
sum_df = phone_device.groupby(5).size()

sum_df.plot(kind='pie', subplots=True, autopct='%.2f', figsize=(8, 8), title = "Versions", legend = True,y="devices")  # 显示百分比
plt.show()