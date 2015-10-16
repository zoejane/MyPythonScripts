
#! python3

import re,pyperclip

#TODO:Create a regex for phone numbers


phoneRegex=re.compile(r'''
# 415-555-0000, 555-00000, (415) 555-0000,555-0000 ext12345, ext. 12345, x12345

( (\d\d\d) | (\ (\d\d\d) ) )? # area code (optional)
(\s|-)                    #first seperator
\d\d\d                   #first 3digits
-                        #separator
\d\d\d\d                 #last 4 digits
( ( ( ext(\.)?\s)|x) #extension word-part(optional)
 ( \d{2,5}) )?       #extension number-part(optional)


''',re.VERBOSE)

#TODO:Create a regex for email addressed
emailRegex=re.compile(r'''

#some.+_thing@s(\d{2,5}))?.com

{a-zA-Z0-9_.+}+        #name part
@        # @ symbol
{a-zA-Z0-9_.+}+         #domain name part

''',re.VERBOSE)

#TODO:Get the text off the clipboard
text =pyperclip.paste()


#TODO:Extract the email/phone from this text
extractedPhone=phoneRegex.findall(text)

#TODO: Copy the extraced email/phone to the clipboard
extractedEmail=emailRegex.findall(text)

print(extractedPhone)
print(extractedEmail)
