# W8_5

Create program which can handle basic user registrations and logins. For this exercise, study the built-in library hashlib. The passwords must be hashed with md5 and hexdigested to a string format. It isn’t necessary to implement unique constraints on usernames as all of the usernames in the tests will be unique.

Main menu options:

* Login
* Register
* Exit

User menu options:

* View profile
* Change passsword (no need to implement)
* Logout

Use “credetials.txt” filename as place to store the credentials in CSV format. The filename can be defined as constant variable on the top-level of the library file. The value separator or delimiter must be a semicolon “;”.

Example “credentials.txt”:
````
0;admin;58d613129c5e71de57ee3f44c5ce16bc
````

Run 1
````
Program starting.
Options:
1 - Login
2 - Register
0 - Exit
Your choice: 2
Insert username: Bob
Insert password: 1234
User registration completed!

Options:
1 - Login
2 - Register
0 - Exit
Your choice: 0
Exiting program.

Program ending.
````

Run 2
````
Program starting.
Options:
1 - Login
2 - Register
0 - Exit
Your choice: 1
Insert username: John
Insert password: WrongPassword
Authentication failed!

Options:
1 - Login
2 - Register
0 - Exit
Your choice: 1
Insert username: John
Insert password: SecretPassword
Authentication successful!

User menu:
1 - View profile
2 - Change password
0 - Logout
Your choice: 1
Profile ID 0 - John

User menu:
1 - View profile
2 - Change password
0 - Logout
Your choice: 0
Logging out...

Options:
1 - Login
2 - Register
0 - Exit
Your choice: 0
Exiting program.

Program ending.
````

Run 3
````
Program starting.
Options:
1 - Login
2 - Register
0 - Exit
Your choice: 2
Insert username: Bob
Insert password: 1234
User registration completed!

Options:
1 - Login
2 - Register
0 - Exit
Your choice: 0
Exiting program.

Program ending.
````

Run 4
````
Program starting.
Options:
1 - Login
2 - Register
0 - Exit
Your choice: 1
Insert username: Bob
Insert password: 1234
Authentication successful!

User menu:
1 - View profile
2 - Change password
0 - Logout
Your choice: 1
Profile ID 1 - Bob

User menu:
1 - View profile
2 - Change password
0 - Logout
Your choice: 0
Logging out...

Options:
1 - Login
2 - Register
0 - Exit
Your choice: 0
Exiting program.

Program ending.
````
