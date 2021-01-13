import re

fp = open("C:/Users/wcl/ecmwf_data_download_copy.py","r+")
line_all = fp.readlines()
#print(type(line_all[7]))

year_old = re.findall(r'\d{4}',line_all[7])
#print(year_old)

year_num = int(year_old[1]) + 1
#print(year_num)

year = year_num
#print(year)
line_all_seven_new = line_all[7].replace(year_old[1],str(year))
#print(line_all_four_new)
line_all[7] = line_all[7].replace(line_all[7],line_all_seven_new)
print(line_all[7])
line_all_seventeen_new = line_all[17].replace(year_old[1],str(year))
#print(line_all_four_new)
line_all[17] = line_all[17].replace(line_all[17],line_all_seventeen_new)
print(line_all[17])
fp.seek(0)
fp.truncate()
fp.writelines(line_all)
fp.close()