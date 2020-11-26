from sshtunnel import SSHTunnelForwarder
from paramiko import SSHClient

server = SSHTunnelForwarder(
    'efg.hdfcbank.com',
    ssh_username="CTRUENORTH",
    ssh_password="Bank@123",
    remote_bind_address=('127.0.0.1', 8080)
)

server.start()

print(server.local_bind_port)  # show assigned local port
# work with `SECRET SERVICE` through `server.local_bind_port`.
with SSHClient() as ssh:
    ssh.connect('efg.hdfcbank.com',
                port=server.local_bind_port,
                username='CTRUENORTH',
                password='Bank@123',
                )
    print(ssh.exec_command('-d'))
server.stop()
