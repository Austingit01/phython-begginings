#import module_1
from module_1 import get_name, get_email as get_email_address

#print(module_1.get_name('Gracious','John'))
print(get_name('Gracious','John'))

email = 'john@gmail.com'
#print(get_email(email))
print(get_email_address(email))

