import bin.Take_Password
import bin.Take_ALL_Site
import bin.Replace
import bin.New_data
import bin.Delete_data


print('\nTo get all site names press - 1\n\
To change the password press - 2\n\
To get the password press - 3\n\
To add data press - 4\n\
To delete data press - 5')
User_response = int(input('\nMake your choice: '))

if User_response == 1:
    bin.Take_ALL_Site.take_all_name_site()

elif User_response == 2:
    bin.Replace.replace_password()

elif User_response == 3:
    bin.Take_Password.take_password()

elif User_response == 4:
    bin.New_data.add_new_data()

else:
    bin.Delete_data.delete_data()
