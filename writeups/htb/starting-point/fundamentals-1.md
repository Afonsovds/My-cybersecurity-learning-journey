# HTB Starting Point - Fundamentals 1: Service Exploration (Web, FTP, MySQL)

Objective: Practice interacting with and exploring different services to understand how they work and how they can expose information.

First, I identified the available services on the target and manually connected to them to explore their functionality.

FTP:
I connected to the FTP service and navigated through the available files and directories.

```bash
ftp IP
```

This helped me understand how file transfer services operate and how misconfigurations can expose sensitive information.

MySQL:
I accessed the MySQL service using valid credentials provided during the exercise.

```bash
mysql -h IP -u USER -p
```

After connecting, I explored the database structure and executed basic queries to inspect the stored data.

Web Services:
I interacted with the web applications running on the target through the browser.

I explored the available pages, observed how the applications behaved, and identified how different services can provide useful information during an assessment.

Result:
By manually exploring each service, I gained practical experience interacting with commonly exposed technologies and understanding their purpose.

What I learned:

* How to connect to and navigate FTP services.
* Basic interaction with MySQL databases.
* How web applications can reveal valuable information.
* The importance of understanding how services function before attempting exploitation.
* That exploration and observation are key parts of the assessment process.

Conclusion:
This module showed that penetration testing is not only about finding vulnerabilities. Understanding how services work and learning to interact with them confidently is essential for building a strong foundation in cybersecurity.
