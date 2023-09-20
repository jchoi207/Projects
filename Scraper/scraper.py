import imaplib
import email 

f = open("credentials.txt", "r")                      # txt file contains email address and gmail pw

user, password = f.readline(), f.readline()           # readline() queues the next line

imap_url = 'imap.gmail.com'                           
M = imaplib.IMAP4_SSL(imap_url) 
M.login(user, password)

M.select('Inbox')


typ, data = M.search(None, 'ALL')


messages = []
for email_number in data[0].split():                 # akin to address of specific emails
    typ, data = M.fetch(email_number, '(RFC822)')    # (RFC822) gets the entire mesage
    messages.append(data) 


for msg in messages[::-1]:                           # iterate through messages newest to latest
    for content_types in msg:                        # go thorugh the different content types (message, headers)
        if type(content_types) is tuple:                
            my_message = email.message_from_bytes((content_types[1])) # M.fetch() returns email content as tuples. make sure all content is valid, 
                                                                                        
            print("Subject:", my_message['subject'])   
            print("From:", my_message['from'])         

            print("Content:") 
            for part in my_message.walk():            # traverses through the parts of the email 
                if part.get_content_type() == 'text/plain': # choose and print only the parts that are text (content)
                    print(part.get_payload(decode=True).decode('utf-8'))


# colored(guesses[i][j], colors[i][j], attrs=["reverse", "blink"])
