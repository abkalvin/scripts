{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import socket\n",
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "server_address = ('localhost', 10000)\n",
    "sock.bind(server_address)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "sock.listen(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "while True:\n",
    "    # Wait for a connection\n",
    "    print(\"Waiting for a connection...\")\n",
    "    connection, client_address = sock.accept()\n",
    "\n",
    "    try:\n",
    "        # Send two random numbers to the client\n",
    "        num1 = random.randint(0, 20)\n",
    "        num2 = random.randint(0, 20)\n",
    "        connection.sendall(str(num1).encode())\n",
    "        connection.sendall(str(num2).encode())\n",
    "\n",
    "        # Receive the summation from the client\n",
    "        sum = connection.recv(16).decode()\n",
    "        sum = int(sum)\n",
    "\n",
    "        # Check if the summation is correct\n",
    "        if sum == num1 + num2:\n",
    "            connection.sendall(\"Correct!\".encode())\n",
    "        else:\n",
    "            connection.sendall(\"Incorrect!\".encode())\n",
    "    finally:\n",
    "        # Clean up the connection\n",
    "        connection.close()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "b671c20432fcd147198c92e7f072af9e705f087eb990bee22b07f08caab9f630"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
