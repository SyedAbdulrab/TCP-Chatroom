# TCP Chatroom

This is a Python implementation of a TCP chatroom using sockets. It allows multiple users to connect to a server and chat with each other in real time. Some of the features include:

- Admin mode: only users with admin privileges can kick or ban other users from the chatroom.
- Kick functionality: admins can kick users from the chatroom.
- Ban functionality: admins can ban users from the chatroom, preventing them from reconnecting.
- Private messaging: users can send private messages to each other.

## Getting started

To use the chatroom, you need to run the server and then connect to it from one or more clients. Here are the steps:

1. Clone this repository: `git clone https://github.com/yourusername/tcp-chatroom.git`.
2. Navigate to the project directory: `cd tcp-chatroom`.
3. Run the server: `python server.py`.
4. In another terminal or command prompt, run a client: `python client.py`.
5. Enter a username when prompted.
6. Chat away!

To run multiple clients, simply repeat step 4 and 5 in additional terminals or command prompts.

## Usage

### Commands

The following commands are available in the chatroom:

- `/private <username> <message>`: sends a private message to the specified user.
- `/kick <username>`: kicks the specified user from the chatroom (admin only).
- `/ban <username>`: bans the specified user from the chatroom (admin only).
- `/admin <password>`: elevates the user to admin status (if the password is correct).

### Admin mode

To use the admin mode, you need to know the admin password (which is hardcoded in the server.py file). Once you know the password, you can use the `/admin <password>` command to elevate your user to admin status. Admins can then use the `/kick <username>` and `/ban <username>` commands to kick or ban users from the chatroom.

### Private messaging

To send a private message to a user, use the `/private <username> <message>` command. The message will only be visible to the specified user.

## LICENSE:

I created this super cool application as an end semester project for my Computer Networks course. All of you are more than welcome to use it. Hope ya'll enjoy!
