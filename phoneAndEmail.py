#! python3

import re, pyperclip

#create a regex for phone numbers

phoneRegex = re.compile(r'''
# 555-111-1234, 111-1234, (555) 111-1234
(
((\d\d\d)|(\(\d\d\d\)))?            #area code(optional)
(\s|-)            #first separator
\d\d\d            #first 3 digits
-                 #separator
\d\d\d\d          #last 4 digits
)
''', re.VERBOSE)

#TODO: create regex for email addresses

emailRegex = re.compile(r'''

[a-zA-Z-9_.+]+        #name part
@                     #@ symbol
[a-zA-Z-9_.+]+        #domain name part


''', re.VERBOSE)

#TODO: get the text off the clipboard

text = pyperclip.paste()

#TODO: extract the email addresses and phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#TODO: copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
