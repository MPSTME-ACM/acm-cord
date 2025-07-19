# 🧠 ACMCord

A powerful and extendable Discord bot for ACM 25-26 committee, featuring:

- Member registration via Discord commands or webhooks

- PostgreSQL database integration

- Role and nickname assignment

- Email invites with HTML templates

- Webhook support

- Department-aware permissions


## To Do:

- [x] Implement sending mails
- [x] Allow webhooks to trigger commands.
- [ ] Dockerize the bot for changes.
- [ ] Implement proper error handling
- [ ] Implement Logging
- [ ] Refactor confusing variables
- [ ] Add more commands
- [ ] Write proper documentation.
- [ ] Make a good todo list :P

## 📁 Project Structure

```
acmcord/
├── controllers/
│   └── ...Controller.py     # Command Logic
├── errorHandler/
│   └── ...ErrorHandler.py   # Error Handlers
├── .env                     # Environment variables
├── .env.sample              # Environment variables
├── .gitignore               # Git essentials
├── bot.py                   # Entry point
├── config.py                # .env and config values
├── db.py                    # SQLAlchemy database
├── emailUtil.py             # Script to send email
├── initialize.py            # Initialization Script
├── mail.html                # Template HTML email
├── mail.mjml                # Template MJML email
├── memberModel.py           # SQL Model
├── middleware.py            # Custom Decorator
├── README.md                # This
├── requirements.txt         # pip essential
└── webhookAuto.py           # Automate Registration
```

## ⚙️ Features

- ✅ Command: `!register <dept_id> <email> <name>`

    Registers a member, stores them in PostgreSQL, assigns role, sets nickname, and sends an invite.

- ✅ Webhook Support
    Webhook messages in xorrect format can be used to register members — useful for automations.

- ✅ PostgreSQL Integration
All members are stored in a acmcord_members table:

    ```
    email TEXT,
    name TEXT,
    department_id INT,
    role INT,
    invite_link TEXT
    ```

- ✅ Role Assignment
Assigns roles based on:

    Department ID

    Role (Exec, Core, SC)

    Discord Roles are configured via .env.

- ✅ Email Invitations
Uses emailUtil.py to send rich HTML invites using an SMTP server. You can configure:

    ```
    {{name}}
    {{email}}
    {{department}}
    {{link}}
    {{role}}
    ```

- ✅ Delayed Batch Registration
Script send_registers.py takes a CSV and registers each user through the webhook with a delay.

---

# Contact: Kartik Jain <acm.dc.gh@jkartik.in>