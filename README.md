# whatsapp-auto-atp
### AI Tech Park Sdn. Bhd. official WhatsApp GitHub repository.

## Required Data in Excel File
Every field is Nullable.

Fields:
- Name
- Send Type
    - 0 for phone send
    - 1 for group send
- Phone
    - For personal message
- Group ID
    - The WhatsApp group ID
- greeting
    - The thing that comes after "Hello" ("Hello (the word)"). For example, "Hello all" / "Hello everyone".
    - Will only apply if sending to a group.
    - You can use "all" or "everyone" if you want to tell multiple people in the same group. Else, just leave empty.

🔗 Sample Excel file link: 

## Message.txt Format
**Do not change first line. Change the number only.**
- The message that will be sent is the rest of the file other than the first line.
- Use "{0}" to insert the greeting. Eg: Hello {0}, --> Hello Shrijan, || (In case a greeting is specified) Hello {0}, --> Hello everyone,
